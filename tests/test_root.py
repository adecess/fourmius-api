from app import main


def test_root(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/")

    # Then
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Fourmius.io!", "environment": "dev", "testing": True}
