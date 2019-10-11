from django.contrib import admin
from .models import Questionnaire, Question, Choice


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'text')

class QuestionnaireAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author')


admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)