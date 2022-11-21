from django.contrib.auth.models import User

import pytest

@pytest.mark.django_db
class TestUserAPIView:
    def test_get_users_should_return_200(self, client):
        # Arrange
        self.user = User.objects.create_superuser(
            username='foobar',
            email='foo@bar.com',
            password='barbaz')
        client.force_login(user=self.user)
        # Act
        response = client.get("/users", follow=True)
        # Assert
        assert response.status_code == 200
        result = response.json()
        assert result == {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "url": "http://testserver/users/1/",
                    "username": "foobar",
                    "email": "foo@bar.com",
                    "groups": []
                }
            ]
        }