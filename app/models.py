from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length = 200)
    option2 = models.CharField(max_length = 200)
    option3 = models.CharField(max_length = 200)
    option4 = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200) 


    def __str__(self):
        return self.question