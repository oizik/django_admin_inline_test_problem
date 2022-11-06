import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth import signals as auth_signals
from django.urls import reverse

User = get_user_model()


# @pytest.fixture(autouse=True)
# def disconnect_record_user_login_in_database_signal(request):
#     """Fixture disables the :func:`users.signals.record_user_login` signal
#     """

#     from users.signals import record_user_login

#     auth_signals.user_logged_in.disconnect(
#         record_user_login, dispatch_uid="record_user_login_in_database"
#     )


class TestUserAdmin:
    def test_add(self, admin_client):
        url = reverse("admin:users_user_add")
        response = admin_client.get(url)
        assert response.status_code == 200

        response = admin_client.post(
            url,
            data={
                "username": "test",
                "password1": "My_R@ndom-P@ssw0rd",
                "password2": "My_R@ndom-P@ssw0rd",
            },
        )
        # below FAILS when UserAdmin includes inlines = [LoginInline]
        assert User.objects.filter(username="test").exists()
        assert response.status_code == 302
