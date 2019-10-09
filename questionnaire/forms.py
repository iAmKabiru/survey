from django import forms 
from .models import Question, Choice


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        exclude = ('questionnaire',)

    def post_question(self):
       text = self.cleaned_data.get('text')
       


class ChoiceForm(forms.ModelForm):

	class Meta:
		model = Choice
		exclude = ('question',)

	def post_choice(self):
		text = self.cleaned_data.get('text')