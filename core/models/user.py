from pydantic import EmailStr
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .form import Form


class User(Base):
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped["EmailStr"] = mapped_column(String(32), unique=True)
    forms: Mapped[list["Form"]] = relationship(
        cascade="all, delete", back_populates="user"
    )
