# Dynamics of sales and profit across the time
# Comparison by categories and sub_catgories
# Distribution of profitability
# Sales and discount
# Overall KPI
# Rentability
# Unprofitable transactions
# Top-10 products by sum of 'sales' and 'quantity'
# Visualisation of profit/sales by State/Region
# Discount's impact on profit
'''
Признак формирования когорты: Месяц или Квартал первой покупки для каждого уникального Customer ID.
 (Это будет ' когорта привлечения'.)
Отчетный период: Месяцы, прошедшие с момента первой покупки.
Анализируемая метрика:
Процент повторных покупок (Retention Rate): Сколько клиентов из когорты, впервые купивших в Январе 2017, сделали повторную покупку в Феврале 2017, Марте 2017 и т.д.
Сумма продаж (Sales): Сколько денег приносит каждая когорта в последующие месяцы.
'''
from functions import get_engine, get_rows, execute_queries
from sql_queries import dynamics_of_sales_and_profit
import pandas as pd
data, columns = get_rows(dynamics_of_sales_and_profit)
dynamics = pd.DataFrame(data, columns=columns)
print(dynamics)
