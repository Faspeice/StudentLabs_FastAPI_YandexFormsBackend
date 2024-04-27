from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import (
    FormAnswerSchema,
    TextAnswerSchema,
    CheckboxAnswerSchema,
    RadioAnswerSchema,
)

router = APIRouter(tags=["Answer"])


@router.post("/submit-form/")
async def submit_form_answers(
    answer_in: FormAnswerSchema,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.submit_answer(answer_in=answer_in, session=session)
