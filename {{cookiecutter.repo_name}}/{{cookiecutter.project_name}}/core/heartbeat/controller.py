from fastapi import APIRouter

router = APIRouter(tags=["health-check"])


@router.get("/ping", response_model=str)
async def get_leads_search() -> str:
    return "pong"
