from django.shortcuts import render
from django.http import HttpResponse, HttpResponse
from django.urls import reverse
from .models import Question, Embti, Choice, Result

# Create your views here.

count = 0
def index(request):
    global count # 바깥영역의 변수를 사용할 때 global
    count = count + 1 # 접속할 때마다 방문자 1 증가
    
    return render(request, 'index.html', {'cnt': count})

def form(request):
    questions = Question.objects.all()
    
    context = {
        'questions' : questions,
    }
    
    return render(request, 'form2.html', context=context)


def result(request):
    print(f'POST : {request.POST}')
    
    sum = 0
    for i in range(10):
        j = str(i+1)
        sum += int(request.POST['question-'+j])
        
        
    if sum == 10:
        return render(request, 'result5.html')
    elif 8 <= sum and sum <= 9:
        return render(request, 'result4.html')
    elif 6 <= sum and sum <= 7:
        return render(request, 'result3.html')
    elif 3 <= sum and sum <= 5:
        return render(request, 'result2.html')
    else:
        return render(request, 'result1.html')
    
    # if request.method == 'POST':
    #     post = Result()


def loading(request):
    return render(request, 'loading_page.html')
