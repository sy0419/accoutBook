from django import forms
from .models import Transaction

# 트랜잭션 폼 정의 / Define the Transaction form
class TransactionForm(forms.ModelForm):
    # 모델과 폼을 연결 / Link the form to the model
    class Meta:
        model = Transaction  # 사용할 모델 / The model to use
        fields = ['date', 'category', 'account', 'description']  # 사용할 필드들 / Fields to include in the form