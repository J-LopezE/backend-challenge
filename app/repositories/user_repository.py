from app.models import User,db

class UserRepository:
    def get_all(self):
        users = User.query.all()
        return users
    def get_by_id(self,id):
        user= User.query.get(id)
        if not user:
           return None
        return user
    def save(self,user):
        db.session.add(user)
        db.session.commit()
        
    def delete(self,user):
        db.session.delete(user)
        db.session.commit()