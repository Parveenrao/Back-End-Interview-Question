""" 

=> Bulk update

   -> update many records


@router.patch("/users/bulk")
def bulk_update(
    users: list[UserUpdate],
    db: Session
):

    for user in users:

        db.query(User).filter(
            User.id == user.id
        ).update({
            "name": user.name
        })

    db.commit()

    return {"updated": len(users)}   



"""