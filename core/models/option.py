from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING
from .option_Answer_association import checkbox_answers_association

if TYPE_CHECKING:
    from .question import Question
    from .answers import CheckboxAnswer


class Option(Base):
    __tablename__ = "options"
    text: Mapped[str]
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE")
    )
    question: Mapped["Question"] = relationship(back_populates="options")
    checkbox_answers: Mapped[list["CheckboxAnswer"]] = relationship(
        secondary=checkbox_answers_association, back_populates="options"
    )
