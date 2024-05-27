from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Form, TextAnswer, RadioAnswer, CheckboxAnswer, Option
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
    form_query = select(Form).where(Form.id == answer_in.form_id)
    form_result = await session.execute(form_query)
    form = form_result.scalars().first()

    if not form:
        raise HTTPException(status_code=404, detail="Form not found")

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
    checkbox_answers = []
    if answer_in.checkbox_answers:
        for checkbox_data in answer_in.checkbox_answers:
            options_query = select(Option).where(Option.id.in_(checkbox_data.options))
            result = await session.execute(options_query)
            options = result.scalars().all()
            checkbox_answer = CheckboxAnswer(options=options)
            checkbox_answers.append(checkbox_answer)
    session.add_all(text_answers + radio_answers + checkbox_answers)
    await session.commit()
    return jsonable_encoder(answer_in)
