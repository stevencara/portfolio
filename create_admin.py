# create_admin.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_portfolio.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "steven"
email = "stevencara2022@gmail.com"
password = "Operacioness3"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✅ Superusuario creado.")
else:
    print("⚠️ El superusuario ya existe.")
