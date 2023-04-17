from sqlalchemy import Column, Index, Integer, String, TIMESTAMP, text, UniqueConstraint
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from orm_base import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class User(Base):
    __tablename__ = "user"


    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(55))
    email: Mapped[Optional[str]] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    
    
    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, name={self.name!r}, email={self.email!r},  password={self.hashed_password!r})"

#Might refactor, of no use. 
class UserAction(Base):
    __tablename__ = "UserAction"
    src_address = Column(String(50), index=True)


    user_action_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column()
    video_id: Mapped[int] = mapped_column()
    date: Mapped[Optional[str]] = mapped_column(String(255), unique=True)
    
    def __repr__(self) -> str:
        return f"User Action(user_id={self.user_id!r}, user_action_id={self.user_action_id!r}, video_id={self.video_id!r},  date={self.date!r})"
