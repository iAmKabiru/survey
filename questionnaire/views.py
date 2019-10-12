from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Questionnaire, Question, Choice
from .forms import QuestionForm, ChoiceForm, QuestionnaireForm
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def questionnaire_list(request):
    questionnaires = Questionnaire.objects.filter(author=request.user)
    template = loader.get_template('questionnaire/questionnaire_list.html') 
    context = { 'questionnaires': questionnaires, } 
    return HttpResponse(template.render(context, request)) 



"""
class QuestionnaireList(ListView):
	model = Questionnaire
	template_name = 'questionnaire/questionnaire_list.html'

    def get_queryset(self):
        return Questionnaire.objects.filter(author=request.user)





    def get_queryset(self):
        return Questionnaire.objects.filter(author=request.user)


class CreateQuestionnaire(CreateView):
	model = Questionnaire
	fields = ['title', 'introduction']
	template_name = 'questionnaire/questionnaire_form.html'
"""
@login_required
def add_questionnaire(request):
    if request.method == "POST":
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save(commit=False)
            questionnaire.author = request.user
            form.post_questionnaire()
            questionnaire.save()
        return redirect('questionnaire_list')
    else:
        form = QuestionnaireForm()
    return render(request, 'questionnaire/questionnaire_form.html', {'form': form})



class UpdateQuestionnaire(LoginRequiredMixin, UpdateView):
	model = Questionnaire
	fields = ['title', 'introduction']
	template_name = 'questionnaire/questionnaire_form.html'

class QuestionnaireDetail(LoginRequiredMixin, DetailView):
	model = Questionnaire 
	template_name = 'questionnaire/questionnaire_detail.html'

class DeleteQuestionnaire(LoginRequiredMixin, DeleteView):
	model = Questionnaire
	template_name  = 'questionnaire/questionnaire_confirm_delete.html'
	success_url = reverse_lazy('questionnaire_list')


@login_required
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



class QuestionDetail(LoginRequiredMixin, DetailView):
	model = Question
	template_name = 'question/question_detail.html'



class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question/question_form.html'

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
@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('questionnaire_detail', pk=question.questionnaire.pk)



@login_required
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

@login_required
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

######################### SURVEY FORMS ################

class Survey(DetailView):
    model = Questionnaire 
    template_name = 'vote/survey.html'



class SurveyItem(DetailView):
    model = Question
    template_name = 'vote/vote.html'





def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'vote/vote.html',
        {
            'question':question,
            'error_message': "you didnt select a choice"
        })
    else:
        selected_choice.vote +=1
        selected_choice.save()
        questionnaire = selected_choice.question.questionnaire
        question_list = Question.objects.filter(questionnaire_id = questionnaire.id)
        question_ids = []
        for qi in question_list:
            question_ids.append(qi.id)

        try:
            next = question_ids[question_ids.index(question.id)+1]
            return HttpResponseRedirect(reverse('survey_item', args=(next,)))
        except IndexError:
            return HttpResponseRedirect(reverse('thank_you'))




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

@login_required
def result(request, pk):
    item = {}
    questions = {}
    #questionnaire = Questionnaire.objects.get(id=4)
    questionnaire = get_object_or_404(Questionnaire, pk=pk)
    q_list = {}
    q_list = Question.objects.filter(questionnaire_id=questionnaire.id)
    for question in q_list:
        for choice in Choice.objects.filter(question_id=question.id):
            item['option'] = choice.text
            item['quantity'] = choice.vote
        questions['text'] = question.text
        questions['items'] = item
    context = {
    'title': questionnaire.title,
    'questions': questions
    }
    return render(request, 'vote/result.html', context=context)







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
