"""

class DeleteUsers(BaseModel):
    ids: list[int]


@router.delete("/users/bulk")
def bulk_delete(
    request: DeleteUsers,
    db: Session
):

    db.query(User).filter(
        User.id.in_(request.ids)
    ).delete(
        synchronize_session=False
    )

    db.commit()

    return {
        "deleted": len(request.ids)
    }

"""    