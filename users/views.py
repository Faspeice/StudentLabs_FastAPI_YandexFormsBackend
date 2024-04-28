from fastapi import APIRouter, Depends, HTTPException, status

from core.models import db_helper
from users.dependencies import user_by_id
from users.schemas import User
from users import crud
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(
    user: User,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        return await crud.create_user(session=session, user_in=user)
    except:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User already exists",
        )


@router.delete("/{user_id}")
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_user(session=session, user=user)
