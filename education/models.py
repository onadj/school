# education/models.py

from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.name

class Exercise(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="exercises")
    title = models.CharField(max_length=100)
    description = models.TextField()
    timer = models.IntegerField(default=0, help_text="Timer in seconds (0 for no timer)")
    image = models.ImageField(upload_to="exercises/", null=True, blank=True)
    video = models.FileField(upload_to="exercises/videos/", null=True, blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="questions")
    question_text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class StudentAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"Answer by {self.student.username} for {self.question}"
