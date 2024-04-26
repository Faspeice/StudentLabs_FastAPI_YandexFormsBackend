from pydantic import BaseModel, ConfigDict


class FormBase(BaseModel):
    description: str
    user_id: int


class FormCreate(FormBase):
    pass


class FormUpdatePartial(FormCreate):
    user_id: int | None = None
    description: str | None = None


class Form(FormBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
