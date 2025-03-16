from typing import Optional

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.dto import UserDto
from app.utils.custom_types import Int64

from .base import Base
from .mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[Int64] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[Int64] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    wallet_address: Mapped[Optional[str]] = mapped_column(nullable=True)
    wallet_mnemonic: Mapped[Optional[list[str]]] = mapped_column(JSON, nullable=True)
    locale: Mapped[str] = mapped_column(String(length=2), nullable=False)
    bot_blocked: Mapped[bool] = mapped_column(default=False, nullable=False)

    def dto(self) -> UserDto:
        return UserDto.model_validate(self)
