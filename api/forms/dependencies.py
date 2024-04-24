from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Form

from . import crud


async def form_by_id(
    form_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Form:
    form = await crud.get_form(session=session, form_id=form_id)
    if form:
        return form
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Form {form_id} not found",
    )
