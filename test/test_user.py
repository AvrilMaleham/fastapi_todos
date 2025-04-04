from routers.user import get_db, get_current_user
from fastapi import status
from models import Todos
from .utils import *
        
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user    

def test_read_all_authenticated(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "avrilmaleham"
    assert response.json()["email"] == "avrilmaleham@email.com"
    assert response.json()["first_name"] == "Avril"
    assert response.json()["last_name"] == "Maleham"
    assert response.json()["role"] == "admin"
    assert response.json()["is_active"] == True
    
def test_change_password_success(test_user):
    request_data={
        "password": "password",
        "new_password": "new_password"
    }
    
    response = client.put("/user/password", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
def test_change_password_invalid_current_password(test_user):
    request_data={
        "password": "wrong_password",
        "new_password": "new_password"
    }
    
    response = client.put("/user/password", json=request_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}
