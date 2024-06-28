import logging
from fastapi import Depends, FastAPI, Request, Response
from app.api import ping
from app.api import summaries
from app.config import Settings, get_settings
from app.middlewares.cors import add_cors
from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope

from app.models.User import User
from app.services.auth import get_admin_user

log = logging.getLogger("uvicorn")

initialize(
    tenant_id_="", 
    client_id_=""
)

excepted_scope = "data.read"



def create_application(settings: Settings = Depends(get_settings)) -> FastAPI:
    application = FastAPI(
        version=settings.VERSION, 
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        swagger_ui_oauth2_redirect_url='/oauth2-redirect',
        swagger_ui_init_oauth={
            "usePkceWithAuthorizationCodeGrant": True,
            "clientId": settings.SWAGGER_UI_CLIENT_ID,
            "scopes": [f'api://{settings.API_CLIENT_ID}/access_as_user']
        }

    )
    add_cors(application)
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()

@app.get("/")
@requires_auth
async def root(request: Request, user: User = Depends(get_admin_user)):
    try:
        validate_scope(request, excepted_scope)
        return "Jinja Template"
    except AuthError as e:
        return Response(status_code=e.status_code, content=e.message)



# @app.on_event("startup")
# async def startup_event():
#     log.info("Starting up...")
#     #initialise db here...


# @app.on_event("shutdown")
# def shutdown_event():
#     log.info("Application Shutdown")
