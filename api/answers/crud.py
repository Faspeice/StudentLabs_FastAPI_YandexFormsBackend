from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Form, TextAnswer, RadioAnswer, CheckboxAnswer
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
    text_answers = (
        [TextAnswer(**data.dict()) for data in answer_in.text_answers]
        if answer_in.text_answers
        else []
    )
    radio_answers = (
        [RadioAnswer(**data.dict()) for data in answer_in.radio_answers]
        if answer_in.radio_answers
        else []
    )
    checkbox_answers = (
        [CheckboxAnswer(**data.dict()) for data in answer_in.checkbox_answers]
        if answer_in.checkbox_answers
        else []
    )

    # Добавьте экземпляры в сессию
    session.add_all(text_answers + radio_answers + checkbox_answers)
    await session.commit()
    # await session.refresh(form)
    return jsonable_encoder(answer_in)
