from django.urls import path
from . import views


urlpatterns = [
	path('new-questionnaire', views.CreateQuestionnaire.as_view(), name='create_questionnaire'),
	path('questionnaire-list', views.QuestionnaireList.as_view(), name = 'questionnaire_list'),
	path('update-questionnaire', views.UpdateQuestionnaire.as_view(), name='update_questionnaire'),
	path('questionnaire-detail/<int:pk>/', views.QuestionnaireDetail.as_view(), name='questionnaire_detail'),
	path('delete-questionnaire/<int:pk>/', views.DeleteQuestionnaire.as_view(), name = 'delete_questionnaire')
]