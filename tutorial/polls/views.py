from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html', {
        'hoge': 'test string',
        'fuga': '<br>tag</br>',
    })
