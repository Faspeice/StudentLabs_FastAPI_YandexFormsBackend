from typing import List

from pydantic import BaseModel, ConfigDict


class TextAnswerSchema(BaseModel):
    question_id: int
    text: str


class RadioAnswerSchema(BaseModel):
    question_id: int
    selected_option_id: int


class CheckboxAnswerSchema(BaseModel):
    selected_options_ids: List[int]


class FormAnswerSchema(BaseModel):
    form_id: int
    text_answers: List[TextAnswerSchema] | None = None
    radio_answers: List[RadioAnswerSchema] | None = None
    checkbox_answers: List[CheckboxAnswerSchema] | None = None
