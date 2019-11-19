from django.contrib import admin
from .models import Question, Choice
# Register your models here.


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']


class AdminChoice(admin.ModelAdmin):
    pass


admin.site.register(Question, AdminQuestion)

admin.site.register(Choice,AdminChoice)