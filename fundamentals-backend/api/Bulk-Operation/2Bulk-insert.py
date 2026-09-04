""" 

=> Bulk Insert

    -> Insert multiple records at once

=> 

from fastapi import APIRouter
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/users/bulk")
def bulk_create_users(
    users: list[UserCreate],
    db: Session
):
    db_users = [
        User(
            name=user.name,
            email=user.email
        )
        for user in users
    ]

    db.bulk_save_objects(db_users)

    db.commit()

    return {
        "inserted": len(db_users)
    }





"""