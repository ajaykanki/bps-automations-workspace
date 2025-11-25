from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck", summary="Health Check")
async def healthcheck():
    return {"status": "ok"}
