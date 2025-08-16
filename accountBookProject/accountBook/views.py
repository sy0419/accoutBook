# render 함수는 템플릿 파일을 렌더링해주는 함수
from django.shortcuts import render
from .models import Transaction

# Create your views here.
def home(request):
    # 'home.html' 템플릿을 렌더링해서 반환
    return render(request, 'home.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})