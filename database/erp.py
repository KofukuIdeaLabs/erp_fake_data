import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# User Management
def create_users():
    users = pd.DataFrame({
        'user_id': range(1, 101),
        'first_name': [fake.first_name() for _ in range(100)],
        'last_name': [fake.last_name() for _ in range(100)],
        'email': [fake.email() for _ in range(100)],
        'password_hash': [fake.sha256() for _ in range(100)],
        'phone_number': [fake.phone_number()[:15] for _ in range(100)],
        'created_at': [fake.date_time_this_year() for _ in range(100)]
    })
    return users

def create_user_addresses():
    addresses = pd.DataFrame({
        'address_id': range(1, 151),
        'user_id': np.random.randint(1, 101, 150),
        'address_line1': [fake.street_address() for _ in range(150)],
        'address_line2': [fake.secondary_address() if random.random() > 0.5 else None for _ in range(150)],
        'city': [fake.city() for _ in range(150)],
        'state': [fake.state() for _ in range(150)],
        'country': [fake.country() for _ in range(150)],
        'postal_code': [fake.postcode() for _ in range(150)],
        'is_default': np.random.choice([True, False], 150)
    })
    return addresses

# Product Management
def create_categories():
    categories = pd.DataFrame({
        'category_id': range(1, 21),
        'category_name': [f"Category {i}" for i in range(1, 21)],
        'parent_category_id': [None if i < 5 else np.random.randint(1, 5) for i in range(1, 21)]
    })
    return categories

def create_products():
    products = pd.DataFrame({
        'product_id': range(1, 201),
        'name': [fake.catch_phrase() for _ in range(200)],
        'description': [fake.text(max_nb_chars=200) for _ in range(200)],
        'price': np.random.uniform(10, 1000, 200).round(2),
        'category_id': np.random.randint(1, 21, 200),
        'created_at': [fake.date_time_this_year() for _ in range(200)]
    })
    return products

def create_product_variants():
    variants = pd.DataFrame({
        'variant_id': range(1, 301),
        'product_id': np.random.randint(1, 201, 300),
        'variant_name': [f"Variant {fake.word()}" for _ in range(300)],
        'price': np.random.uniform(10, 1000, 300).round(2),
        'stock_quantity': np.random.randint(0, 1000, 300)
    })
    return variants

# Inventory Management
def create_inventory():
    inventory = pd.DataFrame({
        'inventory_id': range(1, 201),
        'product_id': range(1, 201),
        'warehouse_location': np.random.choice(['North', 'South', 'East', 'West', 'Central'], 200),
        'stock_quantity': np.random.randint(0, 1000, 200)
    })
    return inventory

# Order Management
def create_orders():
    orders = pd.DataFrame({
        'order_id': range(1, 501),
        'user_id': np.random.randint(1, 101, 500),
        'total_amount': np.random.uniform(50, 5000, 500).round(2),
        'status': np.random.choice(['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled'], 500),
        'created_at': [fake.date_time_this_year() for _ in range(500)]
    })
    return orders

def create_order_items():
    items = pd.DataFrame({
        'order_item_id': range(1, 1001),
        'order_id': np.random.randint(1, 501, 1000),
        'product_id': np.random.randint(1, 201, 1000),
        'quantity': np.random.randint(1, 10, 1000),
        'price': np.random.uniform(10, 1000, 1000).round(2)
    })
    return items

# Payment Management
def create_payments():
    payments = pd.DataFrame({
        'payment_id': range(1, 501),
        'order_id': range(1, 501),
        'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'PayPal'], 500),
        'amount': np.random.uniform(50, 5000, 500).round(2),
        'status': np.random.choice(['Pending', 'Completed', 'Failed', 'Refunded'], 500),
        'created_at': [fake.date_time_this_year() for _ in range(500)]
    })
    return payments

# Additional Tables
def create_currencies():
    currencies = pd.DataFrame({
        'currency_code': ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CNY', 'INR'],
        'exchange_rate': np.random.uniform(0.5, 2.0, 8).round(5),
        'last_updated': [fake.date_time_this_month() for _ in range(8)]
    })
    return currencies

def create_product_pricing():
    pricing = pd.DataFrame({
        'pricing_id': range(1, 1001),
        'product_id': np.random.randint(1, 201, 1000),
        'currency_code': np.random.choice(['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CNY', 'INR'], 1000),
        'price': np.random.uniform(10, 1000, 1000).round(2)
    })
    return pricing

def create_shipping_details(num_records=1000):
    """Generate shipping details data"""
    shipping_statuses = ['Pending', 'Shipped', 'In Transit', 'Delivered', 'Returned']
    carriers = ['FedEx', 'UPS', 'DHL', 'USPS', 'Amazon Logistics', 'OnTrac']
    
    shipping_data = pd.DataFrame({
        'order_id': np.random.randint(1, 501, num_records),  # Assuming 500 orders exist
        'address_id': np.random.randint(1, 151, num_records),  # Assuming 150 addresses exist
        'shipping_status': np.random.choice(shipping_statuses, num_records),
        'tracking_number': [fake.uuid4()[:10].upper() for _ in range(num_records)],
        'carrier_name': np.random.choice(carriers, num_records)
    })
    return shipping_data

def create_reviews(num_records=2000):
    """Generate product reviews data"""
    reviews = pd.DataFrame({
        'product_id': np.random.randint(1, 201, num_records),  # Assuming 200 products exist
        'user_id': np.random.randint(1, 101, num_records),    # Assuming 100 users exist
        'rating': np.random.randint(1, 6, num_records),
        'review_text': [fake.paragraph() for _ in range(num_records)],
        'created_at': [fake.date_time_this_year() for _ in range(num_records)]
    })
    return reviews

def create_coupons(num_records=50):
    """Generate coupons data"""
    coupons = pd.DataFrame({
        'code': [fake.unique.bothify(text='????##').upper() for _ in range(num_records)],
        'discount_percentage': np.random.uniform(5, 50, num_records).round(2),
        'start_date': [fake.date_this_year() for _ in range(num_records)],
        'end_date': [fake.date_between(start_date='+30d', end_date='+90d') for _ in range(num_records)],
        'max_usage': np.random.randint(50, 1000, num_records),
        'usage_count': [0] * num_records
    })
    return coupons

def create_vendors(num_records=50):
    """Generate vendors data"""
    vendors = pd.DataFrame({
        'name': [fake.company() for _ in range(num_records)],
        'email': [fake.company_email() for _ in range(num_records)],
        'phone_number': [fake.phone_number()[:15] for _ in range(num_records)],
        'address': [fake.address() for _ in range(num_records)],
        'created_at': [fake.date_time_this_year() for _ in range(num_records)]
    })
    return vendors

def create_vendor_products(num_records=200):
    """Generate vendor products data"""
    vendor_products = pd.DataFrame({
        'vendor_id': np.random.randint(1, 51, num_records),  # Assuming 50 vendors exist
        'product_id': np.random.randint(1, 201, num_records),  # Assuming 200 products exist
        'stock_quantity': np.random.randint(0, 1000, num_records)
    })
    return vendor_products

def create_warehouses(num_records=10):
    """Generate warehouses data"""
    warehouses = pd.DataFrame({
        'name': [f"Warehouse {fake.city()}" for _ in range(num_records)],
        'location': [fake.address() for _ in range(num_records)],
        'capacity': np.random.randint(5000, 50000, num_records)
    })
    return warehouses

def create_delivery_partners(num_records=20):
    """Generate delivery partners data"""
    partners = pd.DataFrame({
        'name': [fake.company() for _ in range(num_records)],
        'contact_email': [fake.company_email() for _ in range(num_records)],
        'contact_phone': [fake.phone_number()[:15] for _ in range(num_records)]
    })
    return partners

def create_product_views(num_records=5000):
    """Generate product views data"""
    views = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users exist
        'product_id': np.random.randint(1, 201, num_records),  # Assuming 200 products exist
        'view_date': [fake.date_time_this_month() for _ in range(num_records)]
    })
    return views

def create_search_history(num_records=1000):
    """Generate search history data"""
    search_terms = ['shoes', 'laptop', 'phone', 'watch', 'headphones', 'camera', 'tablet', 
                   'printer', 'monitor', 'keyboard', 'mouse', 'speaker', 'dress', 'jacket']
    
    searches = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users exist
        'search_query': [f"{np.random.choice(search_terms)} {fake.word()}" for _ in range(num_records)],
        'search_date': [fake.date_time_this_month() for _ in range(num_records)]
    })
    return searches

def create_abandoned_carts(num_records=500):
    """Generate abandoned carts data"""
    carts = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users exist
        'product_id': np.random.randint(1, 201, num_records),  # Assuming 200 products exist
        'quantity': np.random.randint(1, 5, num_records),
        'added_date': [fake.date_time_this_month() for _ in range(num_records)]
    })
    return carts

def create_sales_reports(num_records=200):
    """Generate sales reports data"""
    reports = pd.DataFrame({
        'product_id': range(1, num_records + 1),  # One report per product
        'sales_date': [fake.date_this_month() for _ in range(num_records)],
        'total_quantity_sold': np.random.randint(0, 1000, num_records),
        'total_revenue': np.random.uniform(0, 50000, num_records).round(2)
    })
    return reports

def create_reward_programs(num_records=10):
    """Generate reward programs data"""
    programs = pd.DataFrame({
        'program_name': [f"{fake.company()} Rewards {fake.word().title()}" for _ in range(num_records)],
        'description': [fake.text(max_nb_chars=200) for _ in range(num_records)],
        'start_date': [fake.date_this_year() for _ in range(num_records)],
        'end_date': [fake.date_between(start_date='+3m', end_date='+2y') for _ in range(num_records)],
        'points_multiplier': np.random.uniform(1.0, 5.0, num_records).round(2)
    })
    return programs

def create_user_rewards(num_records=1000):
    """Generate user rewards data"""
    rewards = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users
        'program_id': np.random.randint(1, 11, num_records),  # Assuming 10 reward programs
        'points_earned': np.random.randint(0, 10000, num_records),
        'points_redeemed': [min(np.random.randint(0, points+1), points) for points in np.random.randint(0, 10000, num_records)]
    })
    return rewards

def create_risk_scores(num_records=500):
    """Generate risk scores data"""
    risk_scores = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users
        'order_id': np.random.randint(1, 501, num_records),  # Assuming 500 orders
        'risk_score': np.random.uniform(0, 100, num_records).round(2),
        'generated_at': [fake.date_time_this_year() for _ in range(num_records)]
    })
    return risk_scores

def create_subscription_plans(num_records=5):
    """Generate subscription plans data"""
    plan_names = ['Basic', 'Premium', 'Pro', 'Enterprise', 'Ultimate']
    billing_cycles = ['Monthly', 'Yearly']
    
    plans = pd.DataFrame({
        'plan_name': plan_names[:num_records],
        'description': [fake.text(max_nb_chars=200) for _ in range(num_records)],
        'price': np.random.uniform(9.99, 299.99, num_records).round(2),
        'billing_cycle': np.random.choice(billing_cycles, num_records),
        'created_at': [fake.date_time_this_year() for _ in range(num_records)]
    })
    return plans

def create_subscriptions(num_records=200):
    """Generate subscriptions data"""
    statuses = ['Active', 'Cancelled', 'Expired']
    
    subscriptions = pd.DataFrame({
        'user_id': np.random.randint(1, 101, num_records),  # Assuming 100 users
        'plan_id': np.random.randint(1, 6, num_records),    # Assuming 5 subscription plans
        'start_date': [fake.date_this_year() for _ in range(num_records)],
        'end_date': [fake.date_between(start_date='+1m', end_date='+1y') if random.random() > 0.7 else None 
                    for _ in range(num_records)],
        'status': np.random.choice(statuses, num_records, p=[0.7, 0.2, 0.1])  # Weighted probabilities
    })
    return subscriptions

def create_tax_rules(num_records=50):
    """Generate tax rules data"""
    regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 
              'Australia', 'Middle East'] + [fake.country() for _ in range(43)]
    
    tax_rules = pd.DataFrame({
        'category_id': np.random.randint(1, 21, num_records),  # Assuming 20 categories
        'region': np.random.choice(regions, num_records, replace=False),
        'tax_rate': np.random.uniform(0, 25, num_records).round(2)  # Tax rates between 0% and 25%
    })
    return tax_rules

def create_invoice_history(num_records=500):
    """Generate invoice history data"""
    # Generate base amounts
    base_amounts = np.random.uniform(50, 5000, num_records).round(2)
    # Calculate tax amounts (between 5% and 20% of base amount)
    tax_rates = np.random.uniform(0.05, 0.20, num_records)
    tax_amounts = (base_amounts * tax_rates).round(2)
    
    invoices = pd.DataFrame({
        'order_id': np.random.randint(1, 501, num_records),  # Assuming 500 orders
        'total_amount': base_amounts + tax_amounts,
        'tax_amount': tax_amounts,
        'issued_at': [fake.date_time_this_year() for _ in range(num_records)]
    })
    return invoices

# Example usage
def print_sample_data():
    """Print sample data from each table in a more readable format"""
    tables = {
        'Users': create_users(),
        'User Addresses': create_user_addresses(),
        'Categories': create_categories(),
        'Products': create_products(),
        'Product Variants': create_product_variants(),
        'Inventory': create_inventory(),
        'Orders': create_orders(),
        'Order Items': create_order_items(),
        'Payments': create_payments(),
        'Currencies': create_currencies(),
        'Product Pricing': create_product_pricing(),
        'Shipping Details': create_shipping_details(),
        'Reviews': create_reviews(),
        'Coupons': create_coupons(),
        'Vendors': create_vendors(),
        'Vendor Products': create_vendor_products(),
        'Warehouses': create_warehouses(),
        'Delivery Partners': create_delivery_partners(),
        'Product Views': create_product_views(),
        'Search History': create_search_history(),
        'Abandoned Carts': create_abandoned_carts(),
        'Sales Reports': create_sales_reports(),
        'Reward Programs': create_reward_programs(),
        'User Rewards': create_user_rewards(),
        'Risk Scores': create_risk_scores(),
        'Subscription Plans': create_subscription_plans(),
        'Subscriptions': create_subscriptions(),
        'Tax Rules': create_tax_rules(),
        'Invoice History': create_invoice_history()
    }
    
    for name, df in tables.items():
        print(f"\n{'='*50}")
        print(f"{name:^50}")  # Center the table name
        print('='*50)
        
        # Handle DataFrame display
        with pd.option_context('display.max_columns', None,  # Show all columns
                             'display.width', 150,           # Wider display
                             'display.precision', 2,         # Round decimals
                             'display.colheader_justify', 'left'):  # Left-align headers
            print(df.head(1).to_string(index=False))  # Remove index column

if __name__ == "__main__":
    print_sample_data()