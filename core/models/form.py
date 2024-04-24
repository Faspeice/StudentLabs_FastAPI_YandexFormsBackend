from sqlalchemy.orm import Mapped

from .base import Base


class Form(Base):
    __tablename__ = "forms"
    type: Mapped[str]
    description: Mapped[str]
