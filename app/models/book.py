from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.core.db import Base


class Book(Base):
    """Models books."""

    title = Column(String(128), index=True)
    image = Column(Text)
    description = Column(Text)
    author = Column(String(128))
    genre = Column(String(128))
    link_download = Column(String(255), unique=True)
    user_id = Column(Integer, ForeignKey("user.id"))
