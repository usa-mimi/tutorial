from django.shortcuts import render
from django.shortcuts import Http404

from .models import Question


def index(request):
    return render(request, 'polls/index.html', {
        'questions': Question.objects.all(),
    })


def detail(request, pk):
    try:
        obj = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {
        'question': obj,
    })
