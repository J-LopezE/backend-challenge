from app.repositories.user_repository import UserRepository
from app.models import User
from app.exceptions.user_exceptions import UserNotFoundException
class UserService:
    def __init__(self):
        self.__repository = UserRepository()
        
    def get_all(self):
        return self.__repository.get_all()
    
    def get_by_id(self,id):
        user = self.__repository.get_by_id(id)
        if not user:
            raise UserNotFoundException(id)
        return user
    def create(self,email, username):
        user = User(email=email, username=username)
        self.__repository.save(user)
        return user
        
    def update(self,id, email, username):
        user = self.__repository.get_by_id(id)
        if not user:
                raise UserNotFoundException(id)
        if email:
         user.email = email
        if username:
            user.username = username
        self.__repository.save(user)
        return user
    
    def delete(self,id):
         user = self.__repository.get_by_id(id)
         if not user:
             raise UserNotFoundException(id)
         self.__repository.delete(user)