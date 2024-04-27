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
            # Асинхронно извлекаем объекты Option по идентификаторам из checkbox_data.options
            options_query = select(Option).where(Option.id.in_(checkbox_data.options))
            result = await session.execute(options_query)
            options = result.scalars().all()
            # Создаем экземпляр CheckboxAnswer и связываем его с найденными объектами Option
            checkbox_answer = CheckboxAnswer(options=options)
            checkbox_answers.append(checkbox_answer)

    # Добавьте экземпляры в сессию
    session.add_all(text_answers + radio_answers + checkbox_answers)
    await session.commit()
    # await session.refresh(form)
    return jsonable_encoder(answer_in)
