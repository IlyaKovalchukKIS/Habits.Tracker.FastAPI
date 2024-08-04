from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    email: почта пользователя
    name_telegram: имя пользователя
    is_active: активен ли пользователь
    is_superuser: является ли пользователь суперпользователем
    is_admin: является ли пользователь админом
    """

    email: EmailStr
    name_telegram: str
    is_active: bool | None
    is_superuser: bool | None
    is_admin: bool | None


class UserCreate(UserBase):
    """
    hashed_password: хэш пароля
    """

    hashed_password: str


class UserRead(UserBase):
    """
    id: номер пользователя
    id_telegram: id пользователя в телеграм
    created_at: дата создания пользователя
    """

    id: int
    id_telegram: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """
    name_telegram: имя пользователя
    id_telegram: id пользователя в телеграм
    hashed_password: хэш пароля
    """

    name_telegram: str
    id_telegram: int
    hashed_password: str
