from fastapi import HTTPException, status
from uuid import UUID


def check_uuid(uuid_str):
    try:
        UUID(uuid_str)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"uuid '{uuid_str}' is incorrect"
        )
