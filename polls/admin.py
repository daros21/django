from django.contrib import admin

from books.models import Notification
from .models import Question, Choice
# Register your models here.

class ChoiceInLine(admin.StackedInline):
    model = Choice
    fields = ['choice_text']
    suit_classes = 'suit-tab suit-tab-questions'


class AdminQuestion(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'is_active']
    search_fields = ['question_text']
    list_filter = ['is_active']

    fieldsets = [
        ('Glowne', {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ['question_text', 'is_active']}),
        ("daty", {
            'classes': ('suit-tab', 'suit-tab-dates'),
            'fields': ['pub_date', 'created', 'modified']}),
        ("image", {
            'classes': ('suit-tab', 'suit-tab-images'),
            'fields': ['image']}),
        ("poziom trudnosci", {
            'classes': ('suit-tab', 'suit-tab-other'),
            'fields': ['level']})
    ]

    suit_form_tabs = (('general', 'General'), ('dates', 'Dates'),
                      ('images', 'Images'), ('other', 'Other'), ('questions', 'Questions'))
    inlines = [ChoiceInLine]
    readonly_fields = ['id', 'created', 'modified']

class AdminChoice(admin.ModelAdmin):
    pass


admin.site.register(Question, AdminQuestion)

admin.site.register(Choice,AdminChoice)

admin.site.register(Notification)
