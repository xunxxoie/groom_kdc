from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', ~~, ~~), # 127.0.0.1:8000/polls/new/

    # ex) 127.0.0.1:8000/polls/5/
    # 특정 투표 페이지 URL
    path('<int:question_id>/', views.detail, name='detail'),

    # ex) 127.0.0.1:8000/polls/5/vote/
    # 투표 이벤트 URL
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex) 127.0.0.1:8000/polls/5/results/
    # 투표 결과 페이지 URL
    path('<int:question_id>/results/', views.results, name='results'),
]