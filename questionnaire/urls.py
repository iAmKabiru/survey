from django.urls import path
from . import views


urlpatterns = [
    path('new-questionnaire', views.add_questionnaire, name='create_questionnaire'),
	#path('new-questionnaire', views.CreateQuestionnaire.as_view(), name='create_questionnaire'),
    path('', views.questionnaire_list, name='questionnaire_list'),
	#path('questionnaire-list', views.QuestionnaireList.as_view(), name = 'questionnaire_list'),
	path('update-questionnaire/<int:pk>/', views.UpdateQuestionnaire.as_view(), name='update_questionnaire'),
	path('questionnaire-detail/<int:pk>/', views.QuestionnaireDetail.as_view(), name='questionnaire_detail'),
	path('delete-questionnaire/<int:pk>/', views.DeleteQuestionnaire.as_view(), name = 'delete_questionnaire'),

	# QUESTIONS URLS GOES HERE
    #path('question-list', views.QuestionList.as_view(), name = 'question_list'),
    path('questionnaire/<int:pk>/question/', views.add_question, name='add_question'),
    path('questionnaire/<int:pk>/question-delete/', views.question_delete, name='question_delete'),
    path('question-detail/<int:pk>/', views.QuestionDetail.as_view(), name = 'question_detail'),
    path('question-update/<int:pk>/', views.QuestionUpdate.as_view(), name = 'question_update'),

    # CHOICE URLS
    path('question/<int:pk>/choice/', views.add_choice, name='add_choice'),
    path('question/<int:pk>/delete_choice/', views.choice_delete, name='choice_delete'),

    # vote veiws for surveys
    path('survey/<int:pk>/', views.Survey.as_view(), name='survey'),
    path('survey-question/<int:pk>/', views.SurveyItem.as_view(), name='survey_item'),
    path('<int:question_id>/answer-question/', views.vote, name='vote'),
    path('thank-you', views.ThankYouView.as_view(), name="thank_you"),
    #path('result/<int:pk>/', views.result, name='result'),
    path('result/<int:pk>/', views.Result.as_view(), name='result'),

    # user views
    path('profile', views.profile, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]