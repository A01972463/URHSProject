import os
import django
from django.contrib.auth import get_user_model

// Todo: Take command arguments

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'URHSProject.settings')
django.setup()

User = get_user_model()

username = 'Gustavo'
email = 'GHuerta@admin.com'
password = 'Password'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created successfully')
else:
    print('Superuser already exists')
