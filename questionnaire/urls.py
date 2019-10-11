from django.urls import path
from . import views


urlpatterns = [
	path('new-questionnaire', views.CreateQuestionnaire.as_view(), name='create_questionnaire'),
	path('questionnaire-list', views.QuestionnaireList.as_view(), name = 'questionnaire_list'),
	path('update-questionnaire/<int:pk>/', views.UpdateQuestionnaire.as_view(), name='update_questionnaire'),
	path('questionnaire-detail/<int:pk>/', views.QuestionnaireDetail.as_view(), name='questionnaire_detail'),
	path('delete-questionnaire/<int:pk>/', views.DeleteQuestionnaire.as_view(), name = 'delete_questionnaire'),

	# QUESTIONS URLS GOES HERE
    #path('question-list', views.QuestionList.as_view(), name = 'question_list'),
    path('questionnaire/<int:pk>/question/', views.add_question, name='add_question'),
    path('questionnaire/<int:pk>/question-delete/', views.question_delete, name='question_delete'),
    path('question-detail/<int:pk>/', views.QuestionDetail.as_view(), name = 'question_detail'),
   # path('questionnaire/<int:pk>/question-update/', views.update_question, name = 'question_update'),

    # CHOICE URLS
    path('question/<int:pk>/choice/', views.add_choice, name='add_choice'),
    path('question/<int:pk>/delete_choice/', views.choice_delete, name='choice_delete'),

    # vote veiws
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('thank-you', views.ThankYouView.as_view(), name="thank_you"),

    # user views
    path('profile', views.profile, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup')
]