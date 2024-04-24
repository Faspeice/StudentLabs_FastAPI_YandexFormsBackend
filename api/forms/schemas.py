from pydantic import BaseModel, ConfigDict


class FormBase(BaseModel):
    type: str
    description: str


class FormCreate(FormBase):
    pass


class FormUpdatePartial(FormCreate):
    type: str | None = None
    description: str | None = None


class Form(FormBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
