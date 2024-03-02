import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TensorCore.settings")
django.setup()

import random
from faker import Faker
from django.contrib.auth.models import User
from portfolio.models import Category, Project  # Replace 'myapp' with your actual app name
from django.utils.text import slugify
from datetime import datetime, timedelta




fake = Faker()

# Ensure Django is properly configured


# Create three categories
categories = ['Web Development', 'Mobile App Development', 'Data Science']

for category_name in categories:
    Category.objects.create(author=User.objects.first(), category=category_name)

# Create 20 projects for each category
for category in Category.objects.all():
    for _ in range(20):
        title = fake.word()
        abstract = fake.text()
        codelink = fake.url()
        publish_date = datetime.now() - timedelta(days=random.randint(1, 365))
        img_url = fake.image_url()
        fulltext = fake.url()

        Project.objects.create(
            category=category,
            title=title,
            abstract=abstract,
            codelink=codelink,
            publish_date=publish_date.date(),
            img=img_url,
            fulltext=fulltext
        )

print("Fake data has been generated.")
