from fastapi import APIRouter

from .forms.views import router as forms_router
from .answers.views import router as answers_router

routerAns = APIRouter()
routerForm = APIRouter()
routerForm.include_router(router=forms_router, prefix="/forms")
routerAns.include_router(router=answers_router, prefix="/answers")
