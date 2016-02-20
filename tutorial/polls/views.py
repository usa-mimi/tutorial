from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Question
from .models import Choice


def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })


def detail(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/detail.html', {
        'question': obj,
    })


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', pk)


def results(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    return render(request, 'polls/results.html', {
        'question': obj,
    })
