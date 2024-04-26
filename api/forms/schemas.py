from typing import List

from pydantic import BaseModel, ConfigDict


class CreateQuestion(BaseModel):
    text: str
    number: int
    type: str


class Question(CreateQuestion):
    model_config = ConfigDict(from_attributes=True)
    id: int


class FormBase(BaseModel):
    description: str
    user_id: int
    questions: List["CreateQuestion"] | None = None


class FormCreate(FormBase):
    pass


class FormUpdatePartial(FormCreate):
    user_id: int | None = None
    description: str | None = None


class Form(FormBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
