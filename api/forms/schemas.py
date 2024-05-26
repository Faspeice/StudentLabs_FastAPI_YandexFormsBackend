from typing import List

from pydantic import BaseModel, ConfigDict


class CreateQuestion(BaseModel):
    text: str
    number: int
    type: str
    options: List["CreateOption"] | None = None


class Question(CreateQuestion):
    model_config = ConfigDict(from_attributes=True)
    id: int


class CreateOption(BaseModel):
    text: str


class Option(CreateOption):
    model_config = ConfigDict(from_attributes=True)
    id: int


class FormBase(BaseModel):
    description: str
    user_id: int


class FormCreate(FormBase):
    questions: List["CreateQuestion"] | None = None


class FullForm(FormCreate):
    id: int


class FormUpdatePartial(FormCreate):
    user_id: int | None = None
    description: str | None = None


class Form(FormBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
