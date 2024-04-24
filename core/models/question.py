from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .form import Form


class Question(Base):
    text: Mapped[str]
    form_id: Mapped[int] = relationship(back_populates="form")
