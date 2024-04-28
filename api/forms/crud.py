from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.models import Form, Question, Option
from sqlalchemy.engine import Result
from .schemas import FormCreate, FormUpdatePartial


async def get_forms_by_user(session: AsyncSession, user_id: int) -> list[Form]:
    stmt = select(Form).where(Form.user_id == user_id)
    result: Result = await session.execute(stmt)
    forms = result.scalars().all()
    return list(forms)


async def get_forms(session: AsyncSession) -> list[Form]:
    stmt = select(Form, Form.id).order_by(Form.id)
    result: Result = await session.execute(stmt)
    forms = result.scalars().all()
    return list(forms)


async def get_form(session: AsyncSession, form_id: int):
    result = await session.execute(
        select(Form)
        .options(selectinload(Form.questions).selectinload(Question.options))
        .where(Form.id == form_id)
    )
    return result.scalars().first()


async def create_form(session: AsyncSession, form_in: FormCreate) -> Form | None:
    form = Form(
        description=form_in.description,
        user_id=form_in.user_id,
    )
    session.add(form)
    await session.flush()
    for question_data in form_in.questions:
        question = Question(
            text=question_data.text,
            type=question_data.type,
            form_id=form.id,
            number=question_data.number,
        )
        session.add(question)
        for option_data in question_data.options:
            option = Option(
                text=option_data.text,
                question_id=option_data.question_id,
            )
            session.add(option)
    await session.commit()
    return jsonable_encoder(form)


async def get_questions_by_form_id(
    session: AsyncSession, form_id: int
) -> list[Question]:
    stmn = select(Question).where(Question.form_id == form_id)
    result: Result = await session.execute(stmn)
    questions = result.scalars().all()
    return list(questions)


async def get_options_by_q_id(session: AsyncSession, question_id: int) -> list[Option]:
    stmn = select(Option).where(Option.question_id == question_id)
    result: Result = await session.execute(stmn)
    options = result.scalars().all()
    return list(options)


async def update_form_partial(
    session: AsyncSession, form: Form, form_update: FormUpdatePartial
):
    for question_data in form_update.questions:
        question = Question(
            text=question_data.text,
            type=question_data.type,
            form_id=form.id,
            number=question_data.number,
        )
        for name, value in question_data.model_dump(exclude_unset=True).items():
            setattr(question, name, value)
        for option_data in question.options:
            option = Option(
                text=option_data.text,
                question_id=option_data.question_id,
            )
            for name, value in option_data.model_dump(exclude_unset=True).items():
                setattr(option, name, value)
    await session.commit()
    return form


async def delete_form(
    session: AsyncSession,
    form: Form,
) -> None:
    await session.execute(delete(Form).where(Form.id == form.id))
    await session.commit()


# why noе cascase='delete'?
