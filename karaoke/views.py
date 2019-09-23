from django.shortcuts import render
# lógica de negócio

def index(request):
    context = {
        'nomes': [
            'eric',
            'aline',
            'juliana'
        ],
        'vazio': False,
        'teste': 'teste'}
    return render(request, 'index.html', context)
