from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Questionnaire, Question, Choice
from .forms import QuestionForm, ChoiceForm

class QuestionnaireList(ListView):
	model = Questionnaire
	template_name = 'questionnaire/questionnaire_list.html'

class CreateQuestionnaire(CreateView):
	model = Questionnaire
	fields = ['title', 'introduction']
	template_name = 'questionnaire/questionnaire_form.html'

class UpdateQuestionnaire(UpdateView):
	model = Questionnaire
	fields = ['title', 'introduction']
	template_name = 'questionnaire/questionnaire_form.html'

class QuestionnaireDetail(DetailView):
	model = Questionnaire 
	template_name = 'questionnaire/questionnaire_detail.html'

class DeleteQuestionnaire(DeleteView):
	model = Questionnaire
	template_name  = 'questionnaire/questionnaire_confirm_delete.html'
	success_url = '/questionnaire-list'



def add_question(request, pk):
    questionnaire = get_object_or_404(Questionnaire, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.questionnaire = questionnaire
            form.post_question()
            question.save()
        return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'question/question_form.html', {'form': form})



class QuestionDetail(DeleteView):
	model = Question
	template_name = 'question/question_detail.html'


"""
def update_question(request, pk):
    questionnaire = get_object_or_404(Questionnaire, pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.questionnaire = questionnaire
            question.save()
            return redirect('questionnaire_detail', pk=questionnaire.pk)
    else:
        form = QuestionForm()
    return render(request, 'question/question_form.html', {'form': form})


class QuestionList(ListView):
    model = Question
"""

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('questionnaire_detail', pk=question.questionnaire.pk)




def add_choice(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            form.post_choice()
            choice.save()
        return redirect('question_detail', pk=question.pk)
    else:
        form = ChoiceForm()
    return render(request, 'choice/choice_form.html', {'form': form})



"""
def update_choice(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = ChoiceForm()
    return render(request, 'choice/choice_form.html', {'form': form})


class ChoiceList(ListView):
    model = Choice
"""


def choice_delete(request, pk):
    choice = get_object_or_404(Choice, pk=pk)
    choice.delete()
    return redirect('question_detail', pk=choice.question.pk)







"""
class QuestionCreate(CreateView):
	model = Question
	fields  = ['text', 'questionnaire']
	template_name = 'question/question_form.html'

class QuestionList(ListView):
	model = Question
	template_name = 'question/question_list.html'
"""



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'question/question_detail.html',
        {
            'question':question,
            'error_message': "you didnt select a question"
        })
    else:
        selected_choice.vote +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('question_detail', args=(question.id + 1,)))


"""

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
        {
            'question':question,
            'error_message': "you didnt select a question"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

"""

class ThankYouView(TemplateView):
    template_name = 'vote/thank_you.html'




############################
############################
##### ACCOUNT VIEWS ########
############################
############################


"""
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
"""

def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
