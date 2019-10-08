from django.shortcuts import render
from django.urls import success_url
from django.views.generic import DetailView, ListView, 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Questionnaire, Question, Choice

class QuestionnaireList(ListView):
	model = Questionnaire
	template_name = 'questionnaire/questionnaire_list.html'

class CreateQuestionnaire(CreateView):
	model = Questionnaire
	fields = ['introduction']
	template_name = 'questionnaire/questionnaire_form.html'
	success_url = 'questionnaire_detail'

class UpdateQuestionnaire(UpdateView):
	model = Questionnaire
	fields = ['introduction']
	template_name = 'questionnaire/questionnaire_form.html'
	success_url = 'questionnaire_detail'


class QuestionnaireDetail(DetailView):
	model = Questionnaire 
	template_name = 'questionnaire/questionnaire_detail.html'

class DeleteQuestionnaire(DeleteView):
	model = Questionnaire
	template_name  = 'questionnaire/questionnaire_confirm_delete.html'
	success_url = 'questionnaire_list'
