import django
django.setup()

from django.contrib.auth.models import User

u = User(username='nirmal')
u.set_password('12345')
u.is_superuser = True
u.is_staff = True
u.save()