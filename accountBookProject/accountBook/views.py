from django.shortcuts import render, redirect, get_object_or_404
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

# 거래 수정 페이지 / Edit transaction page
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk) # 수정할 거래 데이터 가져오기
    if request.method == 'POST': # POST 요청 시
        form = TransactionForm(request.POST, instance=transaction) # 기존 데이터에 덮어쓰기
        if form.is_valid(): # 폼 검증 통과하면
            form.save() # 저장
            return redirect('transaction_list') # 거래 목록 페이지로 리다이렉트
    else:
        form = TransactionForm(instance=transaction) # GET 요청 시 기존 데이터를 채운 폼 생성
        return render(request, 'edit_transaction.html', {'form': form}) # 템플릿에 폼 전달

# 거래 삭제 페이지 / Delete transaction page 
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk) # 삭제할 거래 가져오기 / Get the transaction to delete
    if request.method == 'POST': # POST 요청일 때 삭제 실행 / Delete on POST request
        transaction.delete()
        return redirect('transaction_list') # 삭제 후 거래 목록 페이지로 리다이렉트 / Redirect to transaction list after delete
    return render(request, 'delete_transaction.html', {'transaction': transaction}) # 확인 페이지 렌더링 / Render confirmation page