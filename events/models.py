from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return self.title


class Registration(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name