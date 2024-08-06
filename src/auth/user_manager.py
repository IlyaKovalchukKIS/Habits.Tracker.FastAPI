from typing import Optional

from fastapi_users import IntegerIDMixin, BaseUserManager, models
from fastapi import Request, Depends

from src.config.config import settings
from src.repositories.crud.user import UserOrmCrud
from src.repositories.models.user import UserOrm
from src.utils import send_email


class UserManager(IntegerIDMixin, BaseUserManager[UserOrm, int]):
    reset_password_token_secret = settings.AUTH_VERIFY_KEY
    verification_token_secret = settings.AUTH_VERIFY_KEY

    async def on_after_register(self, user: UserOrm, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserOrm, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserOrm, token: str, request: Optional[Request] = None
    ):
        send_email(
            receiver_email=user.email,
            subject="Подтвердите почту",
            body=f"Перейдите по ссылке: {settings.APP_HOST}/auth/verify/{token}",
        )
        print(f"Verification requested for user {user.id}. Verification token: {token}")

    async def on_after_verify(
        self, user: models.UP, request: Optional[Request] = None
    ) -> None:
        print("________________________")
        print(f"User {user.id} has been verified")


async def get_user_manager(user_db=Depends(UserOrmCrud.get_user_db)):
    yield UserManager(user_db)
