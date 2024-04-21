from fastapi import APIRouter
from api.bases import api_router
from view.bases import view_router

all_router = APIRouter()

all_router.include_router(api_router)
all_router.include_router(view_router)