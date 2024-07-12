from django.db import models

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    appointment_date = models.DateTimeField()

    def __str__(self):
        return self.name