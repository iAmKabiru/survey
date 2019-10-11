from django.db import models
from django.urls import reverse
from django.conf import settings



class Questionnaire(models.Model):
	title = models.CharField(max_length=1000, null=True, blank=True)
	introduction = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse('questionnaire_detail', kwargs={'pk': self.pk}) 

class Question(models.Model):
	text = models.CharField(max_length = 255)
	questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name="questions")

	def __str__(self):
		return self.text

class Choice(models.Model):
	text = models.CharField(max_length = 255)
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
	vote = models.IntegerField(default = 0)

	def __str__(self):
		return self.text


