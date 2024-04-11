from fastapi import APIRouter, Depends, status
from typing import List
from src.schemas.schemas import Author, AuthorBase, Book, BookBase, HTTPError
from src.core.main import DatabaseManager
from src.api.dependencies import get_database
from src.utils.utils import check_uuid

router = APIRouter()


@router.post(
    "/authors",
    status_code=status.HTTP_201_CREATED,
    summary="Add new author",
    tags=["authors"],
    responses={
        status.HTTP_201_CREATED: {"model": Author},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def create_author(
    request: AuthorBase,
    db: DatabaseManager = Depends(get_database)
) -> Author:
    return db.add_author(Author(**request.dict()))


@router.get(
    "/authors",
    status_code=status.HTTP_200_OK,
    summary="Get list of available authors",
    tags=["authors"],
    responses={
        status.HTTP_200_OK: {"model": List[Author]},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def get_authors(
    db: DatabaseManager = Depends(get_database)
) -> List[Author]:
    return db.get_all_authors()


@router.get(
    "/authors/{author_id}",
    status_code=status.HTTP_200_OK,
    summary="Get info about author by id",
    tags=["authors"],
    responses={
        status.HTTP_200_OK: {"model": Author},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def get_author(author_id: str, db: DatabaseManager = Depends(get_database)) -> Author:
    check_uuid(author_id)
    return db.get_author_by_id(author_id)


@router.get(
    "/authors/{author_id}/books",
    status_code=status.HTTP_200_OK,
    summary="Get list of books written by author",
    tags=["books"],
    responses={
        status.HTTP_200_OK: {"model": List[Book]},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def get_books(
    author_id: str,
    db: DatabaseManager = Depends(get_database)
) -> List[Book]:
    check_uuid(author_id)
    return db.get_all_books(author_id)


@router.post(
    "/authors/{author_id}/books",
    status_code=status.HTTP_201_CREATED,
    tags=["books"],
    summary="Add new book for author",
    responses={
        status.HTTP_201_CREATED: {"model": Book},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def create_book(
    author_id: str,
    request: BookBase,
    db: DatabaseManager = Depends(get_database)
) -> Book:
    check_uuid(author_id)
    return db.add_book(Book(author_id=author_id, **request.dict()))


@router.get(
    "/authors/{author_id}/books/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Get book by id written by author",
    tags=["books"],
    responses={
        status.HTTP_200_OK: {"model": Book},
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def get_book(
    author_id: str,
    book_id: str,
    db: DatabaseManager = Depends(get_database)
) -> Book:
    check_uuid(author_id)
    check_uuid(book_id)
    return db.get_book_by_id(author_id, book_id)


@router.delete(
    "/authors",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete all authors",
    tags=["authors"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def delete_authors(
    db: DatabaseManager = Depends(get_database)
):
    db.delete_all_authors()


@router.delete(
    "/authors/{author_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete author by id",
    tags=["authors"],
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def delete_author(
    author_id: str,
    db: DatabaseManager = Depends(get_database)
):
    check_uuid(author_id)
    db.delete_author_by_id(author_id)


@router.delete(
    "/authors/{author_id}/books",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete all books for author",
    tags=["books"],
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def delete_books(
    author_id: str,
    db: DatabaseManager = Depends(get_database)
):
    check_uuid(author_id)
    db.delete_all_books(author_id)


@router.delete(
    "/authors/{author_id}/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete book by id for author",
    tags=["books"],
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": HTTPError},
        status.HTTP_404_NOT_FOUND: {"model": HTTPError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HTTPError},
    },
)
async def delete_book(
    author_id: str,
    book_id: str,
    db: DatabaseManager = Depends(get_database)
):
    check_uuid(author_id)
    check_uuid(book_id)
    db.delete_book_by_id(author_id, book_id)
