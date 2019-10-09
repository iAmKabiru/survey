from django.db import models
from django.urls import reverse

class Questionnaire(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	introduction = models.TextField()

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		return reverse('questionnaire_detail', kwargs={'pk': self.pk}) 

class Question(models.Model):
	text = models.CharField(max_length = 255)
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questions')

	def __str__(self):
		return self.text

class Choice(models.Model):
	text = models.CharField(max_length = 255)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
	vote = models.IntegerField(default = 0)

	def __str__(self):
		return self.text