from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    name_telegram: str


class UserUpdate(schemas.BaseUserUpdate):
    pass
