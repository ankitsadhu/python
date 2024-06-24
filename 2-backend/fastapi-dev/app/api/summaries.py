from fastapi import APIRouter, HTTPException, Path


from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/{id}/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema, id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary_id = id  # db call
    print(f"------> {id}")

    response = {"id": summary_id, "url": payload.url}

    if not summary_id:
        raise HTTPException(status_code=404, detail="Summary not found")

    return response
