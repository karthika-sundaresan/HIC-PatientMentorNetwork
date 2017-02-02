from django.db import models

class Mentee(models.Model):

    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
    )
    city = models.CharField(max_length = 15)
    state = models.CharField(max_length = 15)
    zip = models.IntegerField()
    diagnosis = models.TextField()
    name = models.CharField(max_length = 30)

    def __str__(self):
       return self.name
	


    