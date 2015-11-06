from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Question


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
    pass
