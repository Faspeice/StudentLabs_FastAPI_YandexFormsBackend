from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Form
from sqlalchemy.engine import Result
from .schemas import (
    FormAnswerSchema,
    TextAnswerSchema,
    RadioAnswerSchema,
    CheckboxAnswerSchema,
)


async def submit_answer(
    session: AsyncSession, answer_in: FormAnswerSchema
) -> FormAnswerSchema | None:
    answer = FormAnswerSchema(**answer_in.model_dump())
    session.add(answer.text_answers)
    session.add(answer.radio_answers)
    session.add(answer.checkbox_answers)
    await session.commit()
    # await session.refresh(form)
    return answer
