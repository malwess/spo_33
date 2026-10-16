# Собственные модели в приложении accounts не нужны:
# для пользователей используется встроенная модель Django
# django.contrib.auth.models.User
from django.contrib.auth.models import User

__all__ = ["User"]
