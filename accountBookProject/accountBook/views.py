from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction  

# 홈 페이지 / Home page
def home(request):
    return render(request, 'home.html')

# 트랜잭션 목록 페이지 / Transaction list page
def transaction_list(request):
    transactions = Transaction.objects.all()  # 트랜잭션 데이터를 모두 가져오기
    return render(request, 'transaction_list.html', {'transactions': transactions})

# 트랜잭션 추가 페이지 / Add transaction page
def add_transaction(request):
    if request.method == 'POST':  # POST 요청일 때
        form = TransactionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            form.save()  # 데이터를 저장
            return redirect('transaction_list')  # 트랜잭션 목록 페이지로 리다이렉트
    else:
        form = TransactionForm()  # GET 요청일 때 빈 폼 생성
    return render(request, 'add_transaction.html', {'form': form})  # 폼을 템플릿에 전달