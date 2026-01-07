from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz ,related_name='question', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title 
    
class Answer(models.Model):
    Question = models.ForeignKey(Question,related_name='answers',on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
