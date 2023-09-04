from sqlalchemy import BigInteger, Column, String, Text

from app.core.db import Base


class Book(Base):
    """Models books."""

    title = Column(String(30), index=True)
    image = Column(Text)
    description = Column(Text)
    author = Column(String(64))
    date_publication = Column(BigInteger)
    url_download = Column(String(255), unique=True)
