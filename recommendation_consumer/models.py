from sqlalchemy import Column, Index, Integer, String, TIMESTAMP, text, UniqueConstraint, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from orm_base import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserAction(Base):
    __tablename__ = "UserAction"

    user_action_id: Mapped[int] = mapped_column(primary_key=True)
    action: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column()
    category_id: Mapped[int] = mapped_column()
    video_id: Mapped[int] = mapped_column()
    
    def __repr__(self) -> str:
        return f"User Action(user_id={self.user_id!r}, user_action_id={self.user_action_id!r}, video_id={self.video_id!r})"
