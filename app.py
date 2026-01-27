"""
Household Expense Tracker - Khatabook Style
Using Basic Python (No Pandas, No Graph API'.)
Built with: Loops, Dictionaries, Lists, File Handling + Streamlit Dashboard
"""

import streamlit as st
import json
import os
from datetime import datetime, timedelta

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Ghar Ka Khata - Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# Data file path
DATA_FILE = "expenses_data.json"

# ============================================================================
# CATEGORY STRUCTURE (Using Dictionary)
# ============================================================================

CATEGORIES = {
    "🛒 Groceries": ["Vegetables", "Fruits", "Dairy", "Staples (Rice/Dal)", "Snacks", "Beverages"],
    "💡 Utilities": ["Electricity", "Internet", "Water", "Gas (LPG)", "Mobile Recharge"],
    "🏠 Housing": ["Rent", "Maintenance", "Repairs", "Furniture"],
    "🚗 Transportation": ["Fuel/Petrol", "Auto/Cab", "Public Transport", "Parking"],
    "🏥 Medical": ["Medicines", "Doctor Visits", "Tests/Lab", "Insurance"],
    "📚 Education": ["School Fees", "Books", "Tuition", "Online Courses"],
    "👕 Shopping": ["Clothes", "Footwear", "Electronics", "Appliances"],
    "🎬 Entertainment": ["Movies", "Subscriptions", "Dining Out", "Outings"],
    "💳 EMI/Loans": ["Home Loan", "Car Loan", "Personal Loan", "Credit Card"],
    "🎁 Others": ["Gifts", "Donations", "Miscellaneous"]
}

PAYMENT_MODES = ["Cash", "UPI", "Credit Card", "Debit Card", "Net Banking"]

# ============================================================================
# BASIC PYTHON FUNCTIONS (No Pandas - Using Loops & Lists)
# ============================================================================

def load_expenses():
    """Load expenses from JSON file using basic file handling"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return data
    return []  # Return empty list if no file exists


def save_expenses(expenses_list):
    """Save expenses to JSON file using basic file handling"""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses_list, file, indent=2)


def add_expense(expenses_list, date, category, subcategory, description, amount, payment_mode):
    """Add new expense to list using dictionary"""
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


def delete_expense(expenses_list, expense_id):
    """Delete expense by ID using loop"""
    new_list = []
    for expense in expenses_list:
        if expense['id'] != expense_id:
            new_list.append(expense)
    return new_list


def calculate_total(expenses_list):
    """Calculate total using basic loop"""
    total = 0
    for expense in expenses_list:
        total = total + expense['amount']
    return total


def calculate_average(expenses_list):
    """Calculate average using basic math"""
    if len(expenses_list) == 0:
        return 0
    total = calculate_total(expenses_list)
    average = total / len(expenses_list)
    return round(average, 2)


def find_max_expense(expenses_list):
    """Find maximum expense using loop"""
    if len(expenses_list) == 0:
        return 0
    max_amount = 0
    for expense in expenses_list:
        if expense['amount'] > max_amount:
            max_amount = expense['amount']
    return max_amount


def find_min_expense(expenses_list):
    """Find minimum expense using loop"""
    if len(expenses_list) == 0:
        return 0
    min_amount = expenses_list[0]['amount']
    for expense in expenses_list:
        if expense['amount'] < min_amount:
            min_amount = expense['amount']
    return min_amount


def filter_by_date_range(expenses_list, start_date, end_date):
    """Filter expenses by date range using loop"""
    filtered_list = []
    for expense in expenses_list:
        expense_date = expense['date']
        if start_date <= expense_date <= end_date:
            filtered_list.append(expense)
    return filtered_list


def filter_by_category(expenses_list, category):
    """Filter expenses by category using loop"""
    filtered_list = []
    for expense in expenses_list:
        if expense['category'] == category:
            filtered_list.append(expense)
    return filtered_list


def filter_by_payment_mode(expenses_list, payment_mode):
    """Filter expenses by payment mode using loop"""
    filtered_list = []
    for expense in expenses_list:
        if expense['payment_mode'] == payment_mode:
            filtered_list.append(expense)
    return filtered_list


def filter_today(expenses_list):
    """Filter today's expenses using loop"""
    today = datetime.now().strftime('%Y-%m-%d')
    filtered_list = []
    for expense in expenses_list:
        if expense['date'] == today:
            filtered_list.append(expense)
    return filtered_list


def filter_this_week(expenses_list):
    """Filter this week's expenses using loop"""
    today = datetime.now()
    week_start = today - timedelta(days=today.weekday())
    week_start_str = week_start.strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')
    
    filtered_list = []
    for expense in expenses_list:
        if week_start_str <= expense['date'] <= today_str:
            filtered_list.append(expense)
    return filtered_list


def filter_this_month(expenses_list):
    """Filter this month's expenses using loop"""
    today = datetime.now()
    month_start = today.replace(day=1).strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')
    
    filtered_list = []
    for expense in expenses_list:
        if month_start <= expense['date'] <= today_str:
            filtered_list.append(expense)
    return filtered_list


def filter_this_year(expenses_list):
    """Filter this year's expenses using loop"""
    today = datetime.now()
    year_start = today.replace(month=1, day=1).strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')
    
    filtered_list = []
    for expense in expenses_list:
        if year_start <= expense['date'] <= today_str:
            filtered_list.append(expense)
    return filtered_list


def get_category_wise_totals(expenses_list):
    """Calculate category-wise totals using dictionary and loop"""
    category_totals = {}
    
    # Initialize all categories with 0
    for category in CATEGORIES.keys():
        category_totals[category] = 0
    
    # Sum up amounts for each category
    for expense in expenses_list:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
    
    return category_totals


def get_subcategory_wise_totals(expenses_list, category):
    """Calculate subcategory-wise totals for a specific category"""
    subcategory_totals = {}
    
    # Initialize subcategories with 0
    if category in CATEGORIES:
        for subcategory in CATEGORIES[category]:
            subcategory_totals[subcategory] = 0
    
    # Sum up amounts
    for expense in expenses_list:
        if expense['category'] == category:
            subcategory = expense['subcategory']
            amount = expense['amount']
            if subcategory in subcategory_totals:
                subcategory_totals[subcategory] = subcategory_totals[subcategory] + amount
    
    return subcategory_totals


def get_payment_mode_totals(expenses_list):
    """Calculate payment mode-wise totals using dictionary and loop"""
    payment_totals = {}
    
    # Initialize all payment modes with 0
    for mode in PAYMENT_MODES:
        payment_totals[mode] = 0
    
    # Sum up amounts for each payment mode
    for expense in expenses_list:
        mode = expense['payment_mode']
        amount = expense['amount']
        if mode in payment_totals:
            payment_totals[mode] = payment_totals[mode] + amount
    
    return payment_totals


def get_daily_totals(expenses_list):
    """Calculate daily totals using dictionary and loop"""
    daily_totals = {}
    
    for expense in expenses_list:
        date = expense['date']
        amount = expense['amount']
        
        if date in daily_totals:
            daily_totals[date] = daily_totals[date] + amount
        else:
            daily_totals[date] = amount
    
    return daily_totals


def get_monthly_totals(expenses_list):
    """Calculate monthly totals using dictionary and loop"""
    monthly_totals = {}
    
    for expense in expenses_list:
        # Extract year-month from date
        date_parts = expense['date'].split('-')
        year_month = date_parts[0] + '-' + date_parts[1]
        amount = expense['amount']
        
        if year_month in monthly_totals:
            monthly_totals[year_month] = monthly_totals[year_month] + amount
        else:
            monthly_totals[year_month] = amount
    
    return monthly_totals


def sort_expenses_by_date(expenses_list, ascending=True):
    """Sort expenses by date using bubble sort"""
    n = len(expenses_list)
    sorted_list = expenses_list.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if sorted_list[j]['date'] > sorted_list[j + 1]['date']:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            else:
                if sorted_list[j]['date'] < sorted_list[j + 1]['date']:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list


def sort_expenses_by_amount(expenses_list, ascending=True):
    """Sort expenses by amount using bubble sort"""
    n = len(expenses_list)
    sorted_list = expenses_list.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if sorted_list[j]['amount'] > sorted_list[j + 1]['amount']:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
            else:
                if sorted_list[j]['amount'] < sorted_list[j + 1]['amount']:
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list


def search_expenses(expenses_list, search_term):
    """Search expenses by description using loop"""
    search_term_lower = search_term.lower()
    results = []
    
    for expense in expenses_list:
        description_lower = expense['description'].lower()
        category_lower = expense['category'].lower()
        subcategory_lower = expense['subcategory'].lower()
        
        if (search_term_lower in description_lower or 
            search_term_lower in category_lower or 
            search_term_lower in subcategory_lower):
            results.append(expense)
    
    return results


def generate_text_bar(value, max_value, bar_length=20):
    """Generate a text-based bar for visualization"""
    if max_value == 0:
        return "░" * bar_length
    
    filled_length = int((value / max_value) * bar_length)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return bar


def export_to_csv_format(expenses_list):
    """Convert expenses to CSV format string"""
    csv_lines = []
    csv_lines.append("Date,Category,Subcategory,Description,Amount,Payment Mode")
    
    for expense in expenses_list:
        line = f"{expense['date']},{expense['category']},{expense['subcategory']},{expense['description']},{expense['amount']},{expense['payment_mode']}"
        csv_lines.append(line)
    
    csv_string = "\n".join(csv_lines)
    return csv_string


# ============================================================================
# STREAMLIT DASHBOARD
# ============================================================================

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = load_expenses()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .category-box {
        background: #f0f2f6;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.3rem 0;
        border-left: 4px solid #1E88E5;
    }
    .expense-row {
        background: white;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.3rem 0;
        border: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 📊 Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["🏠 Dashboard", "➕ Add Expense", "📋 View Expenses", "📈 Analytics", "📥 Export Data"]
)

# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================

if page == "🏠 Dashboard":
    st.markdown('<h1 class="main-header">💰 Ghar Ka Khata</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Household Expense Tracker - Like Khatabook!</p>', unsafe_allow_html=True)
    
    # Period selector
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        period = st.selectbox("📅 Select Period", ["Today", "This Week", "This Month", "This Year", "All Time"])
    
    # Filter data based on period
    if period == "Today":
        filtered_expenses = filter_today(st.session_state.expenses)
    elif period == "This Week":
        filtered_expenses = filter_this_week(st.session_state.expenses)
    elif period == "This Month":
        filtered_expenses = filter_this_month(st.session_state.expenses)
    elif period == "This Year":
        filtered_expenses = filter_this_year(st.session_state.expenses)
    else:
        filtered_expenses = st.session_state.expenses
    
    # Summary Metrics
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    total = calculate_total(filtered_expenses)
    count = len(filtered_expenses)
    avg = calculate_average(filtered_expenses)
    max_exp = find_max_expense(filtered_expenses)
    
    with col1:
        st.metric("💵 Total Expenses", f"₹{total:,.2f}")
    with col2:
        st.metric("📝 Transactions", count)
    with col3:
        st.metric("📊 Average", f"₹{avg:,.2f}")
    with col4:
        st.metric("🔝 Highest", f"₹{max_exp:,.2f}")
    
    # Category-wise Breakdown (Text-based visualization)
    st.markdown("---")
    st.subheader("📊 Category-wise Breakdown")
    
    if len(filtered_expenses) > 0:
        category_totals = get_category_wise_totals(filtered_expenses)
        
        # Find max for scaling
        max_category_amount = 0
        for category, amount in category_totals.items():
            if amount > max_category_amount:
                max_category_amount = amount
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Category Breakdown:**")
            for category, amount in category_totals.items():
                if amount > 0:
                    bar = generate_text_bar(amount, max_category_amount, 15)
                    percentage = (amount / total * 100) if total > 0 else 0
                    st.markdown(f"""
                    <div class="category-box">
                        <strong>{category}</strong><br>
                        <code>{bar}</code> ₹{amount:,.2f} ({percentage:.1f}%)
                    </div>
                    """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Payment Mode Breakdown:**")
            payment_totals = get_payment_mode_totals(filtered_expenses)
            
            max_payment_amount = 0
            for mode, amount in payment_totals.items():
                if amount > max_payment_amount:
                    max_payment_amount = amount
            
            for mode, amount in payment_totals.items():
                if amount > 0:
                    bar = generate_text_bar(amount, max_payment_amount, 15)
                    percentage = (amount / total * 100) if total > 0 else 0
                    st.markdown(f"""
                    <div class="category-box">
                        <strong>{mode}</strong><br>
                        <code>{bar}</code> ₹{amount:,.2f} ({percentage:.1f}%)
                    </div>
                    """, unsafe_allow_html=True)
        
        # Recent Transactions
        st.markdown("---")
        st.subheader("📋 Recent Transactions")
        
        sorted_expenses = sort_expenses_by_date(filtered_expenses, ascending=False)
        recent_5 = sorted_expenses[:5]  # Get first 5 (most recent)
        
        for expense in recent_5:
            st.markdown(f"""
            <div class="expense-row">
                📅 <strong>{expense['date']}</strong> | 
                {expense['category']} → {expense['subcategory']} | 
                <strong>₹{expense['amount']:,.2f}</strong> | 
                {expense['payment_mode']} | 
                <em>{expense['description']}</em>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No expenses recorded for this period. Start by adding an expense!")

# ============================================================================
# PAGE 2: ADD EXPENSE
# ============================================================================

elif page == "➕ Add Expense":
    st.markdown('<h1 class="main-header">➕ Add New Expense</h1>', unsafe_allow_html=True)
    
    with st.form("expense_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            expense_date = st.date_input("📅 Date", datetime.now())
            category = st.selectbox("📁 Category", list(CATEGORIES.keys()))
            
            # Get subcategories for selected category using basic access
            subcategory_options = CATEGORIES[category]
            subcategory = st.selectbox("📂 Subcategory", subcategory_options)
        
        with col2:
            amount = st.number_input("💰 Amount (₹)", min_value=0.0, step=10.0)
            payment_mode = st.selectbox("💳 Payment Mode", PAYMENT_MODES)
            description = st.text_input("📝 Description (Optional)", "")
        
        submitted = st.form_submit_button("💾 Save Expense", use_container_width=True)
        
        if submitted:
            if amount > 0:
                date_str = expense_date.strftime('%Y-%m-%d')
                st.session_state.expenses = add_expense(
                    st.session_state.expenses,
                    date_str,
                    category,
                    subcategory,
                    description,
                    amount,
                    payment_mode
                )
                save_expenses(st.session_state.expenses)
                st.success(f"✅ Expense of ₹{amount:,.2f} added successfully!")
                st.balloons()
            else:
                st.error("❌ Please enter a valid amount!")
    
    # Quick Add Section
    st.markdown("---")
    st.subheader("⚡ Quick Add Common Expenses")
    
    quick_items = [
        ("🥛 Milk ₹50", "🛒 Groceries", "Dairy", "Milk", 50),
        ("🥬 Vegetables ₹100", "🛒 Groceries", "Vegetables", "Sabzi", 100),
        ("⛽ Petrol ₹500", "🚗 Transportation", "Fuel/Petrol", "Petrol", 500),
        ("📱 Recharge ₹299", "💡 Utilities", "Mobile Recharge", "Mobile", 299),
    ]
    
    cols = st.columns(4)
    for i in range(len(quick_items)):
        item = quick_items[i]
        with cols[i]:
            if st.button(item[0], key=f"quick_{i}", use_container_width=True):
                today_str = datetime.now().strftime('%Y-%m-%d')
                st.session_state.expenses = add_expense(
                    st.session_state.expenses,
                    today_str,
                    item[1],  # category
                    item[2],  # subcategory
                    item[3],  # description
                    item[4],  # amount
                    "Cash"
                )
                save_expenses(st.session_state.expenses)
                st.success(f"✅ {item[3]} added!")
                st.rerun()

# ============================================================================
# PAGE 3: VIEW EXPENSES
# ============================================================================

elif page == "📋 View Expenses":
    st.markdown('<h1 class="main-header">📋 All Expenses</h1>', unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        filter_cat = st.selectbox("Filter Category", ["All"] + list(CATEGORIES.keys()))
    with col2:
        filter_payment = st.selectbox("Filter Payment", ["All"] + PAYMENT_MODES)
    with col3:
        sort_by = st.selectbox("Sort By", ["Date (Newest)", "Date (Oldest)", "Amount (High)", "Amount (Low)"])
    with col4:
        search_term = st.text_input("🔍 Search", "")
    
    # Apply filters using our basic functions
    display_expenses = st.session_state.expenses.copy()
    
    if filter_cat != "All":
        display_expenses = filter_by_category(display_expenses, filter_cat)
    
    if filter_payment != "All":
        display_expenses = filter_by_payment_mode(display_expenses, filter_payment)
    
    if search_term:
        display_expenses = search_expenses(display_expenses, search_term)
    
    # Apply sorting
    if sort_by == "Date (Newest)":
        display_expenses = sort_expenses_by_date(display_expenses, ascending=False)
    elif sort_by == "Date (Oldest)":
        display_expenses = sort_expenses_by_date(display_expenses, ascending=True)
    elif sort_by == "Amount (High)":
        display_expenses = sort_expenses_by_amount(display_expenses, ascending=False)
    elif sort_by == "Amount (Low)":
        display_expenses = sort_expenses_by_amount(display_expenses, ascending=True)
    
    # Display summary
    total_filtered = calculate_total(display_expenses)
    st.markdown(f"**Showing {len(display_expenses)} expenses | Total: ₹{total_filtered:,.2f}**")
    
    st.markdown("---")
    
    # Display expenses in a table format
    if len(display_expenses) > 0:
        # Table header
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5, 2, 2, 2, 1.5, 1.5, 1])
        col1.markdown("**Date**")
        col2.markdown("**Category**")
        col3.markdown("**Subcategory**")
        col4.markdown("**Description**")
        col5.markdown("**Amount**")
        col6.markdown("**Payment**")
        col7.markdown("**Action**")
        
        st.markdown("---")
        
        # Table rows
        for expense in display_expenses:
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1.5, 2, 2, 2, 1.5, 1.5, 1])
            col1.write(expense['date'])
            col2.write(expense['category'])
            col3.write(expense['subcategory'])
            col4.write(expense['description'] if expense['description'] else "-")
            col5.write(f"₹{expense['amount']:,.2f}")
            col6.write(expense['payment_mode'])
            
            if col7.button("🗑️", key=f"del_{expense['id']}"):
                st.session_state.expenses = delete_expense(st.session_state.expenses, expense['id'])
                save_expenses(st.session_state.expenses)
                st.rerun()
    else:
        st.info("No expenses found matching your criteria.")

# ============================================================================
# PAGE 4: ANALYTICS
# ============================================================================

elif page == "📈 Analytics":
    st.markdown('<h1 class="main-header">📈 Expense Analytics</h1>', unsafe_allow_html=True)
    
    if len(st.session_state.expenses) > 0:
        # Monthly Totals
        st.subheader("📅 Monthly Expense Summary")
        monthly_totals = get_monthly_totals(st.session_state.expenses)
        
        # Find max for scaling
        max_monthly = 0
        for month, amount in monthly_totals.items():
            if amount > max_monthly:
                max_monthly = amount
        
        # Sort months
        sorted_months = sorted(monthly_totals.keys())
        
        for month in sorted_months:
            amount = monthly_totals[month]
            bar = generate_text_bar(amount, max_monthly, 30)
            st.markdown(f"**{month}**: `{bar}` ₹{amount:,.2f}")
        
        st.markdown("---")
        
        # Category Deep Dive
        st.subheader("🔍 Category Deep Dive")
        selected_category = st.selectbox("Select Category to Analyze", list(CATEGORIES.keys()))
        
        category_expenses = filter_by_category(st.session_state.expenses, selected_category)
        
        if len(category_expenses) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**{selected_category} Summary:**")
                cat_total = calculate_total(category_expenses)
                cat_count = len(category_expenses)
                cat_avg = calculate_average(category_expenses)
                
                st.markdown(f"- Total Spent: **₹{cat_total:,.2f}**")
                st.markdown(f"- Transactions: **{cat_count}**")
                st.markdown(f"- Average: **₹{cat_avg:,.2f}**")
            
            with col2:
                st.markdown("**Subcategory Breakdown:**")
                subcat_totals = get_subcategory_wise_totals(st.session_state.expenses, selected_category)
                
                max_subcat = 0
                for subcat, amount in subcat_totals.items():
                    if amount > max_subcat:
                        max_subcat = amount
                
                for subcat, amount in subcat_totals.items():
                    if amount > 0:
                        bar = generate_text_bar(amount, max_subcat, 15)
                        st.markdown(f"- {subcat}: `{bar}` ₹{amount:,.2f}")
        else:
            st.info(f"No expenses in {selected_category}")
        
        st.markdown("---")
        
        # Daily Pattern
        st.subheader("📆 Daily Spending Pattern")
        daily_totals = get_daily_totals(st.session_state.expenses)
        
        # Get last 7 days
        today = datetime.now()
        last_7_days = []
        for i in range(6, -1, -1):
            day = today - timedelta(days=i)
            day_str = day.strftime('%Y-%m-%d')
            last_7_days.append(day_str)
        
        max_daily = 0
        for day in last_7_days:
            amount = daily_totals.get(day, 0)
            if amount > max_daily:
                max_daily = amount
        
        st.markdown("**Last 7 Days:**")
        for day in last_7_days:
            amount = daily_totals.get(day, 0)
            bar = generate_text_bar(amount, max_daily, 25)
            day_name = datetime.strptime(day, '%Y-%m-%d').strftime('%a %d/%m')
            st.markdown(f"{day_name}: `{bar}` ₹{amount:,.2f}")
        
    else:
        st.info("Add some expenses to see analytics!")

# ============================================================================
# PAGE 5: EXPORT DATA
# ============================================================================

elif page == "📥 Export Data":
    st.markdown('<h1 class="main-header">📥 Export Data</h1>', unsafe_allow_html=True)
    
    if len(st.session_state.expenses) > 0:
        st.subheader("📋 Data Preview")
        
        # Display preview
        sorted_expenses = sort_expenses_by_date(st.session_state.expenses, ascending=False)
        
        # Show first 10
        preview_count = min(10, len(sorted_expenses))
        st.markdown(f"Showing first {preview_count} of {len(sorted_expenses)} records:")
        
        for i in range(preview_count):
            expense = sorted_expenses[i]
            st.markdown(f"""
            {i+1}. **{expense['date']}** | {expense['category']} | {expense['subcategory']} | ₹{expense['amount']:,.2f} | {expense['payment_mode']}
            """)
        
        st.markdown("---")
        st.subheader("📤 Download Options")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # CSV Download
            csv_data = export_to_csv_format(st.session_state.expenses)
            st.download_button(
                label="📄 Download CSV",
                data=csv_data,
                file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col2:
            # JSON Download
            json_data = json.dumps(st.session_state.expenses, indent=2)
            st.download_button(
                label="📋 Download JSON",
                data=json_data,
                file_name=f"expenses_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        with col3:
            # Summary Report
            total = calculate_total(st.session_state.expenses)
            avg = calculate_average(st.session_state.expenses)
            max_exp = find_max_expense(st.session_state.expenses)
            min_exp = find_min_expense(st.session_state.expenses)
            
            category_totals = get_category_wise_totals(st.session_state.expenses)
            payment_totals = get_payment_mode_totals(st.session_state.expenses)
            
            # Build summary string
            summary_lines = []
            summary_lines.append("=" * 50)
            summary_lines.append("EXPENSE TRACKER - SUMMARY REPORT")
            summary_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            summary_lines.append("=" * 50)
            summary_lines.append("")
            summary_lines.append(f"Total Expenses: Rs.{total:,.2f}")
            summary_lines.append(f"Total Transactions: {len(st.session_state.expenses)}")
            summary_lines.append(f"Average Expense: Rs.{avg:,.2f}")
            summary_lines.append(f"Highest Expense: Rs.{max_exp:,.2f}")
            summary_lines.append(f"Lowest Expense: Rs.{min_exp:,.2f}")
            summary_lines.append("")
            summary_lines.append("-" * 50)
            summary_lines.append("CATEGORY-WISE BREAKDOWN")
            summary_lines.append("-" * 50)
            
            for category, amount in category_totals.items():
                if amount > 0:
                    summary_lines.append(f"{category}: Rs.{amount:,.2f}")
            
            summary_lines.append("")
            summary_lines.append("-" * 50)
            summary_lines.append("PAYMENT MODE BREAKDOWN")
            summary_lines.append("-" * 50)
            
            for mode, amount in payment_totals.items():
                if amount > 0:
                    summary_lines.append(f"{mode}: Rs.{amount:,.2f}")
            
            summary_lines.append("")
            summary_lines.append("=" * 50)
            
            summary_text = "\n".join(summary_lines)
            
            st.download_button(
                label="📊 Download Summary",
                data=summary_text,
                file_name=f"expense_summary_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        # Google Sheets Instructions
        st.markdown("---")
        st.subheader("📊 Google Sheets / Excel Instructions")
        st.info("""
        **To import into Google Sheets:**
        1. Download the CSV file above
        2. Open Google Sheets → File → Import
        3. Upload the CSV file
        4. Select 'Replace spreadsheet' or 'Insert new sheet'
        
        **To import into Excel:**
        1. Download the CSV file above
        2. Open Excel → Data → From Text/CSV
        3. Select the downloaded file
        4. Follow the import wizard
        """)
    else:
        st.info("No data to export. Start by adding some expenses!")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#888;">💰 Ghar Ka Khata - Built with Basic Python + Streamlit | No Pandas, No Graph APIs!</p>',
    unsafe_allow_html=True
)
