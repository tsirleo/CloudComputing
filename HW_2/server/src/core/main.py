from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException, status
from src.core.orm import AuthorDB, BookDB
from src.schemas.schemas import Author, Book


class DatabaseManager:
    def __init__(self, engine):
        self.engine = engine

    def add_author(self, author_data: Author):
        with Session(self.engine) as session:
            session: Session
            try:
                new_author = AuthorDB(**author_data.dict())
                session.add(new_author)
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()
                return author_data

    def get_all_authors(self):
        with Session(self.engine) as session:
            session: Session
            try:
                authors = session.query(AuthorDB).all()
            except Exception:
                session.rollback()
                raise
            else:
                return authors

    def get_author_by_id(self, author_id):
        with Session(self.engine) as session:
            session: Session
            try:
                author = session.query(AuthorDB).filter_by(author_id=author_id).one()
            except NoResultFound:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"author with id '{author_id}' not found"
                )
            except Exception:
                session.rollback()
                raise
            else:
                return author

    def get_all_books(self, author_id):
        with Session(self.engine) as session:
            session: Session
            try:
                books = session.query(BookDB).filter_by(author_id=author_id).all()
            except Exception:
                session.rollback()
                raise
            else:
                return books

    def add_book(self, book_data: Book):
        with Session(self.engine) as session:
            session: Session
            try:
                new_book = BookDB(**book_data.dict())
                session.add(new_book)
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()
                return book_data

    def get_book_by_id(self, author_id, book_id):
        with Session(self.engine) as session:
            session: Session
            try:
                try:
                    session.query(AuthorDB).filter_by(author_id=author_id).one()
                except NoResultFound:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"author with id '{author_id}' not found"
                    )

                book = session.query(BookDB).filter_by(author_id=author_id, book_id=book_id).one()
            except NoResultFound:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"book with id '{author_id}' not found for author_id '{author_id}'"
                )
            except Exception:
                session.rollback()
                raise
            else:
                return book

    def delete_all_authors(self):
        with Session(self.engine) as session:
            session: Session
            try:
                session.query(AuthorDB).delete()
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()

    def delete_author_by_id(self, author_id):
        with Session(self.engine) as session:
            session: Session
            try:
                author = session.query(AuthorDB).filter_by(author_id=author_id).one()
                session.delete(author)
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()

    def delete_all_books(self, author_id):
        with Session(self.engine) as session:
            session: Session
            try:
                session.query(BookDB).filter_by(author_id=author_id).delete()
            except NoResultFound:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"author with id '{author_id}' not found"
                )
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()

    def delete_book_by_id(self, author_id, book_id):
        with Session(self.engine) as session:
            session: Session
            try:
                try:
                    session.query(AuthorDB).filter_by(author_id=author_id).one()
                except NoResultFound:
                    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"author with id '{author_id}' not found"
                    )
                book = session.query(BookDB).filter_by(author_id=author_id, book_id=book_id).one()
                session.delete(book)
            except NoResultFound:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"book with id '{author_id}' not found for author_id '{author_id}'"
                )
            except Exception:
                session.rollback()
                raise
            else:
                session.commit()
