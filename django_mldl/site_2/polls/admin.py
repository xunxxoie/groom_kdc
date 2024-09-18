from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Title', {'fields':['question_text']}),
        ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})
        
    ]
    
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)