import pandas as pd
from config import db_connection_str
from sqlalchemy import create_engine, text
from sql_queries import create_tables

# 1.Connection to PostgreSQL DB
db_connection = create_engine(db_connection_str)
schema_name = 'superstore_sales'
file_path = "C:\\Users\\Zhassuzak\\OneDrive\\Desktop\\Superstore_sales_analysis\\data\\raw\\Superstore_sales.csv"
print('Programm connected to DB succesfully')


# 2.Uploading raw data
try:
   df_raw = pd.read_csv(file_path, encoding='latin1')
   print('Succesfully read dataset')
except FileNotFoundError:
   print(f'{file_path} not found')
   exit()
   
# 3.Data cleaning
df_raw = df_raw.rename(columns={'Order ID':'order_id',
                                'Order Date':'orderdate',
                                'Ship Date':'shipdate',
                                'Ship Mode':'ship_mode',
                                'Customer ID':'customer_id',
                                'Customer Name':'customer_name',
                                'Segment':'segment',
                                'Country':'country',
                                'City':'city',
                                'State':'state',
                                'Postal Code' : 'postal_code',
                                'Region' : 'region',
                                'Product ID':'product_id',
                                'Category':'category',
                                'Sub-Category':'sub_category',
                                'Product Name':'product_name',
                                'Sales':'sales',
                                'Quantity':'quantity',
                                'Discount':'discount',
                                'Profit':'profit'})

df_raw = df_raw.drop(columns=['Row ID'], axis=1)
customer_info = df_raw[['customer_id', 'customer_name', 'segment', 'country', 'city', 
                         'state', 'postal_code', 'region']].drop_duplicates(subset=['customer_id']).reset_index(drop=True)
order_info=df_raw[['order_id', 'orderdate', 'shipdate', 'ship_mode']].drop_duplicates(subset=['order_id']).reset_index(drop=True)
product_info=df_raw[['product_id', 'category', 'sub_category', 'product_name']].drop_duplicates(subset=['product_id']).reset_index(drop=True)
order_info['order_date'] = pd.to_datetime(order_info['orderdate'], format='%Y-%m-%d').dt.date
order_info['ship_date'] = pd.to_datetime(order_info['shipdate'], format='%Y-%m-%d').dt.date
order_info=order_info.drop(['orderdate', 'shipdate'], axis=1)
deal_info=df_raw[['order_id', 'customer_id', 'product_id', 'sales', 'quantity', 'discount', 'profit']].drop_duplicates()
print('Data cleaned successfully')

# 4. Executing sql queries
with db_connection.connect() as conn:
   try:
      conn.execute((text(create_tables)))
      conn.commit()
   except Exception as e:
      print(f'Something went wrong: {e}')

# 5.Uploading processed data to PostgreSQL DB in order to get 'customer_id', 'product_id', 'order_id' columns
customer_info.to_sql(name=f'customer_info', con=db_connection, schema=schema_name, if_exists='append', index=False)
product_info.to_sql(name=f'product_info', con=db_connection, schema=schema_name, if_exists='append', index=False)
order_info.to_sql(name=f'order_info', con=db_connection, schema=schema_name, if_exists='append', index=False)
deal_info.to_sql(name=f'deal_info', con=db_connection, schema=schema_name, if_exists='append', index=False)
print('Cleaned data uploaded to PostgreSQL succesfully')
print('ETL-pipeline has succesfully finished!')



