# 📊 Household Expense Tracker - Project Execution Guide
## Built with Basic Python (No Pandas, No Graph APIs)

---

## 🎯 Project Overview

**Project Name:** Ghar Ka Khata (Household Expense Tracker)  
**Style:** Khatabook-like digital ledger  
**Tech Stack:** Basic Python + Streamlit (No Pandas, No Plotly/Matplotlib)  
**Duration:** 3 Sprints (6 weeks)

---

## 🐍 Basic Python Concepts Used

This project uses ONLY fundamental Python programming:

| Concept | Where Used | Example |
|---------|------------|---------|
| **Lists** | Storing expenses | `expenses_list = []` |
| **Dictionaries** | Category structure, expense records | `{'date': '2026-01-21', 'amount': 500}` |
| **Loops (for)** | Filtering, calculating totals | `for expense in expenses_list:` |
| **Conditionals (if/else)** | Filtering logic | `if expense['amount'] > max_amount:` |
| **Functions** | Reusable code blocks | `def calculate_total(expenses_list):` |
| **File I/O** | JSON read/write | `json.load(file)`, `json.dump()` |
| **String Operations** | Date parsing, CSV generation | `date.split('-')` |
| **Bubble Sort** | Sorting expenses | Custom sort implementation |

---

## 📋 Phase 1: Project Planning (Sprint 0)

### 1.1 Jira Board Setup

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    JIRA BOARD: GHAR-KA-KHATA                            │
├──────────┬──────────┬─────────────┬─────────────┬──────────┬────────────┤
│ BACKLOG  │  TO DO   │ IN PROGRESS │ CODE REVIEW │ TESTING  │    DONE    │
├──────────┼──────────┼─────────────┼─────────────┼──────────┼────────────┤
│ GKK-008  │ GKK-006  │   GKK-004   │   GKK-003   │ GKK-002  │  GKK-001   │
│ GKK-009  │ GKK-007  │   GKK-005   │             │          │  GKK-000   │
└──────────┴──────────┴─────────────┴─────────────┴──────────┴────────────┘
```

### 1.2 User Stories (Jira Tickets)

| Ticket ID | Type  | Story Title                              | Priority | Points | Sprint |
|-----------|-------|------------------------------------------|----------|--------|--------|
| GKK-000   | Setup | Project Setup - Basic Python Structure   | Critical | 2      | 0      |
| GKK-001   | Story | Create Category/Subcategory Dictionary   | High     | 3      | 1      |
| GKK-002   | Story | Add Expense Using Dictionary & List      | High     | 5      | 1      |
| GKK-003   | Story | Calculate Totals Using Loops             | High     | 3      | 1      |
| GKK-004   | Story | Filter Expenses Using Conditionals       | High     | 5      | 1      |
| GKK-005   | Story | Sort Expenses Using Bubble Sort          | Medium   | 3      | 2      |
| GKK-006   | Story | Search Expenses Using String Matching    | Medium   | 3      | 2      |
| GKK-007   | Story | Export to CSV Using String Building      | Medium   | 3      | 2      |
| GKK-008   | Story | Analytics with Text-Based Charts         | Low      | 5      | 3      |
| GKK-009   | Story | Delete Expense by ID                     | Low      | 2      | 3      |

### 1.3 Detailed User Story Example

#### GKK-002: Add Expense Using Dictionary & List

**As a** household manager  
**I want to** add daily expenses with category and amount  
**So that** I can track where money is spent

**Acceptance Criteria:**
- [ ] Expense stored as dictionary with keys: date, category, subcategory, amount, payment_mode
- [ ] Expense added to list using `list.append()`
- [ ] Data saved to JSON file using `json.dump()`
- [ ] Form accepts user input via Streamlit

**Technical Implementation:**
```python
def add_expense(expenses_list, date, category, subcategory, description, amount, payment_mode):
    new_expense = {
        'id': len(expenses_list) + 1,
        'date': date,
        'category': category,
        'subcategory': subcategory,
        'description': description,
        'amount': amount,
        'payment_mode': payment_mode
    }
    expenses_list.append(new_expense)
    return expenses_list
```

---

## 📊 Phase 2: Google Sheet / Excel Template

### 2.1 Main Expense Sheet

| A (Date) | B (Category) | C (Subcategory) | D (Description) | E (Amount) | F (Payment) |
|----------|--------------|-----------------|-----------------|------------|-------------|
| 2026-01-15 | Groceries | Vegetables | Sabzi Mandi | 250 | Cash |
| 2026-01-15 | Utilities | Electricity | Jan Bill | 1500 | UPI |
| 2026-01-16 | Transport | Fuel/Petrol | Petrol | 500 | Card |

### 2.2 Summary Sheet (Manual Formulas)

| Category | Total (Formula) |
|----------|-----------------|
| Groceries | `=SUMIF(B:B,"Groceries",E:E)` |
| Utilities | `=SUMIF(B:B,"Utilities",E:E)` |
| Transport | `=SUMIF(B:B,"Transport",E:E)` |

### 2.3 Monthly Summary

| Month | Formula for Total |
|-------|-------------------|
| January 2026 | `=SUMIFS(E:E,A:A,">=2026-01-01",A:A,"<=2026-01-31")` |
| February 2026 | `=SUMIFS(E:E,A:A,">=2026-02-01",A:A,"<=2026-02-28")` |

---

## 🛠️ Phase 3: Development (Sprint 1 & 2)

### 3.1 Project Structure

```
expense_tracker_basic/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Only streamlit (no pandas!)
├── expenses_data.json      # Data storage (auto-created)
│
├── README.md               # Quick start guide
└── PROJECT_GUIDE.md        # This detailed document
```

### 3.2 Category Structure (Dictionary)

```python
CATEGORIES = {
    "🛒 Groceries": ["Vegetables", "Fruits", "Dairy", "Staples", "Snacks"],
    "💡 Utilities": ["Electricity", "Internet", "Water", "Gas", "Mobile"],
    "🏠 Housing": ["Rent", "Maintenance", "Repairs", "Furniture"],
    "🚗 Transportation": ["Fuel", "Auto/Cab", "Public Transport", "Parking"],
    "🏥 Medical": ["Medicines", "Doctor", "Tests", "Insurance"],
    "📚 Education": ["School Fees", "Books", "Tuition", "Courses"],
    "👕 Shopping": ["Clothes", "Footwear", "Electronics", "Appliances"],
    "🎬 Entertainment": ["Movies", "Subscriptions", "Dining Out", "Outings"],
    "💳 EMI/Loans": ["Home Loan", "Car Loan", "Personal Loan", "Credit Card"],
    "🎁 Others": ["Gifts", "Donations", "Miscellaneous"]
}
```

---

## 🐍 Basic Python Code Patterns Used

### Pattern 1: Calculate Total Using Loop

```python
def calculate_total(expenses_list):
    """Calculate total using basic loop"""
    total = 0
    for expense in expenses_list:
        total = total + expense['amount']
    return total
```

### Pattern 2: Filter Using Conditionals

```python
def filter_by_category(expenses_list, category):
    """Filter expenses by category using loop"""
    filtered_list = []
    for expense in expenses_list:
        if expense['category'] == category:
            filtered_list.append(expense)
    return filtered_list
```

### Pattern 3: Find Maximum Using Loop

```python
def find_max_expense(expenses_list):
    """Find maximum expense using loop"""
    if len(expenses_list) == 0:
        return 0
    max_amount = 0
    for expense in expenses_list:
        if expense['amount'] > max_amount:
            max_amount = expense['amount']
    return max_amount
```

### Pattern 4: Bubble Sort Implementation

```python
def sort_expenses_by_amount(expenses_list, ascending=True):
    """Sort expenses using bubble sort algorithm"""
    n = len(expenses_list)
    sorted_list = expenses_list.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if sorted_list[j]['amount'] > sorted_list[j + 1]['amount']:
                    # Swap elements
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            else:
                if sorted_list[j]['amount'] < sorted_list[j + 1]['amount']:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list
```

### Pattern 5: Dictionary Aggregation (Group By)

```python
def get_category_wise_totals(expenses_list):
    """Calculate category-wise totals using dictionary"""
    category_totals = {}
    
    # Initialize all categories with 0
    for category in CATEGORIES.keys():
        category_totals[category] = 0
    
    # Sum up amounts for each category
    for expense in expenses_list:
        category = expense['category']
        amount = expense['amount']
        category_totals[category] = category_totals[category] + amount
    
    return category_totals
```

### Pattern 6: Text-Based Bar Chart (No Plotly!)

```python
def generate_text_bar(value, max_value, bar_length=20):
    """Generate a text-based bar for visualization"""
    if max_value == 0:
        return "░" * bar_length
    
    filled_length = int((value / max_value) * bar_length)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return bar

# Usage:
# Groceries: ████████████░░░░░░░░ ₹5,000 (60%)
# Utilities: ██████░░░░░░░░░░░░░░ ₹2,500 (30%)
```

### Pattern 7: Search Using String Matching

```python
def search_expenses(expenses_list, search_term):
    """Search expenses by description using loop"""
    search_term_lower = search_term.lower()
    results = []
    
    for expense in expenses_list:
        description_lower = expense['description'].lower()
        
        if search_term_lower in description_lower:
            results.append(expense)
    
    return results
```

### Pattern 8: CSV Export Without Pandas

```python
def export_to_csv_format(expenses_list):
    """Convert expenses to CSV format string"""
    csv_lines = []
    csv_lines.append("Date,Category,Subcategory,Description,Amount,Payment Mode")
    
    for expense in expenses_list:
        line = f"{expense['date']},{expense['category']},{expense['subcategory']},{expense['description']},{expense['amount']},{expense['payment_mode']}"
        csv_lines.append(line)
    
    csv_string = "\n".join(csv_lines)
    return csv_string
```

---

## 🚀 How to Run

### Step 1: Install Streamlit Only

```bash
pip install streamlit
```

### Step 2: Run the App

```bash
streamlit run app.py
```

### Step 3: Open in Browser

```
http://localhost:8501
```

---

## 📱 App Features

| Page | Features | Python Concepts Used |
|------|----------|---------------------|
| Dashboard | Total, Count, Average, Category breakdown | Loops, Dictionary aggregation |
| Add Expense | Form input, Quick add buttons | Dictionary creation, List append |
| View Expenses | Filter, Sort, Search, Delete | Conditionals, Bubble sort, String matching |
| Analytics | Monthly trends, Category deep dive | Dictionary, Date parsing |
| Export | CSV, JSON, Summary report | File I/O, String building |

---

## 📅 Sprint Planning

### Sprint 1 (Week 2-3)
- [x] Category dictionary structure
- [x] Add expense function
- [x] Calculate total, average, max
- [x] Filter by date (today, week, month, year)
- [x] Basic Streamlit dashboard

### Sprint 2 (Week 4-5)
- [x] Filter by category, payment mode
- [x] Bubble sort implementation
- [x] Search function
- [x] Text-based bar charts
- [x] Export to CSV/JSON

### Sprint 3 (Week 6)
- [x] Delete expense
- [x] Analytics page
- [x] Summary report generation
- [ ] Future: Budget tracking
- [ ] Future: Recurring expenses

---

## 📝 Daily Standup Template

```
📅 Date: ___________
Developer: ___________

✅ Yesterday:
- Completed GKK-002 (Add Expense function)
- Tested with sample data

📋 Today:
- Start GKK-003 (Calculate Totals)
- Write unit tests for loops

🚧 Blockers:
- None
```

---

## 🔄 Git Workflow

```bash
# Create feature branch
git checkout -b feature/GKK-002-add-expense

# Make changes
git add app.py
git commit -m "GKK-002: Add expense function using dictionary and list"

# Push and create PR
git push origin feature/GKK-002-add-expense
```

---

## ✅ Definition of Done

- [ ] Code uses only basic Python (no pandas, no external graph libs)
- [ ] Code reviewed by peer
- [ ] Tested manually with sample data
- [ ] Documentation updated
- [ ] Works in Streamlit dashboard

---

## 🆚 Why Basic Python vs Pandas?

| Aspect | Basic Python | Pandas |
|--------|--------------|--------|
| Learning | Understand fundamentals | Black-box functions |
| Control | Full control over logic | Abstracted away |
| Debugging | Easy to trace | Complex stack traces |
| Performance | Slower for big data | Optimized |
| Dependencies | Minimal | Heavy |

**For learning:** Basic Python is better!  
**For production:** Consider Pandas for large datasets.

---

## 📞 Reference

- Python Lists: https://docs.python.org/3/tutorial/datastructures.html
- Python Dictionaries: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Streamlit: https://docs.streamlit.io

---

**Happy Learning! 🐍💰**
