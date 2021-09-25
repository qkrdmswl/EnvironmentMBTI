from django.shortcuts import render
from .models import Question, Embti, Choice

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
    # 문항 수
    N = Question.objects.count()
    # embti 유형 수
    K = Embti.objects.count()
    
    counter = [0] * (K+1)
    
    for n in range(1,N+1):
        embti_id = int(request.POST[f'question-{n}'][0])
        counter[embti_id] += 1
        
        # 최고점 유형
    best_embti_id = max(range(1, K+1), key=lambda id : counter[id])
    best_embti = Embti.objects.get(pk=best_embti_id)
    best_embti.count += 1
    best_embti.save()
        
    context = {
        'embti' : best_embti,
        'counter' : counter
    }
        
    return render(request, 'result.html', context)

def loading(request):
    return render(request, 'loading_page.html')