import pytest
from app import app  # Corrected import statement


# normally I would organize tests better but here we just have a quick application to demo


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_personal_endpoint(client):
    response = client.get('/personal')
    assert response.status_code == 200
    assert 'name' in response.json


def test_personal_endpoint_post_request(client):
    response = client.post('/personal')
    assert response.status_code == 405


def test_experience_endpoint(client):
    expected_companies = ['Annedora', 'Rolls-Royce', 'CAE', 'Thales']
    response = client.get('/experience')
    assert response.status_code == 200
    for company in expected_companies:
        assert company in response.json


def test_experience_endpoint_post_request(client):
    response = client.post('/experience')
    assert response.status_code == 405


def test_education_endpoint(client):
    response = client.get('/education')
    assert response.status_code == 200
    assert 'Concordia' in response.json


def test_education_endpoint_post_request(client):
    response = client.post('/education')
    assert response.status_code == 405
