from django.db import models
from django.urls import reverse

class Questionnaire(models.Model):
	introduction = models.TextField()

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('questionnaire_detail', kwargs={'pk': self.pk}) 

class Question(models.Model):
	text = models.CharField(max_length = 255)
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

class Choice(models.Model):
	text = models.CharField(max_length = 255)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return self.text