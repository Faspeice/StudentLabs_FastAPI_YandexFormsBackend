from sqlalchemy import Table, Column, ForeignKey, Integer

from .base import Base

checkbox_answers_association = Table(
    "checkbox_answers_association",
    Base.metadata,
    Column(
        "checkboxanswer_id",
        Integer,
        ForeignKey("checkboxanswers.id"),
        primary_key=True,
    ),
    Column("option_id", Integer, ForeignKey("options.id"), primary_key=True),
)
