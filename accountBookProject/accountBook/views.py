from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from .models import Transaction  
from django.db.models import Sum
from django.db.models.functions import TruncMonth

# 홈 페이지 / Home page
def home(request):
    return render(request, 'home.html')

# 트랜잭션 목록 페이지 / Transaction list page
def transaction_list(request):
    transactions = Transaction.objects.all()
    category_summary = transactions.values('category').annotate(total_amount=Sum('amount'))
    monthly_summary = transactions.annotate(month=TruncMonth('date')) \
                                  .values('month') \
                                  .annotate(total_amount=Sum('amount')) \
                                  .order_by('month')

    context = {
        'transactions': transactions,
        'category_summary': category_summary,
        'monthly_summary': monthly_summary,
    }
    return render(request, 'transaction_list.html', context)

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

# 카테고리별 거래 금액 합계를 계산하여 보여주는 뷰
# View to show the total transaction amount grouped by category
def category_summary(request):
    summary = Transaction.objects.values('category').annotate(total_amount=Sum('amount')) # 각 카테고리의 총 합계 계산 / Sum per category
    return render(request, 'category_summary.html', {'summary': summary}) # 템플릿에 결과 전달 / Render result to template

# 월별 거래 금액 합계 조회 뷰 / View to compute monthly transaction totals
def monthly_summary(request):
    summary = (
        Transaction.objects
        .annotate(month=TruncMonth('date'))              # 날짜를 월 단위로 자르기 / Truncate date to month
        .values('month')                                 # 월별 그룹화 / Group by month
        .annotate(total_amount=Sum('amount'))            # 각 월에 대한 금액 합계 계산 / Sum of amounts per month
        .order_by('month')                               # 월 순서대로 정렬 / Order by month
    )
    return render(request, 'monthly_summary.html', {'summary': summary})