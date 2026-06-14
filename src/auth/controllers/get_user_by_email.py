from sqlalchemy.orm import Session

from src.models.user_model import User


def get_user_by_email(
    db: Session,
    email: str
):
    try:
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    except Exception:
        return None