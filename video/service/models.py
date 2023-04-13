from sqlalchemy import Column, Index, Integer, String, TIMESTAMP, text, UniqueConstraint, ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from orm_base import Base

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class Video(Base):
    __tablename__ = "video"

    video_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    title: Mapped[str]
    resume: Mapped[Optional[str]]
    category: Mapped[str] = mapped_column(ForeignKey("category.category"))
    #category_id: Mapped[int] = mapped_column(ForeignKey("category.category_id"))

    
    def __repr__(self) -> str:
       return f"Video (id={self.video_id!r}, user_id={self.user_id!r}, title={self.title!r},  category={self.category!r})"
    

class Category(Base):
    __tablename__ = "category"

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str]

    def __repr__(self) -> str:
        return f"Category (id={self.category_id!r}, category={self.category!r})"
