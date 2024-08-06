from typing import Type

from fastapi_users import FastAPIUsers, schemas
from fastapi_users.authentication import (
    CookieTransport,
    RedisStrategy,
    AuthenticationBackend,
    Authenticator,
)
import redis

from src.auth.routers import get_verify_router
from src.auth.user_manager import get_user_manager
from src.config.config import settings
from src.repositories.models.user import UserOrm

cookie_transport = CookieTransport(cookie_max_age=3600)

redis = redis.asyncio.from_url(settings.DATABASE_URL_redis, decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    """Создание RedisStrategy"""
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)


class FastApiCustom(FastAPIUsers[UserOrm, int]):
    """Переопределение FastAPIUsers"""
    authenticator: Authenticator

    def __init__(self, value_1, value_2):
        super().__init__(get_user_manager=value_1, auth_backends=value_2)
        self.authenticator = Authenticator(
            backends=value_2, get_user_manager=get_user_manager
        )
        self.get_user_manager = get_user_manager
        self.current_user = self.authenticator.current_user

    def get_verify_router(self, user_schema: Type[schemas.U]):
        return get_verify_router(self.get_user_manager, user_schema)


fastapi_users = FastApiCustom(get_user_manager, [auth_backend])
