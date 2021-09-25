from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from django.urls import reverse
from .models import Question, Embti, Choice, Result

# Create your views here.

def index(request):
    embtis = Embti.objects.all()
    
    context = {
        'embtis' : embtis,
    }
    
    return render(request, 'index.html', context=context)

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form.html', context=context)


def result(request):
    print(f'POST : {request.POST}')
    
    sum = 0
    for i in range(10):
        j = i+1
        sum += request.POST[0]['question-'+j]
        
    if sum == 10:
        return render(request, 'result.html')
    elif 8 <= sum and sum >= 9:
        return render(request, 'result1.html')
    elif 5 <= sum and sum >= 7:
        return render(request, 'result2.html')
    elif 3 <= sum and sum >= 4:
        return render(request, 'result3.html')
    else:
        return render(request, 'result4.html')
    
    # if request.method == 'POST':
    #     post = Result()


def loading(request):
    return render(request, 'loading_page.html')

