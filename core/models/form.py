from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .question import Question


class Form(Base):
    __tablename__ = "forms"
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="forms")
    questions: Mapped[list["Question"]] = relationship(
        cascade="all, delete", back_populates="form"
    )
