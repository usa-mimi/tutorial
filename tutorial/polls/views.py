from django.shortcuts import render
from django.utils.html import mark_safe


def index(request):
    return render(request, 'polls/index.html', {
        'hoge': 'test string',
        'fuga': '<br>tag</br>',
        'piyo': mark_safe('<br>tag</br>'),
    })
