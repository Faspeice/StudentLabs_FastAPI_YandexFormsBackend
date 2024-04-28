from core.models import User
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user_in: User, session: AsyncSession) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
    )
    session.add(user)
    await session.commit()
    return user


async def delete_user(user: User, session: AsyncSession) -> None:
    await session.delete(user)
    await session.commit()


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)
