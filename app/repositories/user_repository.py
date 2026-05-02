from app.models import User, db
from app.exceptions.user_exceptions import DuplicateUserException
from sqlalchemy.exc import IntegrityError


class UserRepository:
    def get_all(self):
        users = User.query.all()
        return users

    def get_by_id(self, id):
        user = User.query.get(id)
        if not user:
            return None
        return user

    def save(self, user):
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise DuplicateUserException("username or email")

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
