from django import forms 
from .models import Questionnaire, Question, Choice



class QuestionnaireForm(forms.ModelForm):

    class Meta:
        model = Questionnaire
        exclude = ('author',)

    def post_questionnaire(self):
       text = self.cleaned_data.get('title')
       text = self.cleaned_data.get('introduction')

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ('questionnaire',)

    def post_question(self):
       text = self.cleaned_data.get('text')
       


class ChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice
		exclude = ('question','vote',)

	def post_choice(self):
		text = self.cleaned_data.get('text')
