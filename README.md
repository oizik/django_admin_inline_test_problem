# Django Admin Inline Form Test Problem

This little project exhibits a problem with Django Admin Inline Form Saving in Test Cases.

Quickly create superuser:

```bash
DJANGO_SUPERUSER_PASSWORD=password  bash -c 'poetry run python manage.py createsuperuser --noinput --username admin --email="admin@example.com"'
```
