import psycopg2
from sqlalchemy import create_engine
from datetime import datetime
import erp

DB_PARAMS = {
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5432,
    'sslmode': 'require'
}

CREATE_TABLES_SQL = """
-- USERS AND AUTHENTICATION
CREATE TABLE Users (
    user_id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE User_Addresses (
    address_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- PRODUCT MANAGEMENT
CREATE TABLE Categories (
    category_id BIGSERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    parent_category_id BIGINT NULL,
    FOREIGN KEY (parent_category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Products (
    product_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category_id BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Product_Images (
    image_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    image_url VARCHAR(2083) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Product_Variants (
    variant_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    variant_name VARCHAR(100),
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- INVENTORY
CREATE TABLE Inventory (
    inventory_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    warehouse_location VARCHAR(255),
    stock_quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- ORDERS
CREATE TABLE Orders (
    order_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Order_Items (
    order_item_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- PAYMENT
CREATE TABLE Payments (
    payment_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    payment_method VARCHAR(20) CHECK (payment_method IN ('Credit Card', 'Debit Card', 'Net Banking', 'UPI', 'PayPal')) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Completed', 'Failed', 'Refunded')) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

-- SHIPPING AND DELIVERY
CREATE TABLE Shipping_Details (
    shipping_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    address_id BIGINT NOT NULL,
    shipping_status VARCHAR(20) CHECK (shipping_status IN ('Pending', 'Shipped', 'In Transit', 'Delivered', 'Returned')) DEFAULT 'Pending',
    tracking_number VARCHAR(50),
    carrier_name VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (address_id) REFERENCES User_Addresses(address_id)
);

-- REVIEWS AND RATINGS
CREATE TABLE Reviews (
    review_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- COUPONS AND PROMOTIONS
CREATE TABLE Coupons (
    coupon_id BIGSERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    discount_percentage DECIMAL(5, 2) NOT NULL CHECK (discount_percentage BETWEEN 0 AND 100),
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_usage INT,
    usage_count INT DEFAULT 0
);

CREATE TABLE Order_Coupons (
    order_coupon_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    coupon_id BIGINT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (coupon_id) REFERENCES Coupons(coupon_id)
);

CREATE TABLE Vendors (
    vendor_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(15),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Vendor_Products (
    vendor_product_id BIGSERIAL PRIMARY KEY,
    vendor_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Vendor_Payments (
    payment_id BIGSERIAL PRIMARY KEY,
    vendor_id BIGINT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) CHECK (status IN ('Pending', 'Completed', 'Failed')) DEFAULT 'Pending',
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
);

CREATE TABLE Warehouses (
    warehouse_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(255) NOT NULL,
    capacity INT NOT NULL
);

CREATE TABLE Inventory_Locations (
    location_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    warehouse_id BIGINT NOT NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
);

CREATE TABLE Delivery_Partners (
    partner_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100),
    contact_phone VARCHAR(15)
);

CREATE TABLE Delivery_Tracking (
    tracking_id BIGSERIAL PRIMARY KEY,
    shipping_id BIGINT NOT NULL,
    partner_id BIGINT NOT NULL,
    tracking_number VARCHAR(100) NOT NULL,
    current_status VARCHAR(20) CHECK (current_status IN ('In Transit', 'Delivered', 'Returned', 'Lost')) DEFAULT 'In Transit',
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shipping_id) REFERENCES Shipping_Details(shipping_id),
    FOREIGN KEY (partner_id) REFERENCES Delivery_Partners(partner_id)
);

CREATE TABLE Product_Views (
    view_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    product_id BIGINT NOT NULL,
    view_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Search_History (
    search_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    search_query VARCHAR(255) NOT NULL,
    search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Abandoned_Carts (
    cart_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Sales_Reports (
    report_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    sales_date DATE NOT NULL,
    total_quantity_sold INT NOT NULL DEFAULT 0,
    total_revenue DECIMAL(10, 2) NOT NULL DEFAULT 0.0,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Currencies (
    currency_code CHAR(3) PRIMARY KEY,
    exchange_rate DECIMAL(10, 5) NOT NULL DEFAULT 1.0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Product_Pricing (
    pricing_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    currency_code CHAR(3) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (currency_code) REFERENCES Currencies(currency_code)
);

CREATE TABLE Reward_Programs (
    program_id BIGSERIAL PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    points_multiplier DECIMAL(5, 2) NOT NULL DEFAULT 1.0
);

CREATE TABLE User_Rewards (
    reward_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    program_id BIGINT NOT NULL,
    points_earned INT NOT NULL DEFAULT 0,
    points_redeemed INT NOT NULL DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (program_id) REFERENCES Reward_Programs(program_id)
);

CREATE TABLE Risk_Scores (
    risk_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT,
    order_id BIGINT,
    risk_score DECIMAL(5, 2) NOT NULL CHECK (risk_score BETWEEN 0 AND 100),
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

CREATE TABLE Subscription_Plans (
    plan_id BIGSERIAL PRIMARY KEY,
    plan_name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    billing_cycle VARCHAR(20) CHECK (billing_cycle IN ('Monthly', 'Yearly')) DEFAULT 'Monthly',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Subscriptions (
    subscription_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL,
    plan_id BIGINT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    status VARCHAR(20) CHECK (status IN ('Active', 'Cancelled', 'Expired')) DEFAULT 'Active',
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (plan_id) REFERENCES Subscription_Plans(plan_id)
);

CREATE TABLE Tax_Rules (
    tax_id BIGSERIAL PRIMARY KEY,
    category_id BIGINT NOT NULL,
    region VARCHAR(100) NOT NULL,
    tax_rate DECIMAL(5, 2) NOT NULL CHECK (tax_rate BETWEEN 0 AND 100),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

CREATE TABLE Invoice_History (
    invoice_id BIGSERIAL PRIMARY KEY,
    order_id BIGINT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    tax_amount DECIMAL(10, 2) NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);


"""

def create_database():
    """Create the database and tables."""
    conn = None
    cursor = None
    try:
        print("Connecting to PostgreSQL database...")
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True
        cursor = conn.cursor()
        
        print("Creating tables...")
        cursor.execute(CREATE_TABLES_SQL)
        print("Tables created successfully.")

    except psycopg2.Error as e:
        print(f"Error creating tables: {e}")
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def load_data():
    """Load data into the database using SQLAlchemy."""
    try:
        engine = create_engine(
            f"postgresql://{DB_PARAMS['user']}:{DB_PARAMS['password']}@{DB_PARAMS['host']}:{DB_PARAMS['port']}/{DB_PARAMS['database']}"
        )
        
        # Create fake data using functions in erp.py
        users = erp.create_users()
        user_addresses = erp.create_user_addresses()
        categories = erp.create_categories()
        products = erp.create_products()
        product_variants = erp.create_product_variants()
        inventory = erp.create_inventory()
        orders = erp.create_orders()
        order_items = erp.create_order_items()
        payments = erp.create_payments()
        currencies = erp.create_currencies()
        product_pricing = erp.create_product_pricing()
        shipping = erp.create_shipping_details()
        reviews = erp.create_reviews()
        coupons = erp.create_coupons()
        vendors = erp.create_vendors()
        vendor_products = erp.create_vendor_products()
        warehouses = erp.create_warehouses()
        delivery_partners = erp.create_delivery_partners()
        product_views = erp.create_product_views()
        search_history = erp.create_search_history()
        abandoned_carts = erp.create_abandoned_carts()
        sales_reports = erp.create_sales_reports()
        reward_programs = erp.create_reward_programs()
        user_rewards = erp.create_user_rewards()
        risk_scores = erp.create_risk_scores()
        subscription_plans = erp.create_subscription_plans()
        subscriptions = erp.create_subscriptions()
        tax_rules = erp.create_tax_rules()
        invoice_history = erp.create_invoice_history()

        # Load data into database
        users.to_sql('users', engine, if_exists='append', index=False)
        user_addresses.to_sql('user_addresses', engine, if_exists='append', index=False)
        categories.to_sql('categories', engine, if_exists='append', index=False)
        products.to_sql('products', engine, if_exists='append', index=False)
        product_variants.to_sql('product_variants', engine, if_exists='append', index=False)
        inventory.to_sql('inventory', engine, if_exists='append', index=False)
        orders.to_sql('orders', engine, if_exists='append', index=False)
        order_items.to_sql('order_items', engine, if_exists='append', index=False)
        payments.to_sql('payments', engine, if_exists='append', index=False)
        currencies.to_sql('currencies', engine, if_exists='append', index=False)
        product_pricing.to_sql('product_pricing', engine, if_exists='append', index=False)
        shipping.to_sql('shipping_details', engine, if_exists='append', index=False)
        reviews.to_sql('reviews', engine, if_exists='append', index=False)
        coupons.to_sql('coupons', engine, if_exists='append', index=False)
        vendors.to_sql('vendors', engine, if_exists='append', index=False)
        vendor_products.to_sql('vendor_products', engine, if_exists='append', index=False)
        warehouses.to_sql('warehouses', engine, if_exists='append', index=False)
        delivery_partners.to_sql('delivery_partners', engine, if_exists='append', index=False)
        product_views.to_sql('product_views', engine, if_exists='append', index=False)
        search_history.to_sql('search_history', engine, if_exists='append', index=False)
        abandoned_carts.to_sql('abandoned_carts', engine, if_exists='append', index=False)
        sales_reports.to_sql('sales_reports', engine, if_exists='append', index=False)
        reward_programs.to_sql('reward_programs', engine, if_exists='append', index=False)
        user_rewards.to_sql('user_rewards', engine, if_exists='append', index=False)
        risk_scores.to_sql('risk_scores', engine, if_exists='append', index=False)
        subscription_plans.to_sql('subscription_plans', engine, if_exists='append', index=False)
        subscriptions.to_sql('subscriptions', engine, if_exists='append', index=False)
        tax_rules.to_sql('tax_rules', engine, if_exists='append', index=False)
        invoice_history.to_sql('invoice_history', engine, if_exists='append', index=False)

        print("Data loaded successfully.")

    except Exception as e:
        print(f"Error loading data: {e}")

def delete_database():
    """Delete all tables from the database."""
    conn = None
    cursor = None
    try:
        print("Connecting to PostgreSQL database...")
        conn = psycopg2.connect(**DB_PARAMS)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # First, terminate any existing connections to the tables
        cursor.execute("""
            SELECT pg_terminate_backend(pid) 
            FROM pg_stat_activity 
            WHERE datname = %s AND pid <> pg_backend_pid()
        """, (DB_PARAMS['database'],))
        
        # Drop all tables in reverse order of creation to handle dependencies
        print("Dropping tables...")
        cursor.execute("""
            DROP TABLE IF EXISTS 
                invoice_history,
                tax_rules,
                subscriptions,
                subscription_plans,
                risk_scores,
                user_rewards,
                reward_programs,
                sales_reports,
                abandoned_carts,
                search_history,
                product_views,
                delivery_tracking,
                delivery_partners,
                inventory_locations,
                warehouses,
                vendor_payments,
                vendor_products,
                vendors,
                order_coupons,
                coupons,
                reviews,
                shipping_details,
                payments,
                order_items,
                orders,
                inventory,
                product_variants,
                product_images,
                product_pricing,
                products,
                categories,
                user_addresses,
                users,
                currencies
            CASCADE
        """)
        print("Tables dropped successfully.")

    except psycopg2.Error as e:
        print(f"Error dropping tables: {e}")
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def main():
    delete_database()
    create_database()
    load_data()

if __name__ == "__main__":
    main()