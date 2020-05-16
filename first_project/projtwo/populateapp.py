import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','projtwo.settings')

import django
django.setup()
from secondapp.models import Users
from faker import Faker


fakegen = Faker()

def pop(N=5):
    for entry in range(N):
        fake_firstn = fakegen.first_name()
        fake_firstl = fakegen.last_name()
        fake_url = fakegen.url()

        objg = Users.objects.get_or_create(userfirst = fake_firstn,userlast = fake_firstl,userEmail = fake_url)[0]

if __name__ == '__main__':
    pop()
