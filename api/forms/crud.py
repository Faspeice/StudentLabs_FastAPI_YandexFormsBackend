from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Form
from sqlalchemy.engine import Result
from .schemas import FormCreate, FormUpdatePartial


async def get_forms(session: AsyncSession) -> list[Form]:
    stmt = select(Form, Form.id).order_by(Form.id)
    result: Result = await session.execute(stmt)
    forms = result.scalars().all()
    return list(forms)


async def get_form(session: AsyncSession, form_id: int) -> Form | None:
    return await session.get(Form, form_id)


async def create_form(session: AsyncSession, form_in: FormCreate) -> Form | None:
    form = Form(**form_in.model_dump())
    session.add(form)
    await session.commit()
    # await session.refresh(form)
    return form


async def update_form_partial(
    session: AsyncSession, form: Form, form_update: FormUpdatePartial
):
    for name, value in form_update.model_dump(exclude_unset=True).items():
        setattr(form, name, value)
    await session.commit()
    return form


async def delete_form(
    session: AsyncSession,
    form: Form,
) -> None:
    await session.delete(form)
    await session.commit()
