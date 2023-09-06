from sqlalchemy import BigInteger, Column, String, Text, Integer, ForeignKey

from app.core.db import Base


class Book(Base):
    """Models books."""

    title = Column(String(128), index=True)
    image = Column(Text)
    description = Column(Text)
    author = Column(String(128))
    genre = Column(String(128))
    date_publication = Column(BigInteger)
    url_download = Column(String(255), unique=True)
    user_id = Column(Integer, ForeignKey("user.id"))
