import requests
import json

# Replace this URL with the actual URL where your FastAPI app is running
BASE_URL = "http://127.0.0.1:8000"

def test_create_videogames():
    videogame_data = [{"name": "Test Game 1", "platform": "Test Platform 1", "genre": "Test Genre 1"}]
    response = requests.post(f"{BASE_URL}/videogames/", json=videogame_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_videogames():
    response = requests.get(f"{BASE_URL}/videogames/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_videogame():
    response = requests.get(f"{BASE_URL}/videogames/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_update_videogame():
    videogame_data = {"name": "Updated Game", "platform": "Updated Platform", "genre": "Updated Genre"}
    response = requests.put(f"{BASE_URL}/videogames/1", json=videogame_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == "Updated Game"

def test_delete_videogame():
    response = requests.delete(f"{BASE_URL}/videogames/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_create_genres():
    genre_data = [{"name": "Test Genre 1"}]
    response = requests.post(f"{BASE_URL}/genres/", json=genre_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_genres():
    response = requests.get(f"{BASE_URL}/genres/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_genre():
    response = requests.get(f"{BASE_URL}/genres/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_update_genre():
    genre_data = {"name": "Updated Genre"}
    response = requests.put(f"{BASE_URL}/genres/1", json=genre_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == "Updated Genre"

def test_delete_genre():
    response = requests.delete(f"{BASE_URL}/genres/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_create_ontwikkelaars():
    ontwikkelaar_data = [{"name": "Test Ontwikkelaar 1"}]
    response = requests.post(f"{BASE_URL}/ontwikkelaars/", json=ontwikkelaar_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_ontwikkelaars():
    response = requests.get(f"{BASE_URL}/ontwikkelaars/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_ontwikkelaar():
    response = requests.get(f"{BASE_URL}/ontwikkelaars/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_update_ontwikkelaar():
    ontwikkelaar_data = {"name": "Updated Ontwikkelaar"}
    response = requests.put(f"{BASE_URL}/ontwikkelaars/1", json=ontwikkelaar_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == "Updated Ontwikkelaar"

def test_delete_ontwikkelaar():
    response = requests.delete(f"{BASE_URL}/ontwikkelaars/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Tests for platformen endpoints
def test_create_platformen():
    platform_data = [{"name": "Test Platform 1"}]
    response = requests.post(f"{BASE_URL}/platformen/", json=platform_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_platformen():
    response = requests.get(f"{BASE_URL}/platformen/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_platform():
    response = requests.get(f"{BASE_URL}/platformen/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_update_platform():
    platform_data = {"name": "Updated Platform"}
    response = requests.put(f"{BASE_URL}/platformen/1", json=platform_data)
    
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["name"] == "Updated Platform"

def test_delete_platform():
    response = requests.delete(f"{BASE_URL}/platformen/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
