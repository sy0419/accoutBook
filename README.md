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

Made by **[Your Name]**  
Inspired by the need to simply track income and expenses with Django.  
Feedback and contributions welcome!

---

### 📜 License

MIT License  
Feel free to use, modify, and share.
