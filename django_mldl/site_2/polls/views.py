from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {'latest_question_list' : latest_question_list}
    
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question':q})

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice_select'])
    except:
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/result.html', {'question' : question})