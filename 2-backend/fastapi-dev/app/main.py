import logging
from fastapi import FastAPI
from app.api import ping
from app.api import summaries
from app.middlewares.cors import add_cors

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI(version="1.0.0", title="Visual IDMA Service")
    add_cors(application)
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()

@app.get("/")
async def root():
    return "Jinja Template"



# @app.on_event("startup")
# async def startup_event():
#     log.info("Starting up...")
#     #initialise db here...


# @app.on_event("shutdown")
# def shutdown_event():
#     log.info("Application Shutdown")
