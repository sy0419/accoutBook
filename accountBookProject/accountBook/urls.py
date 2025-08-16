from django.urls import path
# views에서 함수 임포트 / Import views from the current app
from . import views  

# URL 패턴 정의 / Define URL patterns
urlpatterns = [
    # 기본 URL에 home 뷰 연결 / Link home view to the root URL
    path('', views.home, name='home'),  
]
