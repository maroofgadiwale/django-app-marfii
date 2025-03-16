from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80,default="maroof")
    marks = models.IntegerField(null=False)
    # Explicitly define the manager
    objects = models.Manager()

    # Display details:
    def __str__(self):
        return f"Roll: {self.roll}\nName: {self.name}\nMarks: {self.marks}"

