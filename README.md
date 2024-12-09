# Ecommerce website documentation
## Summary

- [Introduction](#introduction)
- [Database Type](#database-type)
- [Table Structure](#table-structure)
	- [Users](#Users)
	- [User_Addresses](#User_Addresses)
	- [Categories](#Categories)
	- [Products](#Products)
	- [Product_Images](#Product_Images)
	- [Product_Variants](#Product_Variants)
	- [Inventory](#Inventory)
	- [Orders](#Orders)
	- [Order_Items](#Order_Items)
	- [Payments](#Payments)
	- [Shipping_Details](#Shipping_Details)
	- [Reviews](#Reviews)
	- [Coupons](#Coupons)
	- [Order_Coupons](#Order_Coupons)
	- [Vendors](#Vendors)
	- [Vendor_Products](#Vendor_Products)
	- [Vendor_Payments](#Vendor_Payments)
	- [Warehouses](#Warehouses)
	- [Inventory_Locations](#Inventory_Locations)
	- [Delivery_Partners](#Delivery_Partners)
	- [Delivery_Tracking](#Delivery_Tracking)
	- [Product_Views](#Product_Views)
	- [Search_History](#Search_History)
	- [Abandoned_Carts](#Abandoned_Carts)
	- [Sales_Reports](#Sales_Reports)
	- [Currencies](#Currencies)
	- [Product_Pricing](#Product_Pricing)
	- [Reward_Programs](#Reward_Programs)
	- [User_Rewards](#User_Rewards)
	- [Risk_Scores](#Risk_Scores)
	- [Subscription_Plans](#Subscription_Plans)
	- [Subscriptions](#Subscriptions)
	- [Tax_Rules](#Tax_Rules)
	- [Invoice_History](#Invoice_History)
- [Relationships](#relationships)
- [Database Diagram](#database-Diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Users

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **user_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **first_name** | VARCHAR(50) | not null  |  | |
| **last_name** | VARCHAR(50) | not null  |  | |
| **email** | VARCHAR(100) | not null , unique |  | |
| **password_hash** | VARCHAR(255) | not null  |  | |
| **phone_number** | VARCHAR(15) | not null  |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | |
| **updated_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### User_Addresses

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **address_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | User_Addresses_user_id_fk | |
| **address_line1** | VARCHAR(255) | not null  |  | |
| **address_line2** | VARCHAR(255) | not null  |  | |
| **city** | VARCHAR(100) | not null  |  | |
| **state** | VARCHAR(100) | not null  |  | |
| **country** | VARCHAR(100) | not null  |  | |
| **postal_code** | VARCHAR(20) | not null  |  | |
| **is_default** | BOOLEAN | not null , default: false |  | | 


### Categories

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **category_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **category_name** | VARCHAR(100) | not null  |  | |
| **parent_category_id** | BIGINT | not null  |  | | 


### Products

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **product_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | VARCHAR(255) | not null  |  | |
| **description** | TEXT | not null  |  | |
| **price** | DECIMAL(10,2) | not null  |  | |
| **category_id** | BIGINT | not null  | Products_category_id_fk | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | |
| **updated_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Product_Images

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **image_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Product_Images_product_id_fk | |
| **image_url** | VARCHAR(2083) | not null  |  | |
| **is_primary** | BOOLEAN | not null , default: false |  | | 


### Product_Variants

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **variant_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Product_Variants_product_id_fk | |
| **variant_name** | VARCHAR(100) | not null  |  | |
| **price** | DECIMAL(10,2) | not null  |  | |
| **stock_quantity** | INTEGER | not null , default: 0 |  | | 


### Inventory

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **inventory_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Inventory_product_id_fk | |
| **warehouse_location** | VARCHAR(255) | not null  |  | |
| **stock_quantity** | INTEGER | not null  |  | | 


### Orders

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **order_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Orders_user_id_fk | |
| **total_amount** | DECIMAL(10,2) | not null  |  | |
| **status** | BLOB | not null , default: Pending |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | |
| **updated_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Order_Items

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **order_item_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **order_id** | BIGINT | not null  | Order_Items_order_id_fk | |
| **product_id** | BIGINT | not null  | Order_Items_product_id_fk | |
| **quantity** | INTEGER | not null  |  | |
| **price** | DECIMAL(10,2) | not null  |  | | 


### Payments

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **payment_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **order_id** | BIGINT | not null  | Payments_order_id_fk | |
| **payment_method** | BLOB | not null  |  | |
| **amount** | DECIMAL(10,2) | not null  |  | |
| **payment_status** | BLOB | not null , default: Pending |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Shipping_Details

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **shipping_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **order_id** | BIGINT | not null  | Shipping_Details_order_id_fk | |
| **address_id** | BIGINT | not null  | Shipping_Details_address_id_fk | |
| **shipping_status** | BLOB | not null , default: Pending |  | |
| **tracking_number** | VARCHAR(50) | not null  |  | |
| **carrier_name** | VARCHAR(100) | not null  |  | | 


### Reviews

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **review_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Reviews_product_id_fk | |
| **user_id** | BIGINT | not null  | Reviews_user_id_fk | |
| **rating** | INTEGER | not null  |  | |
| **review_text** | TEXT | not null  |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Coupons

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **coupon_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **code** | VARCHAR(20) | not null , unique |  | |
| **discount_percentage** | DECIMAL(5,2) | not null  |  | |
| **start_date** | DATE | not null  |  | |
| **end_date** | DATE | not null  |  | |
| **max_usage** | INTEGER | not null  |  | |
| **usage_count** | INTEGER | not null , default: 0 |  | | 


### Order_Coupons

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **order_coupon_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **order_id** | BIGINT | not null  | Order_Coupons_order_id_fk | |
| **coupon_id** | BIGINT | not null  | Order_Coupons_coupon_id_fk | | 


### Vendors

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **vendor_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | VARCHAR(100) | not null  |  | |
| **email** | VARCHAR(100) | not null , unique |  | |
| **phone_number** | VARCHAR(15) | not null  |  | |
| **address** | VARCHAR(255) | not null  |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | |
| **updated_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Vendor_Products

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **vendor_product_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **vendor_id** | BIGINT | not null  | Vendor_Products_vendor_id_fk | |
| **product_id** | BIGINT | not null  | Vendor_Products_product_id_fk | |
| **stock_quantity** | INTEGER | not null  |  | | 


### Vendor_Payments

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **payment_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **vendor_id** | BIGINT | not null  | Vendor_Payments_vendor_id_fk | |
| **amount** | DECIMAL(10,2) | not null  |  | |
| **payment_date** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | |
| **status** | BLOB | not null , default: Pending |  | | 


### Warehouses

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **warehouse_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | VARCHAR(100) | not null  |  | |
| **location** | VARCHAR(255) | not null  |  | |
| **capacity** | INTEGER | not null  |  | | 


### Inventory_Locations

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **location_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Inventory_Locations_product_id_fk | |
| **warehouse_id** | BIGINT | not null  | Inventory_Locations_warehouse_id_fk | |
| **stock_quantity** | INTEGER | not null  |  | | 


### Delivery_Partners

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **partner_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | VARCHAR(100) | not null  |  | |
| **contact_email** | VARCHAR(100) | not null  |  | |
| **contact_phone** | VARCHAR(15) | not null  |  | | 


### Delivery_Tracking

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **tracking_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **shipping_id** | BIGINT | not null  | Delivery_Tracking_shipping_id_fk | |
| **partner_id** | BIGINT | not null  | Delivery_Tracking_partner_id_fk | |
| **tracking_number** | VARCHAR(100) | not null  |  | |
| **current_status** | BLOB | not null , default: In Transit |  | |
| **last_updated** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Product_Views

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **view_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Product_Views_user_id_fk | |
| **product_id** | BIGINT | not null  | Product_Views_product_id_fk | |
| **view_date** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Search_History

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **search_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Search_History_user_id_fk | |
| **search_query** | VARCHAR(255) | not null  |  | |
| **search_date** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Abandoned_Carts

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **cart_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Abandoned_Carts_user_id_fk | |
| **product_id** | BIGINT | not null  | Abandoned_Carts_product_id_fk | |
| **quantity** | INTEGER | not null  |  | |
| **added_date** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Sales_Reports

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **report_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Sales_Reports_product_id_fk | |
| **sales_date** | DATE | not null  |  | |
| **total_quantity_sold** | INTEGER | not null , default: 0 |  | |
| **total_revenue** | DECIMAL(10,2) | not null , default: 0 |  | | 


### Currencies

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **currency_code** | CHAR(3) | 🔑 PK, not null  |  | |
| **exchange_rate** | DECIMAL(10,5) | not null , default: 1 |  | |
| **last_updated** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Product_Pricing

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **pricing_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **product_id** | BIGINT | not null  | Product_Pricing_product_id_fk | |
| **currency_code** | CHAR(3) | not null  | Product_Pricing_currency_code_fk | |
| **price** | DECIMAL(10,2) | not null  |  | | 


### Reward_Programs

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **program_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **program_name** | VARCHAR(100) | not null  |  | |
| **description** | TEXT | not null  |  | |
| **start_date** | DATE | not null  |  | |
| **end_date** | DATE | not null  |  | |
| **points_multiplier** | DECIMAL(5,2) | not null , default: 1 |  | | 


### User_Rewards

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **reward_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | User_Rewards_user_id_fk | |
| **program_id** | BIGINT | not null  | User_Rewards_program_id_fk | |
| **points_earned** | INTEGER | not null , default: 0 |  | |
| **points_redeemed** | INTEGER | not null , default: 0 |  | | 


### Risk_Scores

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **risk_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Risk_Scores_user_id_fk | |
| **order_id** | BIGINT | not null  | Risk_Scores_order_id_fk | |
| **risk_score** | DECIMAL(5,2) | not null  |  | |
| **generated_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Subscription_Plans

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **plan_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **plan_name** | VARCHAR(100) | not null  |  | |
| **description** | TEXT | not null  |  | |
| **price** | DECIMAL(10,2) | not null  |  | |
| **billing_cycle** | BLOB | not null , default: Monthly |  | |
| **created_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


### Subscriptions

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **subscription_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **user_id** | BIGINT | not null  | Subscriptions_user_id_fk | |
| **plan_id** | BIGINT | not null  | Subscriptions_plan_id_fk | |
| **start_date** | DATE | not null  |  | |
| **end_date** | DATE | not null  |  | |
| **status** | BLOB | not null , default: Active |  | | 


### Tax_Rules

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **tax_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **category_id** | BIGINT | not null  | Tax_Rules_category_id_fk | |
| **region** | VARCHAR(100) | not null  |  | |
| **tax_rate** | DECIMAL(5,2) | not null  |  | | 


### Invoice_History

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **invoice_id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **order_id** | BIGINT | not null  | Invoice_History_order_id_fk | |
| **total_amount** | DECIMAL(10,2) | not null  |  | |
| **tax_amount** | DECIMAL(10,2) | not null  |  | |
| **issued_at** | TIMESTAMP | not null , default: CURRENT_TIMESTAMP |  | | 


## Relationships

- **User_Addresses to Users**: many_to_one
- **Products to Categories**: many_to_one
- **Product_Images to Products**: many_to_one
- **Product_Variants to Products**: many_to_one
- **Inventory to Products**: many_to_one
- **Orders to Users**: many_to_one
- **Order_Items to Orders**: many_to_one
- **Order_Items to Products**: many_to_one
- **Payments to Orders**: many_to_one
- **Shipping_Details to Orders**: many_to_one
- **Shipping_Details to User_Addresses**: many_to_one
- **Reviews to Products**: many_to_one
- **Reviews to Users**: many_to_one
- **Order_Coupons to Orders**: many_to_one
- **Order_Coupons to Coupons**: many_to_one
- **Vendor_Products to Vendors**: many_to_one
- **Vendor_Products to Products**: many_to_one
- **Vendor_Payments to Vendors**: many_to_one
- **Inventory_Locations to Products**: many_to_one
- **Inventory_Locations to Warehouses**: many_to_one
- **Delivery_Tracking to Shipping_Details**: many_to_one
- **Delivery_Tracking to Delivery_Partners**: many_to_one
- **Product_Views to Users**: many_to_one
- **Product_Views to Products**: many_to_one
- **Search_History to Users**: many_to_one
- **Abandoned_Carts to Users**: many_to_one
- **Abandoned_Carts to Products**: many_to_one
- **Sales_Reports to Products**: many_to_one
- **Product_Pricing to Products**: many_to_one
- **Product_Pricing to Currencies**: many_to_one
- **User_Rewards to Users**: many_to_one
- **User_Rewards to Reward_Programs**: many_to_one
- **Risk_Scores to Users**: many_to_one
- **Risk_Scores to Orders**: many_to_one
- **Subscriptions to Users**: many_to_one
- **Subscriptions to Subscription_Plans**: many_to_one
- **Tax_Rules to Categories**: many_to_one
- **Invoice_History to Orders**: many_to_one

## Database Diagram

```mermaid
erDiagram
	User_Addresses ||--o{ Users : references
	Products ||--o{ Categories : references
	Product_Images ||--o{ Products : references
	Product_Variants ||--o{ Products : references
	Inventory ||--o{ Products : references
	Orders ||--o{ Users : references
	Order_Items ||--o{ Orders : references
	Order_Items ||--o{ Products : references
	Payments ||--o{ Orders : references
	Shipping_Details ||--o{ Orders : references
	Shipping_Details ||--o{ User_Addresses : references
	Reviews ||--o{ Products : references
	Reviews ||--o{ Users : references
	Order_Coupons ||--o{ Orders : references
	Order_Coupons ||--o{ Coupons : references
	Vendor_Products ||--o{ Vendors : references
	Vendor_Products ||--o{ Products : references
	Vendor_Payments ||--o{ Vendors : references
	Inventory_Locations ||--o{ Products : references
	Inventory_Locations ||--o{ Warehouses : references
	Delivery_Tracking ||--o{ Shipping_Details : references
	Delivery_Tracking ||--o{ Delivery_Partners : references
	Product_Views ||--o{ Users : references
	Product_Views ||--o{ Products : references
	Search_History ||--o{ Users : references
	Abandoned_Carts ||--o{ Users : references
	Abandoned_Carts ||--o{ Products : references
	Sales_Reports ||--o{ Products : references
	Product_Pricing ||--o{ Products : references
	Product_Pricing ||--o{ Currencies : references
	User_Rewards ||--o{ Users : references
	User_Rewards ||--o{ Reward_Programs : references
	Risk_Scores ||--o{ Users : references
	Risk_Scores ||--o{ Orders : references
	Subscriptions ||--o{ Users : references
	Subscriptions ||--o{ Subscription_Plans : references
	Tax_Rules ||--o{ Categories : references
	Invoice_History ||--o{ Orders : references

	Users {
		BIGINT user_id
		VARCHAR(50) first_name
		VARCHAR(50) last_name
		VARCHAR(100) email
		VARCHAR(255) password_hash
		VARCHAR(15) phone_number
		TIMESTAMP created_at
		TIMESTAMP updated_at
	}

	User_Addresses {
		BIGINT address_id
		BIGINT user_id
		VARCHAR(255) address_line1
		VARCHAR(255) address_line2
		VARCHAR(100) city
		VARCHAR(100) state
		VARCHAR(100) country
		VARCHAR(20) postal_code
		BOOLEAN is_default
	}

	Categories {
		BIGINT category_id
		VARCHAR(100) category_name
		BIGINT parent_category_id
	}

	Products {
		BIGINT product_id
		VARCHAR(255) name
		TEXT description
		DECIMAL(10,2) price
		BIGINT category_id
		TIMESTAMP created_at
		TIMESTAMP updated_at
	}

	Product_Images {
		BIGINT image_id
		BIGINT product_id
		VARCHAR(2083) image_url
		BOOLEAN is_primary
	}

	Product_Variants {
		BIGINT variant_id
		BIGINT product_id
		VARCHAR(100) variant_name
		DECIMAL(10,2) price
		INTEGER stock_quantity
	}

	Inventory {
		BIGINT inventory_id
		BIGINT product_id
		VARCHAR(255) warehouse_location
		INTEGER stock_quantity
	}

	Orders {
		BIGINT order_id
		BIGINT user_id
		DECIMAL(10,2) total_amount
		BLOB status
		TIMESTAMP created_at
		TIMESTAMP updated_at
	}

	Order_Items {
		BIGINT order_item_id
		BIGINT order_id
		BIGINT product_id
		INTEGER quantity
		DECIMAL(10,2) price
	}

	Payments {
		BIGINT payment_id
		BIGINT order_id
		BLOB payment_method
		DECIMAL(10,2) amount
		BLOB payment_status
		TIMESTAMP created_at
	}

	Shipping_Details {
		BIGINT shipping_id
		BIGINT order_id
		BIGINT address_id
		BLOB shipping_status
		VARCHAR(50) tracking_number
		VARCHAR(100) carrier_name
	}

	Reviews {
		BIGINT review_id
		BIGINT product_id
		BIGINT user_id
		INTEGER rating
		TEXT review_text
		TIMESTAMP created_at
	}

	Coupons {
		BIGINT coupon_id
		VARCHAR(20) code
		DECIMAL(5,2) discount_percentage
		DATE start_date
		DATE end_date
		INTEGER max_usage
		INTEGER usage_count
	}

	Order_Coupons {
		BIGINT order_coupon_id
		BIGINT order_id
		BIGINT coupon_id
	}

	Vendors {
		BIGINT vendor_id
		VARCHAR(100) name
		VARCHAR(100) email
		VARCHAR(15) phone_number
		VARCHAR(255) address
		TIMESTAMP created_at
		TIMESTAMP updated_at
	}

	Vendor_Products {
		BIGINT vendor_product_id
		BIGINT vendor_id
		BIGINT product_id
		INTEGER stock_quantity
	}

	Vendor_Payments {
		BIGINT payment_id
		BIGINT vendor_id
		DECIMAL(10,2) amount
		TIMESTAMP payment_date
		BLOB status
	}

	Warehouses {
		BIGINT warehouse_id
		VARCHAR(100) name
		VARCHAR(255) location
		INTEGER capacity
	}

	Inventory_Locations {
		BIGINT location_id
		BIGINT product_id
		BIGINT warehouse_id
		INTEGER stock_quantity
	}

	Delivery_Partners {
		BIGINT partner_id
		VARCHAR(100) name
		VARCHAR(100) contact_email
		VARCHAR(15) contact_phone
	}

	Delivery_Tracking {
		BIGINT tracking_id
		BIGINT shipping_id
		BIGINT partner_id
		VARCHAR(100) tracking_number
		BLOB current_status
		TIMESTAMP last_updated
	}

	Product_Views {
		BIGINT view_id
		BIGINT user_id
		BIGINT product_id
		TIMESTAMP view_date
	}

	Search_History {
		BIGINT search_id
		BIGINT user_id
		VARCHAR(255) search_query
		TIMESTAMP search_date
	}

	Abandoned_Carts {
		BIGINT cart_id
		BIGINT user_id
		BIGINT product_id
		INTEGER quantity
		TIMESTAMP added_date
	}

	Sales_Reports {
		BIGINT report_id
		BIGINT product_id
		DATE sales_date
		INTEGER total_quantity_sold
		DECIMAL(10,2) total_revenue
	}

	Currencies {
		CHAR(3) currency_code
		DECIMAL(10,5) exchange_rate
		TIMESTAMP last_updated
	}

	Product_Pricing {
		BIGINT pricing_id
		BIGINT product_id
		CHAR(3) currency_code
		DECIMAL(10,2) price
	}

	Reward_Programs {
		BIGINT program_id
		VARCHAR(100) program_name
		TEXT description
		DATE start_date
		DATE end_date
		DECIMAL(5,2) points_multiplier
	}

	User_Rewards {
		BIGINT reward_id
		BIGINT user_id
		BIGINT program_id
		INTEGER points_earned
		INTEGER points_redeemed
	}

	Risk_Scores {
		BIGINT risk_id
		BIGINT user_id
		BIGINT order_id
		DECIMAL(5,2) risk_score
		TIMESTAMP generated_at
	}

	Subscription_Plans {
		BIGINT plan_id
		VARCHAR(100) plan_name
		TEXT description
		DECIMAL(10,2) price
		BLOB billing_cycle
		TIMESTAMP created_at
	}

	Subscriptions {
		BIGINT subscription_id
		BIGINT user_id
		BIGINT plan_id
		DATE start_date
		DATE end_date
		BLOB status
	}

	Tax_Rules {
		BIGINT tax_id
		BIGINT category_id
		VARCHAR(100) region
		DECIMAL(5,2) tax_rate
	}

	Invoice_History {
		BIGINT invoice_id
		BIGINT order_id
		DECIMAL(10,2) total_amount
		DECIMAL(10,2) tax_amount
		TIMESTAMP issued_at
	}
```
