import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Now import models
from myapp.models import Student

# Insert data
# s1 = Student(roll=13, name="maroof", marks=100)
# s1.save()
# print("Data Inserted!")

records = Student.objects.filter(roll = 13)

for data in records:
    print(data)