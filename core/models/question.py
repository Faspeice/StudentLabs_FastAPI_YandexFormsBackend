from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .form import Form
    from .option import Option


class Question(Base):
    text: Mapped[str]
    number: Mapped[int]
    type: Mapped[str]
    form_id: Mapped[int] = mapped_column(ForeignKey("forms.id"))
    form: Mapped["Form"] = relationship(back_populates="questions")
    options: Mapped[list["Option"]] = relationship(back_populates="question")
