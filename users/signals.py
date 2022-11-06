from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


@receiver(user_logged_in, dispatch_uid="record_user_login_in_database")
def record_user_login(sender, user, request, **kwargs):
    """Record user login"""
    from users.models import Login

    login = Login.objects.create(
        user=user,
        # add defaults so that we don't need to disable it during testing
        ip=request.META.get('REMOTE_ADDR', 'some_ip_address'),
        user_agent=request.META.get('HTTP_USER_AGENT', 'some_user_agent'),
        http_host=request.META.get('HTTP_HOST', None),
        remote_host=request.META.get('REMOTE_HOST', None),
        server_name=request.META.get('SERVER_NAME', None),
    )

    return login
