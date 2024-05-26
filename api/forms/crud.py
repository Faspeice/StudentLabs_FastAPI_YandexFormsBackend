from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.models import Form, Question, Option, User
from sqlalchemy.engine import Result
from .schemas import FormCreate, FormUpdatePartial, FullForm


async def get_forms_by_user(session: AsyncSession, username: str) -> list[Form]:
    st = select(User.id).where(User.username == username)
    resultus: Result = await session.execute(st)
    row = resultus.fetchone()
    if row:
        stmt = select(Form).where(Form.user_id == int(row[0]))
        result: Result = await session.execute(stmt)
        forms = result.scalars().all()
        return list(forms)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"this User not found",
    )


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
    questions = []
    for question_data in form_in.questions:
        question = Question(
            text=question_data.text,
            type=question_data.type,
            form_id=form.id,
            number=question_data.number,
        )
        session.add(question)
        questions.append(question)
    await session.flush()
    for question, question_data in zip(questions, form_in.questions):
        if question_data.options:
            for option_data in question_data.options:
                option = Option(
                    text=option_data.text,
                    question_id=question.id,
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


async def delete_form(
    session: AsyncSession,
    form: Form,
) -> None:
    await session.execute(delete(Form).where(Form.id == form.id))
    await session.commit()


# why noе cascase='delete'?
