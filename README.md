# 💰 Django 가계부  
Django로 만든 간단한 개인 가계부 웹 애플리케이션입니다.  
사용자는 거래 내역을 추가, 수정, 삭제할 수 있고, 카테고리별 및 월별 합계를 확인할 수 있습니다.

---

## 📌 주요 기능  
- 📄 모든 거래 내역 조회  
- ➕ 수입/지출 거래 내역 추가  
- 📝 거래 내역 수정 및 삭제  
- 📊 카테고리별, 월별 합계 조회  
- 🌐 한글-영어 다국어 주석 포함  

---

## 🗂️ 화면 & 페이지  
| 경로                           | 설명                      |  
|------------------------------|-------------------------|  
| /                            | 홈 페이지 (네비게이션 포함) |  
| /transactions/                | 거래 목록 (수정/삭제 가능)    |  
| /transactions/add/            | 거래 내역 추가 페이지          |  
| /transactions/<id>/edit/      | 특정 거래 내역 수정 페이지       |  
| /transactions/delete/<id>/    | 삭제 확인 페이지               |  
| /transactions/summary/        | 카테고리별 합계 테이블          |  
| /transactions/monthly-summary/| 월별 합계 테이블               |  

---

## 🛠️ 기술 스택  
- 백엔드: Django 5.x  
- 프론트엔드: HTML5 + Django 템플릿 엔진  
- 데이터베이스: SQLite (기본, 변경 가능)  
- 프로그래밍 언어: Python 3.11 이상  
- 개발 환경: Virtualenv (venv)  

---

## 🚀 시작하기  

### 1. 저장소 클론  
```bash
git clone https://github.com/your-username/account-book.git
cd account-book
```

### 2. 가상환경 설정
```bash
python -m venv venv
source venv/Scripts/activate  # Windows  
# 또는  
source venv/bin/activate     # macOS/Linux
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```
만약 requirements.txt 파일이 없으면 아래 명령어로 Django를 직접 설치하세요.
```bash
만약 requirements.txt 파일이 없으면 아래 명령어로 Django를 직접 설치하세요.
```

### 4. 마이그레이션 적용
```bash
python manage.py makemigrations
python manage.py migrate\
```

### 5. 서버 실행
```bash
python manage.py runserver
```
브라우저에서 http://127.0.0.1:8000 으로 접속하세요.

### 📁 프로젝트 구조 (주요 파일)
```bash
accountBookProject/
├── accountBook/                 # 메인 Django 앱
│   ├── migrations/             # 데이터베이스 마이그레이션 파일
│   ├── templates/              # 템플릿 HTML 파일들
│   │   ├── add_transaction.html         # 거래 내역 추가 페이지  
│   │   ├── delete_transaction.html      # 삭제 확인 페이지  
│   │   ├── edit_transaction.html        # 거래 내역 수정 페이지  
│   │   ├── home.html                    # 메인 홈 페이지  
│   │   ├── transaction_list.html        # 거래 목록 및 합계 페이지  
│   │   ├── category_summary.html        # 카테고리별 합계 페이지  
│   │   └── monthly_summary.html         # 월별 합계 페이지  
│   ├── models.py                # Transaction 모델 정의  
│   ├── forms.py                 # 거래 내역 입력 폼  
│   ├── views.py                 # CRUD 및 합계 로직 처리  
│   └── urls.py                  # 앱별 URL 경로  
├── accountBookProject/
│   └── urls.py                  # 프로젝트 전체 URL 경로  
├── db.sqlite3                   # SQLite DB 파일  
└── manage.py                    # Django 실행 스크립트  
```

### 📝 Transaction 모델 예시
```bash
class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    CATEGORY_CHOICES = [
        ('income', '수입'),
        ('expense', '지출')
    ]
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255, blank=True)
```

### 🙌 제작자
박신영
Django로 간단히 수입과 지출을 관리하고자 만들어진 프로젝트입니다.
피드백과 기여는 언제나 환영합니다!

---

# 💰 Django Account Book

A simple personal account book web application built with Django.  
Users can add, edit, delete transactions, and view summaries by category and month.

---

## 📌 Features

- 📄 View a list of all transactions
- ➕ Add a new transaction (income or expense)
- 📝 Edit or delete existing transactions
- 📊 View **category-wise** and **monthly** summaries
- 🌐 Korean-English bilingual interface (commented)

---

## 🗂️ Screens & Pages

| Page | Description |
|------|-------------|
| `/` | Home page with navigation |
| `/transactions/` | Transaction list with edit/delete options |
| `/transactions/add/` | Add a new transaction |
| `/transactions/<id>/edit/` | Edit a specific transaction |
| `/transactions/delete/<id>/` | Delete confirmation page |
| `/transactions/summary/` | Category-wise summary table |
| `/transactions/monthly-summary/` | Monthly summary table |

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML5 + Django Template Engine
- **Database**: SQLite (default, easily switchable)
- **Language**: Python 3.11+
- **Environment**: Virtualenv (`venv`)

---

## 🚀 Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/your-username/account-book.git
cd account-book
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
If requirements.txt doesn't exist, manually install Django:
```bash
pip install django
```

### 4.Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the server
```bash
python manage.py runserver
```
Then go to http://127.0.0.1:8000 in your browser.

### 📁 Project Structure (Main Parts)
```bash
accountBookProject/
├── accountBook/                 # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   ├── add_transaction.html         # Add a new transaction
│   │   ├── delete_transaction.html      # Confirm deletion
│   │   ├── edit_transaction.html        # Edit a transaction
│   │   ├── home.html                    # Landing page
│   │   ├── transaction_list.html        # All transactions + summaries
│   │   ├── category_summary.html        # Summary by category
│   │   └── monthly_summary.html         # Summary by month
│   ├── models.py                # Transaction model
│   ├── forms.py                 # TransactionForm for input
│   ├── views.py                 # All logic for CRUD and summaries
│   └── urls.py                  # App-level routes
├── accountBookProject/
│   └── urls.py                  # Project-level routes
├── db.sqlite3                   # SQLite database
└── manage.py                    # Django entry point
```

### 📝 Transaction Model
```bash
class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255, blank=True)
```

### 🙌 Author

Made by **shinyoungPark**  
Inspired by the need to simply track income and expenses with Django.  
Feedback and contributions welcome!

---

### 📜 License

MIT License  
Feel free to use, modify, and share.
