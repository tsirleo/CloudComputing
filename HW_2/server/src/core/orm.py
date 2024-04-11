from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class AuthorDB(Base):
    __tablename__ = 'authors'

    author_id = Column(String(36), primary_key=True, unique=True, nullable=False, default='UUID()')
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    birthplace = Column(String(255))
    birthdate = Column(Date)

    books = relationship("BookDB", back_populates="author", cascade="all, delete-orphan")


class BookDB(Base):
    __tablename__ = 'books'

    book_id = Column(String(36), primary_key=True, unique=True, nullable=False, default='UUID()')
    title = Column(String(255), nullable=False)
    publication_date = Column(Date)
    publishing_house = Column(String(255))
    author_id = Column(String(36), ForeignKey('authors.author_id'))

    author = relationship("AuthorDB", back_populates="books")