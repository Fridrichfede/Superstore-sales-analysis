from functions import get_engine
import sql_queries
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd


engine = get_engine()


# 1. Dynamics of sales and profit across the time

df = pd.read_sql_query(sql=sql_queries.dynamics_of_sales_and_profit, con=engine)
df['year'] = pd.to_datetime(df['order_date']).dt.year
df1 = df.groupby('year')[['sales', 'profit']].sum()
def sales_by_year():
     sns.lineplot(data=df1, x='year', y='sales')
     ax = plt.gca()
     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
     plt.show()
def profit_by_year():
     sns.lineplot(data=df1, x='year', y='profit')
     ax = plt.gca()
     ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
     plt.show()


# 2.Comparison by categories and sub_catgories


df2 = pd.read_sql_query(sql=sql_queries.comparison_by_categories, con=engine)
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
def sales_by_sub_category():
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


profit_d = pd.read_sql_query(sql=sql_queries.distribution_of_profitability, con=engine)
def show_distr_of_profitability():
     sns.histplot(data=profit_d, x='profit', log_scale=True, bins=100, kde=True)
     plt.title('Distribution of profitability among items')
     plt.show()


# Overall KPI


df3 = pd.read_sql_query(sql=sql_queries.overall_KPI, con=engine)
total_sales = df3['sales'].sum()
total_profit = df3['profit'].sum()
def KPI():
     print(f'Total profit: {total_profit}, Total sales:{total_sales}')


# Rentability for sub_categories


df2_rentability = pd.read_sql_query(sql=sql_queries.rentability, con=engine)
def barplot_rentability():
    axis1= sns.barplot(x='sub_category', y='net_profit_margin', data=df2_rentability, errorbar=None)
    axis1.tick_params(axis='x', rotation=90)
    plt.title('Net profit margin by sub-category')
    plt.tight_layout()
    plt.show()
 

# Unprofitable transactions


df4=pd.read_sql_query(sql=sql_queries.unprofitable_transactions, con=engine)
def unp_transactions():
      print(df4)


# Visualisation of sales by Region


df5 = pd.read_sql_query(sql=sql_queries.visualisation_of_sales_and_profit_by_region, con=engine)
def sales_v_by_region():
     sns.barplot(x='region', y='sum_of_sales', data=df5, errorbar=None)
     plt.title('Sales by region')
     plt.tight_layout()
     plt.show()


# Visualisation of sales by State


df6 = pd.read_sql_query(sql=sql_queries.visualisation_of_sales_and_profit_by_state, con=engine)
def sales_v_by_state():
     axis2 = sns.barplot(x='state', y='sum_of_sales', data=df6, errorbar=None)
     axis2.tick_params(axis='x', rotation=90)
     plt.title('Sales by state')
     plt.tight_layout()
     plt.show()
sales_v_by_state()


# Correlation between profit and discount


df7 = pd.read_sql_query(sql=sql_queries.discount_impact_on_profit, con=engine)
def discount_and_profit_correlation():
     corr_value = df7['profit'].corr(df7['discount'])
     print(f'Correlation value between profit and discount: {corr_value}')