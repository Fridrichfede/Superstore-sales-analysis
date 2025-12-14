create_tables = '''
create schema if not exists superstore_sales;
drop table if exists superstore_sales.deal_info cascade;
drop table if exists superstore_sales.customer_info cascade;
drop table if exists superstore_sales.product_info cascade;
drop table if exists superstore_sales.order_info cascade;

create table superstore_sales.order_info (
order_id VARCHAR(500) primary KEY,
order_date DATE,
ship_date DATE,
ship_mode VARCHAR(500)
);
create table superstore_sales.customer_info (
customer_id VARCHAR(500) primary KEY,
customer_name VARCHAR(500),
segment VARCHAR(500),
country VARCHAR(500),
city VARCHAR(500),
state VARCHAR(500),
postal_code float,
region VARCHAR(500)
);
create table superstore_sales.product_info (
product_id VARCHAR(500) primary KEY,
category VARCHAR(500),
sub_category VARCHAR(500),
product_name VARCHAR(500));

create table superstore_sales.deal_info (
deal_id INT generated always as identity  primary KEY,
order_id VARCHAR(500),
customer_id VARCHAR(500),
product_id VARCHAR(500),
sales numeric(10,2),
quantity INT,
discount numeric(10,2),
profit numeric(10,2),
foreign key (order_id) references superstore_sales.order_info(order_id),
foreign key (customer_id) references superstore_sales.customer_info(customer_id),
foreign key (product_id) references superstore_sales.product_info(product_id)
);
'''
dynamics_of_sales_and_profit = '''
SELECT order_i.order_id, order_date, sales, profit
FROM superstore_sales.order_info AS order_i
LEFT JOIN superstore_sales.deal_info AS s_s ON order_i.order_id = s_s.order_id;
'''
comparison_by_categories = '''
SELECT p_i.category, p_i.sub_category, d_i.sales, d_i.profit, d_i.quantity
FROM superstore_sales.product_info AS p_i
LEFT JOIN superstore_sales.deal_info AS d_i ON p_i.product_id = d_i.product_id;
'''

distribution_of_profitability='''SELECT profit
FROM superstore_sales.deal_info;'''

overall_KPI='''SELECT profit, sales, quantity
FROM superstore_sales.deal_info;'''
rentability='''SELECT p_i.sub_category, d_i.sales, d_i.profit, d_i.profit/d_i.sales AS net_profit_margin
FROM superstore_sales.product_info AS p_i
LEFT JOIN superstore_sales.deal_info AS d_i ON p_i.product_id = d_i.product_id;'''

unprofitable_transactions='''SELECT order_id, customer_id, product_id, profit
FROM superstore_sales.deal_info
WHERE profit<0;'''
top_10_products=6
visualisation=7
discount_impact_on_profit=8
