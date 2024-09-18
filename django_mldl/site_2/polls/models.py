from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model): # 설문조사 주제 테이블
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    
    was_published_recently.boolean = True
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.short_description = 'Published Recently?'
    
    list_filter = ['pub_date']
    search_fields = ['question_text']

class Choice(models.Model): # 설문조사 선택지 테이블
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #자동으로 Question 테이블의 PK 참조
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text