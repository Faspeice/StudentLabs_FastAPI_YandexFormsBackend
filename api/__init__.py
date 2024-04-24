from fastapi import APIRouter

from .forms.views import router as forms_router

router = APIRouter()
router.include_router(router=forms_router, prefix="/forms")
