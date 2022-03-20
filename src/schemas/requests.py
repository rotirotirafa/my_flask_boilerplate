from typing import Optional

from pydantic import BaseModel


class BodyUserCreateSchema(BaseModel):
    #TODO user_type é interessante ser ENUM
    email: str
    password: str or int
    user_type: str


class BodyUserUpdateSchema(BaseModel):
    email: str
    user_type: str


class QueryUserParamsSchema(BaseModel):
    user_id: int = None

