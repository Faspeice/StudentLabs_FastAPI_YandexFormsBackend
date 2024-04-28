from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Form, FormCreate, FormUpdatePartial
from .dependencies import form_by_id, form_by_user

router = APIRouter(tags=["Forms"])


@router.get("/", response_model=list[Form])
async def get_forms(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_forms(session=session)


@router.post("/", response_model=Form, status_code=status.HTTP_201_CREATED)
async def create_form(
    form_in: FormCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_form(session=session, form_in=form_in)


@router.get("/{form_id}/", response_model=Form)
async def get_form(form: Form = Depends(form_by_id)):
    return form


@router.get("/user/{user_id}/", response_model=list[Form])
async def get_form(forms: list["Form"] = Depends(form_by_user)):
    return forms


@router.patch("/{form_id}/")
async def update_form(
    form_update: FormUpdatePartial,
    form: Form = Depends(form_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_form_partial(
        session=session, form=form, form_update=form_update
    )


@router.delete("/{form_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_form(
    form: Form = Depends(form_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_form(session=session, form=form)
