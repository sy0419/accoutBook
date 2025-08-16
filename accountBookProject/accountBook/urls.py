from django.urls import path
# views에서 함수 임포트 / Import views from the current app
from . import views  

# URL 패턴 정의 / Define URL patterns
urlpatterns = [
    path('', views.home, name='home'),  # 홈 페이지 / Home page
    path('transactions/', views.transaction_list, name='transaction_list'),  # 트랜잭션 목록 페이지 / Transaction list page
    path('transactions/add/', views.add_transaction, name='add_transaction'),  # 트랜잭션 추가 페이지 / Transactiono adding page
    path('transactions/<int:pk>/edit/', views.edit_transaction, name='edit_transaction'),  # 거래 수정 페이지 / Edit transaction page
]