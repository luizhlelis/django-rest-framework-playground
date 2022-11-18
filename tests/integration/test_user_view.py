from datetime import date

import pytest

class TestUserAPIView:
    def test_get_users_should_return_200(self, client):
        # Arrange
        fake_data = {}
        header = {
            "HTTP_AUTHORIZATION": "Bearer fake-token",
        }
        # Act
        response = client.get("/users", content_type="application/json", data=fake_data, auth=("admin", "admin123"))
        # Assert
        assert response.status_code == 200
        result = response.json()
        assert result == {
            "count": 1,
            "next": "null",
            "previous": "null",
            "results": [
                {
                    "url": "http://127.0.0.1:8000/users/1/",
                    "username": "admin",
                    "email": "admin@example.com",
                    "groups": []
                }
            ]
        }