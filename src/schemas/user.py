from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    email: почта пользователя
    name_telegram: имя пользователя
    """

    email: EmailStr
    name_telegram: str


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
    is_active: активен ли пользователь
    is_superuser: является ли пользователь суперпользователем
    is_admin: является ли пользователь админом
    """

    id: int
    id_telegram: int
    created_at: datetime
    is_active: bool
    is_superuser: bool
    is_admin: bool

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


ex = {
    "id": 1,
    "id_telegram": 1,
    "email": "a@a.ru",
    "name_telegram": "a",
    "hashed_password": "a",
    "created_at": datetime.now(),
    "is_active": True,
    "is_superuser": False,
    "is_admin": False,
}
