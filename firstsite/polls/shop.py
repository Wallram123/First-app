from django.shortcuts import render

def view(request):
    context = {
        'title': 'JAO',
        'message': 'AAAAAAAAAAAAAAAAAAAAAAAAAAA!',
    }
    return render(request, 'polls/view.html', context)  
