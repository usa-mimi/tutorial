from django.contrib import admin

from .models import Question
from .models import Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
