from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)    

def test_read_main():

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Backend is running" 
    
def test_user_signup():
    response = client.post("/auth/signup", json={"email": "unittest@test.pl", "password": "12345678"})

    assert response.status_code == 200

def test_user_signin():
    response = client.post("/auth/signin", json={"email": "unittest@test.pl", "password": "12345678"})
    assert response.status_code == 200  