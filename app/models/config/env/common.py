from pydantic import SecretStr

from .base import EnvSettings


class CommonConfig(EnvSettings, env_prefix="COMMON_"):
    admin_chat_id: int
    users_cache_time: int = 30
    coinmarketcap_key: SecretStr = SecretStr("")
    tonconsole_key: SecretStr = SecretStr("")
