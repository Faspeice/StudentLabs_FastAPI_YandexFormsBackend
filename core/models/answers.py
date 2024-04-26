from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING
from .option_Answer_association import checkbox_answers_association

if TYPE_CHECKING:
    from .option import Option


class TextAnswer(Base):
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    text: Mapped[str]


class RadioAnswer(Base):
    option_id: Mapped[int] = mapped_column(ForeignKey("options.id"))


class CheckboxAnswer(Base):
    __tablename__ = "checkboxanswers"
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    options: Mapped[list["Option"]] = relationship(
        secondary=checkbox_answers_association, back_populates="checkbox_answers"
    )
