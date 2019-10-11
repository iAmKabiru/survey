from django.contrib import admin
from .models import Questionnaire, Question, Choice


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'text')


admin.site.register(Questionnaire)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)