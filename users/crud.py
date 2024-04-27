from core.models import User
from users.schemas import CreateUser
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(user_in: CreateUser, session: AsyncSession) -> User:
    user = User(
        username=user_in.username,
        email=user_in.email,
    )
    session.add(user)
    await session.commit()
    return user
