from functions import get_engine
from sql_queries import dynamics_of_sales_and_profit, comparison_by_categories, distribution_of_profitability
from sql_queries import overall_KPI, rentability, unprofitable_transactions
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd
engine = get_engine()


# 1. Dynamics of sales and profit across the time


df = pd.read_sql_query(sql=dynamics_of_sales_and_profit, con=engine)
df['year'] = pd.to_datetime(df['order_date']).dt.year
df1 = df.groupby('year')[['sales', 'profit']].sum()
def sales_by_year():
     sns.lineplot(data=df1, x='year', y='Sales')
     ax = plt.gca()
     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
     plt.show()
def profit_by_year():
     sns.lineplot(data=df1, x='year', y='Profit')
     ax = plt.gca()
     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
     plt.show()

# 2.Comparison by categories and sub_catgories


df2 = pd.read_sql_query(sql=comparison_by_categories, con=engine)
df_2_category = df2[['category', 'sales', 'profit', 'quantity']]
df_2_category_group = df_2_category.groupby('category')[['sales', 'profit']].sum()
def sales_by_category():
     sns.barplot(x='category', y='sales', data=df_2_category_group)
     plt.title('Sales by categories')
     plt.show()
def profit_by_category():
     sns.barplot(x='category', y='profit', data=df_2_category_group)
     plt.title('Profit by categories 2015-2018')
     plt.show()

df_2_sub_category = df2[['sub_category', 'sales', 'profit', 'quantity']]
df_2_sub_category_group = df_2_sub_category.groupby('sub_category')[['sales', 'profit']].sum()
def sales_sub_category():
     ax = sns.barplot(x='sub_category', y='sales', data=df_2_sub_category_group)
     ax.tick_params(axis='x', rotation=90)
     plt.title('Sales by sub-categories')
     plt.tight_layout()
     plt.show()

def profit_by_sub_category():
     ax_1 = sns.barplot(x='sub_category', y='profit', data=df_2_sub_category_group)
     ax_1.tick_params(axis='x', rotation=90)
     plt.title('Profit by sub categories')
     plt.tight_layout()
     plt.show()

# 3.Distribution of profitability
profit_d = pd.read_sql_query(sql=distribution_of_profitability, con=engine)
def show_distr_of_profitability():
     sns.histplot(data=profit_d, x='profit', log_scale=True, bins=100, kde=True)
     plt.title('Distribution of profitability among items')
     plt.show()


# Overall KPI
df3 = pd.read_sql_query(sql=overall_KPI, con=engine)
total_sales = df3['sales'].sum()
total_profit = df3['profit'].sum()
def KPI():
     print(f'Total profit: {total_profit}, Total sales:{total_sales}')


# Rentability for sub_categories
df2_rentability = pd.read_sql_query(sql=rentability, con=engine)
def barplot_rentability():
    axis1= sns.barplot(x='sub_category', y='net_profit_margin', data=df2_rentability, errorbar=None)
    axis1.tick_params(axis='x', rotation=90)
    plt.title('Net profit margin by sub-category')
    plt.tight_layout()
    plt.show()

# Unprofitable transactions
df4=pd.read_sql_query(sql=unprofitable_transactions, con=engine)
print(df4)

# Top-10 products by sum of 'sales' and 'quantity'
# Visualisation of profit/sales by State/Region
# Discount's impact on profit