from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    CookieTransport,
    RedisStrategy,
    AuthenticationBackend,
)
import redis

from src.auth.user_manager import get_user_manager
from src.config.config import settings
from src.repositories.models.user import UserOrm

cookie_transport = CookieTransport(cookie_max_age=3600)

redis = redis.asyncio.from_url(settings.DATABASE_URL_redis, decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[UserOrm, int](
    get_user_manager,
    [auth_backend],
)
