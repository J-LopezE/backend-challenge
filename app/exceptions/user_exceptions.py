

class UserNotFoundException(Exception):
    def __init__(self, user_id):
        super().__init__(f"User not found: {user_id}")
        
class DuplicateUserException (Exception):
    def __init__(self,field):
        super().__init__(f"{field} already exists")