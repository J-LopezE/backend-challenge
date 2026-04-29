import pytest
from app.exceptions.user_exceptions import UserNotFoundException
from app.services.user_service import UserService
from app.models import User

def test_get_all_returns_users(mocker):
    mock_repo = mocker.patch("app.services.user_service.UserRepository")
    mock_repo.return_value.get_all.return_value = [
        User(id=1, email="test@mail.com", username="test")
    ]
    
    service = UserService()
    result= service.get_all()
    
    assert len(result) ==1
    assert result[0].email == "test@mail.com"

def test_create_user_success(mocker):
    mock_repo = mocker.patch("app.services.user_service.UserRepository")
    service = UserService()
    service.create("new@mail.com", "newuser")  
    mock_repo.return_value.save.assert_called_once()
    

def test_get_by_id_raises_not_found(mocker):
    mock_repo = mocker.patch("app.services.user_service.UserRepository")
    mock_repo.return_value.get_by_id.return_value = None
    
    service = UserService()
    with pytest.raises(UserNotFoundException):
        service.get_by_id(999)