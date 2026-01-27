"""
Household Expense Tracker - Khatabook Style
Using Basic Python (No Pandas, No Graph APIs)
Built with: Loops, Dictionaries, Lists, File Handling + Streamlit Dashboard
Version: 3.0 - Dynamic Subcategories + Edit Functionality + Reports
"""

import streamlit as st
import json
import os
import time
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
# ENHANCED CATEGORY & SUBCATEGORY STRUCTURE
# ============================================================================

CATEGORIES = {
    "🛒 Groceries": [
        "Vegetables (Sabzi)",
        "Fruits (Phal)",
        "Milk & Dairy (Doodh/Paneer/Dahi)",
        "Rice & Grains (Chawal/Gehu)",
        "Dal & Pulses (Dal/Chana)",
        "Cooking Oil & Ghee",
        "Spices & Masala",
        "Flour & Atta",
        "Bread & Bakery",
        "Eggs & Meat",
        "Fish & Seafood",
        "Snacks & Namkeen",
        "Biscuits & Cookies",
        "Tea & Coffee",
        "Sugar & Jaggery",
        "Dry Fruits",
        "Packaged Food",
        "Beverages & Soft Drinks",
        "Other Groceries"
    ],
    
    "💡 Utilities": [
        "Electricity Bill",
        "Water Bill",
        "Gas (LPG/PNG) Bill",
        "Internet/WiFi Bill",
        "Mobile Recharge",
        "Landline Bill",
        "DTH/Cable TV",
        "Newspaper/Magazine",
        "Society Maintenance",
        "Garbage Collection",
        "Other Utilities"
    ],
    
    "🏠 Housing & Rent": [
        "House Rent",
        "Society Maintenance",
        "Property Tax",
        "Home Insurance",
        "Repairs & Maintenance",
        "Plumbing Work",
        "Electrical Work",
        "Painting & Whitewash",
        "Pest Control",
        "Security Charges",
        "Parking Charges",
        "Other Housing"
    ],
    
    "🚗 Transportation": [
        "Petrol/Diesel",
        "CNG/Gas",
        "Auto Rickshaw",
        "Cab/Taxi (Ola/Uber)",
        "Bus Fare",
        "Metro/Train Fare",
        "Toll Charges",
        "Parking Fees",
        "Vehicle Service",
        "Vehicle Repair",
        "Tyre/Battery",
        "Vehicle Insurance",
        "Driving License/RC",
        "Fastag Recharge",
        "Other Transport"
    ],
    
    "🏥 Medical & Health": [
        "Doctor Consultation",
        "Medicines (Pharmacy)",
        "Lab Tests & Diagnostics",
        "Hospital Bills",
        "Health Insurance Premium",
        "Dental Treatment",
        "Eye Care/Spectacles",
        "Ayurvedic/Homeopathy",
        "Gym/Fitness Membership",
        "Yoga Classes",
        "Medical Equipment",
        "First Aid Supplies",
        "Vaccinations",
        "Physiotherapy",
        "Other Medical"
    ],
    
    "📚 Education": [
        "School Fees",
        "College Fees",
        "Tuition/Coaching Fees",
        "Books & Notebooks",
        "Stationery",
        "School Uniform",
        "School Bus/Transport",
        "Online Courses",
        "Certification Exams",
        "Computer Classes",
        "Music/Dance Classes",
        "Sports Coaching",
        "Educational Apps",
        "Library Fees",
        "Project Materials",
        "Other Education"
    ],
    
    "👕 Shopping & Clothing": [
        "Men's Clothing",
        "Women's Clothing",
        "Kids' Clothing",
        "Footwear/Shoes",
        "Jewellery",
        "Watches",
        "Bags & Wallets",
        "Cosmetics & Makeup",
        "Skincare Products",
        "Hair Care Products",
        "Perfumes & Deodorants",
        "Accessories",
        "Festival Shopping",
        "Wedding Shopping",
        "Other Shopping"
    ],
    
    "🎬 Entertainment": [
        "Movies (Theatre)",
        "OTT Subscriptions (Netflix/Prime/Hotstar)",
        "Music Subscriptions (Spotify/Gaana)",
        "Dining Out/Restaurant",
        "Food Delivery (Swiggy/Zomato)",
        "Cafe & Coffee",
        "Street Food",
        "Picnic/Outing",
        "Amusement Park",
        "Gaming",
        "Books & Magazines",
        "Hobbies",
        "Party & Celebration",
        "Other Entertainment"
    ],
    
    "✈️ Travel & Vacation": [
        "Flight Tickets",
        "Train Tickets (IRCTC)",
        "Bus Tickets",
        "Hotel/Accommodation",
        "Travel Insurance",
        "Visa Fees",
        "Passport Fees",
        "Tour Package",
        "Local Sightseeing",
        "Travel Food",
        "Travel Shopping",
        "Pilgrimage/Religious Travel",
        "Other Travel"
    ],
    
    "💳 EMI & Loans": [
        "Home Loan EMI",
        "Car Loan EMI",
        "Personal Loan EMI",
        "Education Loan EMI",
        "Credit Card Bill",
        "Credit Card EMI",
        "Gold Loan EMI",
        "Two-Wheeler Loan EMI",
        "Consumer Durable EMI",
        "Other Loan EMI"
    ],
    
    "📱 Electronics & Gadgets": [
        "Mobile Phone",
        "Laptop/Computer",
        "Tablet/iPad",
        "TV/Smart TV",
        "Refrigerator",
        "Washing Machine",
        "AC/Cooler",
        "Microwave/Oven",
        "Mixer/Grinder",
        "Water Purifier",
        "Geyser/Heater",
        "Fan/Cooler",
        "Camera",
        "Earphones/Headphones",
        "Smart Watch",
        "Other Electronics"
    ],
    
    "🏡 Home & Furniture": [
        "Furniture (Sofa/Bed/Table)",
        "Mattress & Bedding",
        "Curtains & Blinds",
        "Kitchen Utensils",
        "Cookware",
        "Crockery & Cutlery",
        "Home Decor",
        "Cleaning Supplies",
        "Detergent & Soap",
        "Room Freshener",
        "Storage & Organization",
        "Garden Supplies",
        "Light & Lamps",
        "Other Home Items"
    ],
    
    "👶 Kids & Baby": [
        "Baby Food & Formula",
        "Diapers",
        "Baby Clothes",
        "Baby Care Products",
        "Toys & Games",
        "School Supplies",
        "Kids Books",
        "Baby Furniture",
        "Stroller/Pram",
        "Kids Activities",
        "Birthday Party",
        "Other Kids Expenses"
    ],
    
    "🐕 Pets": [
        "Pet Food",
        "Pet Grooming",
        "Vet/Doctor Visits",
        "Pet Medicines",
        "Pet Accessories",
        "Pet Insurance",
        "Pet Boarding",
        "Other Pet Expenses"
    ],
    
    "💰 Investments & Savings": [
        "SIP/Mutual Funds",
        "Fixed Deposit",
        "Recurring Deposit",
        "PPF Contribution",
        "NPS Contribution",
        "LIC Premium",
        "Stock Purchase",
        "Gold Purchase",
        "Chit Fund",
        "Other Investments"
    ],
    
    "🎁 Gifts & Donations": [
        "Birthday Gifts",
        "Wedding Gifts",
        "Festival Gifts",
        "Charity/Donation",
        "Religious Donation",
        "Temple/Church Offering",
        "Tips & Gratuity",
        "Other Gifts"
    ],
    
    "👨‍👩‍👧‍👦 Family & Personal": [
        "Salon/Haircut",
        "Spa & Massage",
        "Parlour/Beauty",
        "Laundry/Dry Cleaning",
        "Tailoring/Alterations",
        "Marriage Expenses",
        "Funeral Expenses",
        "Family Function",
        "Pocket Money",
        "Personal Care",
        "Other Personal"
    ],
    
    "📋 Government & Taxes": [
        "Income Tax",
        "Property Tax",
        "Professional Tax",
        "GST Payment",
        "Stamp Duty",
        "Registration Fees",
        "Court Fees",
        "Fine/Penalty",
        "Other Government"
    ],
    
    "🔧 Services & Repairs": [
        "Maid/Domestic Help",
        "Cook Salary",
        "Driver Salary",
        "Watchman/Security",
        "Carpenter Work",
        "AC Service/Repair",
        "Appliance Repair",
        "Mobile Repair",
        "Computer Repair",
        "Other Services"
    ],
    
    "❓ Miscellaneous": [
        "ATM Withdrawal (Cash)",
        "Bank Charges",
        "Courier/Postage",
        "Photocopy/Printing",
        "Emergency Expense",
        "Lost/Stolen Items",
        "Uncategorized",
        "Other Expenses"
    ]
}

PAYMENT_MODES = [
    "Cash",
    "UPI (GPay/PhonePe/Paytm)",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Wallet (Paytm/Amazon)",
    "Cheque",
    "Bank Transfer (NEFT/IMPS)",
    "EMI",
    "Other"
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                return data
        except:
            return []
    return []


def save_expenses(expenses_list):
    """Save expenses to JSON file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses_list, file, indent=2)


def generate_unique_id():
    """Generate unique ID using timestamp"""
    return int(time.time() * 1000000)


def add_expense(expenses_list, date, category, subcategory, description, amount, payment_mode):
    """Add new expense"""
    new_expense = {
        'id': generate_unique_id(),
        'date': date,
        'category': category,
        'subcategory': subcategory,
        'description': description,
        'amount': amount,
        'payment_mode': payment_mode,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses_list.append(new_expense)
    return expenses_list


def update_expense(expenses_list, expense_id, date, category, subcategory, description, amount, payment_mode):
    """Update existing expense by ID"""
    for i in range(len(expenses_list)):
        if expenses_list[i]['id'] == expense_id:
            expenses_list[i]['date'] = date
            expenses_list[i]['category'] = category
            expenses_list[i]['subcategory'] = subcategory
            expenses_list[i]['description'] = description
            expenses_list[i]['amount'] = amount
            expenses_list[i]['payment_mode'] = payment_mode
            expenses_list[i]['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    return expenses_list


def delete_expense(expenses_list, expense_id):
    """Delete expense by ID"""
    new_list = []
    for expense in expenses_list:
        if expense['id'] != expense_id:
            new_list.append(expense)
    return new_list


def get_expense_by_id(expenses_list, expense_id):
    """Get single expense by ID"""
    for expense in expenses_list:
        if expense['id'] == expense_id:
            return expense
    return None


def calculate_total(expenses_list):
    """Calculate total"""
    total = 0
    for expense in expenses_list:
        total = total + expense['amount']
    return total


def calculate_average(expenses_list):
    """Calculate average"""
    if len(expenses_list) == 0:
        return 0
    total = calculate_total(expenses_list)
    average = total / len(expenses_list)
    return round(average, 2)


def find_max_expense(expenses_list):
    """Find maximum expense"""
    if len(expenses_list) == 0:
        return 0
    max_amount = 0
    for expense in expenses_list:
        if expense['amount'] > max_amount:
            max_amount = expense['amount']
    return max_amount


def find_min_expense(expenses_list):
    """Find minimum expense"""
    if len(expenses_list) == 0:
        return 0
    min_amount = expenses_list[0]['amount']
    for expense in expenses_list:
        if expense['amount'] < min_amount:
            min_amount = expense['amount']
    return min_amount


def filter_by_category(expenses_list, category):
    """Filter by category"""
    filtered_list = []
    for expense in expenses_list:
        if expense['category'] == category:
            filtered_list.append(expense)
    return filtered_list


def filter_by_payment_mode(expenses_list, payment_mode):
    """Filter by payment mode"""
    filtered_list = []
    for expense in expenses_list:
        if expense['payment_mode'] == payment_mode:
            filtered_list.append(expense)
    return filtered_list


def filter_today(expenses_list):
    """Filter today's expenses"""
    today = datetime.now().strftime('%Y-%m-%d')
    filtered_list = []
    for expense in expenses_list:
        if expense['date'] == today:
            filtered_list.append(expense)
    return filtered_list


def filter_this_week(expenses_list):
    """Filter this week's expenses"""
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
    """Filter this month's expenses"""
    today = datetime.now()
    month_start = today.replace(day=1).strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')
    
    filtered_list = []
    for expense in expenses_list:
        if month_start <= expense['date'] <= today_str:
            filtered_list.append(expense)
    return filtered_list


def filter_this_year(expenses_list):
    """Filter this year's expenses"""
    today = datetime.now()
    year_start = today.replace(month=1, day=1).strftime('%Y-%m-%d')
    today_str = today.strftime('%Y-%m-%d')
    
    filtered_list = []
    for expense in expenses_list:
        if year_start <= expense['date'] <= today_str:
            filtered_list.append(expense)
    return filtered_list


def filter_by_date_range(expenses_list, start_date, end_date):
    """Filter by date range"""
    filtered_list = []
    for expense in expenses_list:
        if start_date <= expense['date'] <= end_date:
            filtered_list.append(expense)
    return filtered_list


def get_category_wise_totals(expenses_list):
    """Calculate category-wise totals"""
    category_totals = {}
    
    for category in CATEGORIES.keys():
        category_totals[category] = 0
    
    for expense in expenses_list:
        category = expense['category']
        amount = expense['amount']
        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount
    
    return category_totals


def get_subcategory_wise_totals(expenses_list, category):
    """Calculate subcategory-wise totals"""
    subcategory_totals = {}
    
    if category in CATEGORIES:
        for subcategory in CATEGORIES[category]:
            subcategory_totals[subcategory] = 0
    
    for expense in expenses_list:
        if expense['category'] == category:
            subcategory = expense['subcategory']
            amount = expense['amount']
            if subcategory in subcategory_totals:
                subcategory_totals[subcategory] = subcategory_totals[subcategory] + amount
            else:
                subcategory_totals[subcategory] = amount
    
    return subcategory_totals


def get_payment_mode_totals(expenses_list):
    """Calculate payment mode-wise totals"""
    payment_totals = {}
    
    for mode in PAYMENT_MODES:
        payment_totals[mode] = 0
    
    for expense in expenses_list:
        mode = expense['payment_mode']
        amount = expense['amount']
        if mode in payment_totals:
            payment_totals[mode] = payment_totals[mode] + amount
        else:
            payment_totals[mode] = amount
    
    return payment_totals


def get_daily_totals(expenses_list):
    """Calculate daily totals"""
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
    """Calculate monthly totals"""
    monthly_totals = {}
    
    for expense in expenses_list:
        date_parts = expense['date'].split('-')
        year_month = date_parts[0] + '-' + date_parts[1]
        amount = expense['amount']
        
        if year_month in monthly_totals:
            monthly_totals[year_month] = monthly_totals[year_month] + amount
        else:
            monthly_totals[year_month] = amount
    
    return monthly_totals


def sort_expenses_by_date(expenses_list, ascending=True):
    """Sort by date using bubble sort"""
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
    """Sort by amount using bubble sort"""
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
    """Search expenses"""
    search_term_lower = search_term.lower()
    results = []
    
    for expense in expenses_list:
        description_lower = expense['description'].lower() if expense['description'] else ""
        category_lower = expense['category'].lower()
        subcategory_lower = expense['subcategory'].lower()
        
        if (search_term_lower in description_lower or 
            search_term_lower in category_lower or 
            search_term_lower in subcategory_lower):
            results.append(expense)
    
    return results


def generate_text_bar(value, max_value, bar_length=20):
    """Generate text-based bar"""
    if max_value == 0:
        return "░" * bar_length
    
    filled_length = int((value / max_value) * bar_length)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return bar


def export_to_csv_format(expenses_list):
    """Convert to CSV format"""
    csv_lines = []
    csv_lines.append("Date,Category,Subcategory,Description,Amount,Payment Mode")
    
    for expense in expenses_list:
        desc = expense['description'].replace(',', ';') if expense['description'] else ""
        line = f"{expense['date']},{expense['category']},{expense['subcategory']},{desc},{expense['amount']},{expense['payment_mode']}"
        csv_lines.append(line)
    
    csv_string = "\n".join(csv_lines)
    return csv_string


def get_top_expenses(expenses_list, n=5):
    """Get top N expenses"""
    sorted_list = sort_expenses_by_amount(expenses_list, ascending=False)
    return sorted_list[:n]


def generate_detailed_report(expenses_list, report_type="monthly"):
    """Generate detailed expense report"""
    report_lines = []
    
    # Header
    report_lines.append("=" * 60)
    report_lines.append("       GHAR KA KHATA - DETAILED EXPENSE REPORT")
    report_lines.append("=" * 60)
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"Report Type: {report_type.upper()}")
    report_lines.append("=" * 60)
    report_lines.append("")
    
    # Summary Section
    total = calculate_total(expenses_list)
    avg = calculate_average(expenses_list)
    max_exp = find_max_expense(expenses_list)
    min_exp = find_min_expense(expenses_list)
    count = len(expenses_list)
    
    report_lines.append("📊 SUMMARY")
    report_lines.append("-" * 40)
    report_lines.append(f"Total Expenses     : Rs. {total:,.2f}")
    report_lines.append(f"Total Transactions : {count}")
    report_lines.append(f"Average Expense    : Rs. {avg:,.2f}")
    report_lines.append(f"Highest Expense    : Rs. {max_exp:,.2f}")
    report_lines.append(f"Lowest Expense     : Rs. {min_exp:,.2f}")
    report_lines.append("")
    
    # Category-wise Breakdown
    report_lines.append("📁 CATEGORY-WISE BREAKDOWN")
    report_lines.append("-" * 40)
    
    category_totals = get_category_wise_totals(expenses_list)
    
    # Sort categories by amount
    sorted_cats = []
    for cat, amt in category_totals.items():
        if amt > 0:
            sorted_cats.append((cat, amt))
    
    for i in range(len(sorted_cats)):
        for j in range(i + 1, len(sorted_cats)):
            if sorted_cats[i][1] < sorted_cats[j][1]:
                sorted_cats[i], sorted_cats[j] = sorted_cats[j], sorted_cats[i]
    
    for cat, amt in sorted_cats:
        percentage = (amt / total * 100) if total > 0 else 0
        report_lines.append(f"{cat}")
        report_lines.append(f"    Amount: Rs. {amt:,.2f} ({percentage:.1f}%)")
    
    report_lines.append("")
    
    # Payment Mode Breakdown
    report_lines.append("💳 PAYMENT MODE BREAKDOWN")
    report_lines.append("-" * 40)
    
    payment_totals = get_payment_mode_totals(expenses_list)
    for mode, amt in payment_totals.items():
        if amt > 0:
            percentage = (amt / total * 100) if total > 0 else 0
            report_lines.append(f"{mode}: Rs. {amt:,.2f} ({percentage:.1f}%)")
    
    report_lines.append("")
    
    # Monthly Breakdown
    report_lines.append("📅 MONTHLY BREAKDOWN")
    report_lines.append("-" * 40)
    
    monthly_totals = get_monthly_totals(expenses_list)
    sorted_months = sorted(monthly_totals.keys())
    
    for month in sorted_months:
        amt = monthly_totals[month]
        report_lines.append(f"{month}: Rs. {amt:,.2f}")
    
    report_lines.append("")
    
    # Top 10 Expenses
    report_lines.append("🔝 TOP 10 HIGHEST EXPENSES")
    report_lines.append("-" * 40)
    
    top_expenses = get_top_expenses(expenses_list, 10)
    for i, expense in enumerate(top_expenses):
        report_lines.append(f"{i+1}. Rs. {expense['amount']:,.2f}")
        report_lines.append(f"   {expense['category']} → {expense['subcategory']}")
        report_lines.append(f"   Date: {expense['date']} | {expense['payment_mode']}")
        if expense['description']:
            report_lines.append(f"   Note: {expense['description']}")
        report_lines.append("")
    
    # Transaction Details
    report_lines.append("📋 ALL TRANSACTIONS")
    report_lines.append("-" * 40)
    
    sorted_expenses = sort_expenses_by_date(expenses_list, ascending=False)
    for i, expense in enumerate(sorted_expenses):
        report_lines.append(f"{i+1}. {expense['date']} | Rs. {expense['amount']:,.2f}")
        report_lines.append(f"   {expense['category']} → {expense['subcategory']}")
        report_lines.append(f"   Payment: {expense['payment_mode']}")
        if expense['description']:
            report_lines.append(f"   Note: {expense['description']}")
        report_lines.append("")
    
    # Footer
    report_lines.append("=" * 60)
    report_lines.append("         End of Report - Ghar Ka Khata v3.0")
    report_lines.append("=" * 60)
    
    return "\n".join(report_lines)


# ============================================================================
# STREAMLIT DASHBOARD
# ============================================================================

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = load_expenses()

if 'edit_expense_id' not in st.session_state:
    st.session_state.edit_expense_id = None

if 'show_edit_form' not in st.session_state:
    st.session_state.show_edit_form = False

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
    .edit-box {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #ffc107;
        margin: 1rem 0;
    }
    .success-msg {
        background: #d4edda;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 📊 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Dashboard", "➕ Add Expense", "📋 View & Edit Expenses", "📈 Analytics", "📊 Reports", "📥 Export Data"],
    key="nav_radio"
)

# Show total in sidebar
total_all = calculate_total(st.session_state.expenses)
st.sidebar.markdown("---")
st.sidebar.markdown(f"### 💰 Total Expenses")
st.sidebar.markdown(f"## ₹{total_all:,.2f}")
st.sidebar.markdown(f"📝 {len(st.session_state.expenses)} transactions")

# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================

if page == "🏠 Dashboard":
    st.markdown('<h1 class="main-header">💰 Ghar Ka Khata</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Household Expense Tracker v3.0</p>', unsafe_allow_html=True)
    
    # Period selector
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        period = st.selectbox(
            "📅 Select Period", 
            ["Today", "This Week", "This Month", "This Year", "All Time"], 
            key="dashboard_period"
        )
    
    # Filter data
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
        st.metric("💵 Total", f"₹{total:,.2f}")
    with col2:
        st.metric("📝 Count", count)
    with col3:
        st.metric("📊 Average", f"₹{avg:,.2f}")
    with col4:
        st.metric("🔝 Highest", f"₹{max_exp:,.2f}")
    
    # Category Breakdown
    st.markdown("---")
    if len(filtered_expenses) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Top Categories")
            category_totals = get_category_wise_totals(filtered_expenses)
            
            max_cat_amt = 0
            for cat, amt in category_totals.items():
                if amt > max_cat_amt:
                    max_cat_amt = amt
            
            # Sort and show top 5
            sorted_cats = [(cat, amt) for cat, amt in category_totals.items() if amt > 0]
            for i in range(len(sorted_cats)):
                for j in range(i + 1, len(sorted_cats)):
                    if sorted_cats[i][1] < sorted_cats[j][1]:
                        sorted_cats[i], sorted_cats[j] = sorted_cats[j], sorted_cats[i]
            
            for cat, amt in sorted_cats[:5]:
                bar = generate_text_bar(amt, max_cat_amt, 12)
                pct = (amt / total * 100) if total > 0 else 0
                st.markdown(f"**{cat}**")
                st.markdown(f"`{bar}` ₹{amt:,.0f} ({pct:.0f}%)")
        
        with col2:
            st.subheader("📋 Recent Expenses")
            sorted_exp = sort_expenses_by_date(filtered_expenses, ascending=False)
            for exp in sorted_exp[:5]:
                st.markdown(f"**{exp['date']}** - ₹{exp['amount']:,.0f}")
                st.markdown(f"_{exp['subcategory']}_")
                st.markdown("---")
    else:
        st.info("No expenses for this period. Add some expenses to get started!")

# ============================================================================
# PAGE 2: ADD EXPENSE (with Dynamic Subcategory)
# ============================================================================

elif page == "➕ Add Expense":
    st.markdown('<h1 class="main-header">➕ Add New Expense</h1>', unsafe_allow_html=True)
    
    # IMPORTANT: Use callback to handle dynamic subcategory
    # Category selection OUTSIDE form for dynamic update
    st.subheader("Select Category First")
    
    selected_category = st.selectbox(
        "📁 Category",
        list(CATEGORIES.keys()),
        key="add_category_select"
    )
    
    # Get subcategories for selected category
    subcategory_options = CATEGORIES[selected_category]
    
    st.markdown("---")
    st.subheader("Fill Expense Details")
    
    # Form for other details
    with st.form("expense_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            expense_date = st.date_input(
                "📅 Date", 
                datetime.now(), 
                key="add_expense_date"
            )
            
            # Subcategory dropdown - now shows correct options based on selected category
            subcategory = st.selectbox(
                "📂 Subcategory", 
                subcategory_options, 
                key="add_expense_subcategory"
            )
            
            description = st.text_input(
                "📝 Description (Optional)", 
                "", 
                placeholder="E.g., Monthly grocery from Big Bazaar",
                key="add_expense_description"
            )
        
        with col2:
            amount = st.number_input(
                "💰 Amount (₹)", 
                min_value=0.0, 
                step=10.0, 
                format="%.2f",
                key="add_expense_amount"
            )
            
            payment_mode = st.selectbox(
                "💳 Payment Mode", 
                PAYMENT_MODES, 
                key="add_expense_payment"
            )
        
        # Show selected category in form
        st.info(f"**Selected Category:** {selected_category}")
        
        submitted = st.form_submit_button("💾 Save Expense", use_container_width=True)
        
        if submitted:
            if amount > 0:
                date_str = expense_date.strftime('%Y-%m-%d')
                st.session_state.expenses = add_expense(
                    st.session_state.expenses,
                    date_str,
                    selected_category,  # Use the category selected outside form
                    subcategory,
                    description,
                    amount,
                    payment_mode
                )
                save_expenses(st.session_state.expenses)
                st.success(f"✅ Expense of ₹{amount:,.2f} added to {selected_category} → {subcategory}")
                st.balloons()
            else:
                st.error("❌ Please enter amount greater than 0!")
    
    # Quick Add
    st.markdown("---")
    st.subheader("⚡ Quick Add")
    
    quick_items = [
        ("🥛 Milk ₹60", "🛒 Groceries", "Milk & Dairy (Doodh/Paneer/Dahi)", "Milk", 60),
        ("🥬 Sabzi ₹150", "🛒 Groceries", "Vegetables (Sabzi)", "Vegetables", 150),
        ("⛽ Petrol ₹500", "🚗 Transportation", "Petrol/Diesel", "Petrol", 500),
        ("📱 Recharge ₹299", "💡 Utilities", "Mobile Recharge", "Recharge", 299),
    ]
    
    cols = st.columns(4)
    for i, item in enumerate(quick_items):
        with cols[i]:
            if st.button(item[0], key=f"quick_{i}", use_container_width=True):
                today_str = datetime.now().strftime('%Y-%m-%d')
                st.session_state.expenses = add_expense(
                    st.session_state.expenses,
                    today_str,
                    item[1], item[2], item[3], item[4],
                    "Cash"
                )
                save_expenses(st.session_state.expenses)
                st.success(f"✅ {item[3]} added!")
                st.rerun()

# ============================================================================
# PAGE 3: VIEW & EDIT EXPENSES
# ============================================================================

elif page == "📋 View & Edit Expenses":
    st.markdown('<h1 class="main-header">📋 View & Edit Expenses</h1>', unsafe_allow_html=True)
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_cat = st.selectbox("Filter Category", ["All"] + list(CATEGORIES.keys()), key="view_filter_cat")
    with col2:
        sort_by = st.selectbox("Sort By", ["Date (Newest)", "Date (Oldest)", "Amount (High)", "Amount (Low)"], key="view_sort")
    with col3:
        search_term = st.text_input("🔍 Search", "", key="view_search")
    
    # Apply filters
    display_expenses = st.session_state.expenses.copy()
    
    if filter_cat != "All":
        display_expenses = filter_by_category(display_expenses, filter_cat)
    
    if search_term:
        display_expenses = search_expenses(display_expenses, search_term)
    
    # Apply sorting
    if sort_by == "Date (Newest)":
        display_expenses = sort_expenses_by_date(display_expenses, ascending=False)
    elif sort_by == "Date (Oldest)":
        display_expenses = sort_expenses_by_date(display_expenses, ascending=True)
    elif sort_by == "Amount (High)":
        display_expenses = sort_expenses_by_amount(display_expenses, ascending=False)
    else:
        display_expenses = sort_expenses_by_amount(display_expenses, ascending=True)
    
    # Summary
    total_filtered = calculate_total(display_expenses)
    st.markdown(f"**Showing {len(display_expenses)} expenses | Total: ₹{total_filtered:,.2f}**")
    st.markdown("---")
    
    # Check if editing
    if st.session_state.show_edit_form and st.session_state.edit_expense_id:
        expense_to_edit = get_expense_by_id(st.session_state.expenses, st.session_state.edit_expense_id)
        
        if expense_to_edit:
            st.markdown("### ✏️ Edit Expense")
            st.markdown('<div class="edit-box">', unsafe_allow_html=True)
            
            # Category selection for edit (outside form for dynamic subcategory)
            edit_category = st.selectbox(
                "📁 Category",
                list(CATEGORIES.keys()),
                index=list(CATEGORIES.keys()).index(expense_to_edit['category']) if expense_to_edit['category'] in CATEGORIES else 0,
                key="edit_category_select"
            )
            
            # Get subcategories for selected category
            edit_subcategory_options = CATEGORIES[edit_category]
            
            with st.form("edit_expense_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    edit_date = st.date_input(
                        "📅 Date",
                        datetime.strptime(expense_to_edit['date'], '%Y-%m-%d'),
                        key="edit_date"
                    )
                    
                    # Find subcategory index
                    subcat_idx = 0
                    if expense_to_edit['subcategory'] in edit_subcategory_options:
                        subcat_idx = edit_subcategory_options.index(expense_to_edit['subcategory'])
                    
                    edit_subcategory = st.selectbox(
                        "📂 Subcategory",
                        edit_subcategory_options,
                        index=subcat_idx,
                        key="edit_subcategory"
                    )
                    
                    edit_description = st.text_input(
                        "📝 Description",
                        expense_to_edit['description'] or "",
                        key="edit_description"
                    )
                
                with col2:
                    edit_amount = st.number_input(
                        "💰 Amount (₹)",
                        min_value=0.0,
                        value=float(expense_to_edit['amount']),
                        step=10.0,
                        key="edit_amount"
                    )
                    
                    pay_idx = 0
                    if expense_to_edit['payment_mode'] in PAYMENT_MODES:
                        pay_idx = PAYMENT_MODES.index(expense_to_edit['payment_mode'])
                    
                    edit_payment = st.selectbox(
                        "💳 Payment Mode",
                        PAYMENT_MODES,
                        index=pay_idx,
                        key="edit_payment"
                    )
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    save_btn = st.form_submit_button("💾 Save Changes", use_container_width=True)
                with col2:
                    cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
                
                if save_btn:
                    if edit_amount > 0:
                        st.session_state.expenses = update_expense(
                            st.session_state.expenses,
                            st.session_state.edit_expense_id,
                            edit_date.strftime('%Y-%m-%d'),
                            edit_category,
                            edit_subcategory,
                            edit_description,
                            edit_amount,
                            edit_payment
                        )
                        save_expenses(st.session_state.expenses)
                        st.session_state.show_edit_form = False
                        st.session_state.edit_expense_id = None
                        st.success("✅ Expense updated successfully!")
                        st.rerun()
                    else:
                        st.error("Amount must be greater than 0!")
                
                if cancel_btn:
                    st.session_state.show_edit_form = False
                    st.session_state.edit_expense_id = None
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
    
    # Display expenses table
    if len(display_expenses) > 0:
        for i, expense in enumerate(display_expenses):
            col1, col2, col3, col4, col5 = st.columns([2, 3, 2, 1, 1])
            
            with col1:
                st.write(f"**{expense['date']}**")
                st.write(f"₹{expense['amount']:,.2f}")
            
            with col2:
                cat_short = expense['category'][:20]
                subcat_short = expense['subcategory'][:25]
                st.write(f"**{cat_short}**")
                st.write(f"_{subcat_short}_")
            
            with col3:
                st.write(expense['payment_mode'][:15])
                if expense['description']:
                    st.write(f"_{expense['description'][:20]}_")
            
            with col4:
                if st.button("✏️", key=f"edit_{i}_{expense['id']}"):
                    st.session_state.edit_expense_id = expense['id']
                    st.session_state.show_edit_form = True
                    st.rerun()
            
            with col5:
                if st.button("🗑️", key=f"del_{i}_{expense['id']}"):
                    st.session_state.expenses = delete_expense(st.session_state.expenses, expense['id'])
                    save_expenses(st.session_state.expenses)
                    st.rerun()
            
            st.markdown("---")
    else:
        st.info("No expenses found.")

# ============================================================================
# PAGE 4: ANALYTICS
# ============================================================================

elif page == "📈 Analytics":
    st.markdown('<h1 class="main-header">📈 Analytics</h1>', unsafe_allow_html=True)
    
    if len(st.session_state.expenses) > 0:
        # Monthly Summary
        st.subheader("📅 Monthly Summary")
        monthly_totals = get_monthly_totals(st.session_state.expenses)
        
        max_monthly = max(monthly_totals.values()) if monthly_totals else 0
        
        for month in sorted(monthly_totals.keys()):
            amt = monthly_totals[month]
            bar = generate_text_bar(amt, max_monthly, 25)
            st.markdown(f"**{month}**: `{bar}` ₹{amt:,.2f}")
        
        st.markdown("---")
        
        # Category Analysis
        st.subheader("🔍 Category Analysis")
        selected_cat = st.selectbox("Select Category", list(CATEGORIES.keys()), key="analytics_cat")
        
        cat_expenses = filter_by_category(st.session_state.expenses, selected_cat)
        
        if cat_expenses:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"**Total:** ₹{calculate_total(cat_expenses):,.2f}")
                st.markdown(f"**Count:** {len(cat_expenses)}")
                st.markdown(f"**Average:** ₹{calculate_average(cat_expenses):,.2f}")
            
            with col2:
                st.markdown("**Subcategory Breakdown:**")
                subcat_totals = get_subcategory_wise_totals(st.session_state.expenses, selected_cat)
                
                for subcat, amt in subcat_totals.items():
                    if amt > 0:
                        st.markdown(f"- {subcat}: ₹{amt:,.2f}")
        else:
            st.info(f"No expenses in {selected_cat}")
        
        st.markdown("---")
        
        # Top Expenses
        st.subheader("🔝 Top 5 Expenses")
        top_5 = get_top_expenses(st.session_state.expenses, 5)
        
        for i, exp in enumerate(top_5):
            st.markdown(f"**{i+1}.** ₹{exp['amount']:,.2f} - {exp['subcategory']} ({exp['date']})")
    else:
        st.info("Add expenses to see analytics!")

# ============================================================================
# PAGE 5: REPORTS
# ============================================================================

elif page == "📊 Reports":
    st.markdown('<h1 class="main-header">📊 Generate Reports</h1>', unsafe_allow_html=True)
    
    if len(st.session_state.expenses) > 0:
        st.subheader("📅 Select Report Period")
        
        col1, col2 = st.columns(2)
        
        with col1:
            report_type = st.selectbox(
                "Report Type",
                ["All Time", "This Month", "This Year", "Custom Date Range"],
                key="report_type"
            )
        
        with col2:
            if report_type == "Custom Date Range":
                date_range = st.date_input(
                    "Select Date Range",
                    [datetime.now() - timedelta(days=30), datetime.now()],
                    key="report_date_range"
                )
        
        # Filter based on report type
        if report_type == "This Month":
            report_expenses = filter_this_month(st.session_state.expenses)
        elif report_type == "This Year":
            report_expenses = filter_this_year(st.session_state.expenses)
        elif report_type == "Custom Date Range" and len(date_range) == 2:
            start_str = date_range[0].strftime('%Y-%m-%d')
            end_str = date_range[1].strftime('%Y-%m-%d')
            report_expenses = filter_by_date_range(st.session_state.expenses, start_str, end_str)
        else:
            report_expenses = st.session_state.expenses
        
        st.markdown("---")
        
        # Report Preview
        st.subheader("📋 Report Preview")
        
        total = calculate_total(report_expenses)
        count = len(report_expenses)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Expenses", f"₹{total:,.2f}")
        col2.metric("Transactions", count)
        col3.metric("Average", f"₹{calculate_average(report_expenses):,.2f}")
        
        # Category Summary
        st.markdown("**Category Summary:**")
        cat_totals = get_category_wise_totals(report_expenses)
        
        for cat, amt in cat_totals.items():
            if amt > 0:
                pct = (amt / total * 100) if total > 0 else 0
                st.markdown(f"- {cat}: ₹{amt:,.2f} ({pct:.1f}%)")
        
        st.markdown("---")
        
        # Download Report
        st.subheader("📥 Download Report")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Detailed Text Report
            detailed_report = generate_detailed_report(report_expenses, report_type)
            st.download_button(
                "📄 Download Detailed Report",
                detailed_report,
                f"expense_report_{datetime.now().strftime('%Y%m%d')}.txt",
                "text/plain",
                use_container_width=True,
                key="download_detailed"
            )
        
        with col2:
            # CSV Report
            csv_data = export_to_csv_format(report_expenses)
            st.download_button(
                "📊 Download CSV",
                csv_data,
                f"expenses_{datetime.now().strftime('%Y%m%d')}.csv",
                "text/csv",
                use_container_width=True,
                key="download_csv_report"
            )
        
        with col3:
            # JSON Report
            json_data = json.dumps(report_expenses, indent=2, ensure_ascii=False)
            st.download_button(
                "📋 Download JSON",
                json_data,
                f"expenses_{datetime.now().strftime('%Y%m%d')}.json",
                "application/json",
                use_container_width=True,
                key="download_json_report"
            )
    else:
        st.info("Add expenses to generate reports!")

# ============================================================================
# PAGE 6: EXPORT DATA
# ============================================================================

elif page == "📥 Export Data":
    st.markdown('<h1 class="main-header">📥 Export & Manage Data</h1>', unsafe_allow_html=True)
    
    if len(st.session_state.expenses) > 0:
        st.subheader("📋 Data Overview")
        st.markdown(f"**Total Records:** {len(st.session_state.expenses)}")
        st.markdown(f"**Total Amount:** ₹{calculate_total(st.session_state.expenses):,.2f}")
        
        st.markdown("---")
        
        # Quick Export
        st.subheader("📤 Quick Export")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            csv_data = export_to_csv_format(st.session_state.expenses)
            st.download_button(
                "📄 Export as CSV",
                csv_data,
                f"all_expenses_{datetime.now().strftime('%Y%m%d')}.csv",
                "text/csv",
                use_container_width=True,
                key="export_csv"
            )
        
        with col2:
            json_data = json.dumps(st.session_state.expenses, indent=2, ensure_ascii=False)
            st.download_button(
                "📋 Export as JSON",
                json_data,
                f"all_expenses_{datetime.now().strftime('%Y%m%d')}.json",
                "application/json",
                use_container_width=True,
                key="export_json"
            )
        
        with col3:
            full_report = generate_detailed_report(st.session_state.expenses, "All Time")
            st.download_button(
                "📊 Full Report",
                full_report,
                f"full_report_{datetime.now().strftime('%Y%m%d')}.txt",
                "text/plain",
                use_container_width=True,
                key="export_report"
            )
        
        st.markdown("---")
        
        # Danger Zone
        st.subheader("⚠️ Danger Zone")
        st.warning("These actions cannot be undone!")
        
        if st.button("🗑️ Delete All Data", key="delete_all"):
            st.session_state.confirm_delete = True
        
        if 'confirm_delete' in st.session_state and st.session_state.confirm_delete:
            st.error("Are you sure you want to delete ALL expenses?")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("✅ Yes, Delete Everything", key="confirm_yes"):
                    st.session_state.expenses = []
                    save_expenses([])
                    st.session_state.confirm_delete = False
                    st.success("All data deleted!")
                    st.rerun()
            
            with col2:
                if st.button("❌ Cancel", key="confirm_no"):
                    st.session_state.confirm_delete = False
                    st.rerun()
    else:
        st.info("No data to export. Start by adding expenses!")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#888;">💰 Ghar Ka Khata v3.0 - Dynamic Categories | Edit & Delete | Reports</p>',
    unsafe_allow_html=True
)
