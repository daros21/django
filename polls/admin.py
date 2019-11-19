from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.StackedInline):
    model = Choice
    fields = ['choice_text']


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ('Glowne', {'fields': ['question_text', 'is_active']}),
        ("daty", {'fields': ['pub_date', 'created', 'modified']}),
        ("image", {'fields': ['image']}),
        ("poziom trudnosci", {'fields': ['level']})
    ]
    inlines = [ChoiceInLine]
    readonly_fields = ['id', 'created', 'modified']

class AdminChoice(admin.ModelAdmin):
    pass


admin.site.register(Question, AdminQuestion)

admin.site.register(Choice,AdminChoice)