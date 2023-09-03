from sqlalchemy import Column, String, Text, Integer, BigInteger

from app.core.db import Base


class Book(Base):
    """Models books."""

    title = Column(String(30), index=True)
    image = Column(Text)
    description = Column(Text)
    author = Column(String(64))
    date_publication = Column(BigInteger)
    price = Column(Integer)
