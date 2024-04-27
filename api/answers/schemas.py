from typing import List

from pydantic import BaseModel, ConfigDict


class TextAnswerSchema(BaseModel):
    question_id: int
    text: str


class RadioAnswerSchema(BaseModel):
    option_id: int


class CheckboxAnswerSchema(BaseModel):
    options: List[int]


class FormAnswerSchema(BaseModel):
    form_id: int
    text_answers: List[TextAnswerSchema] | None = None
    radio_answers: List[RadioAnswerSchema] | None = None
    checkbox_answers: List[CheckboxAnswerSchema] | None = None
