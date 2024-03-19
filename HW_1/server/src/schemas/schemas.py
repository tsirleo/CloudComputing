from typing import Optional
from pydantic import BaseModel, Field, root_validator
from datetime import date
from uuid import UUID, uuid4


class AuthorBase(BaseModel):
    firstname: str
    lastname: str
    birthplace: Optional[str]
    birthdate: Optional[date]

    class Config:
        orm_mode = True


class Author(AuthorBase):
    author_id: UUID = Field(default_factory=uuid4)


class BookBase(BaseModel):
    title: str
    publishing_house: Optional[str]
    publication_date: Optional[date]

    class Config:
        orm_mode = True


class Book(BookBase):
    author_id: str = Field(...)
    book_id: UUID = Field(default_factory=uuid4)

    @root_validator(pre=True)
    def check_author_id(cls, values):
        if 'author_id' not in values:
            raise ValueError('author_id is required')
        return values


class HTTPError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
