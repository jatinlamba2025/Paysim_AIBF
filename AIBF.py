#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime as dt


# In[3]:


# Set the sales variable to 8000
sales = 8000

# Set the cost of goods sold (cogs) variable to 5400
cogs = 5400

# Calculate the gross profit (gross_profit)
gross_profit = sales - cogs

# Print the gross profit
print("The gross profit is {}.".format(gross_profit))


# In[5]:


# Create and print the opex list
admin=700
travel=250
training=130
marketing=280
insurance=150


opex = [admin, travel, training, marketing, insurance]
print(opex)

# Calculate and print net profit
net_profit = gross_profit - sum(opex)
print("The net profit is {}.".format(net_profit))


# In[6]:


forecast_units = 950


# In[7]:


# Set variables units sold and sales price of the T-shirts (basic and custom)
salesprice_basic = 15
salesprice_custom = 25

# Calculate the combined sales price taking into account the sales mix
average_sales_price = (salesprice_basic * 0.6) + (salesprice_custom * 0.4)

# Calculate the total sales for next month
sales_USD = average_sales_price * forecast_units


# In[8]:


# Print the total sales
print("Next month's forecast sales figure is {:.2f} USD.".format(sales_USD))


# In[9]:


sales_price = 40

units_january = 500

units_february = 700


# In[10]:


# Forecast the sales of January
sales_january = sales_price * units_january

# Forecast the discounted price
dsales_price = sales_price * 0.6

# Forecast the sales of February
sales_february = (sales_price * units_february * 0.55) + (dsales_price * units_february * 0.45)

# Print the forecast sales for January and February
print("The forecast sales for January and February are {} and {} USD respectively.".format(sales_january, sales_february))


# In[11]:


machine_rental = 1300
material_costs_per_unit = 8
labor_costs_per_unit = 2
units_jan = 200
units_feb = 250


# In[12]:


# Set the variables for fixed costs and variable costs
fixed_costs = machine_rental  
variable_costs_per_unit = material_costs_per_unit  + labor_costs_per_unit

# Calculate the cogs for January and February
cogs_jan = ( 200 * variable_costs_per_unit) + fixed_costs
cogs_feb = (250* variable_costs_per_unit) + fixed_costs


# In[13]:


cogs_jan


# In[14]:


# Calculate the unit cost for January and February
unit_cost_jan = cogs_jan / units_jan
unit_cost_feb = cogs_feb / units_feb 

# Print the January and February cost per unit
print("The cost per unit for January and February are {} and {} USD respectively.".format(unit_cost_jan, unit_cost_feb))


# In[ ]:


# Calculate the unit cost for January and February
unit_cost_jan = cogs_jan / units_jan
unit_cost_feb = cogs_feb / units_feb 

# Print the January and February cost per unit
print("The cost per unit for January and February are {} and {} USD respectively.".format(unit_cost_jan, unit_cost_feb))


# In[15]:


fixed_costs = 1300
variable_costs_per_unit = 10
units_jan = 200
units_feb = 250
sales_price = 16
cogs_jan = (units_jan * variable_costs_per_unit) + fixed_costs
cogs_feb = (units_feb * variable_costs_per_unit) + machine_rental


# In[16]:


# Calculate the break-even point (in units) for Wizit
break_even = fixed_costs /(sales_price  - variable_costs_per_unit)

# Print the break even point in units
print("The break even point is {} units.".format(break_even))

# Forecast the gross profit for January and February
gross_profit_jan = (sales_price*units_jan ) - cogs_jan
gross_profit_feb = (sales_price*units_feb ) - cogs_feb 

# Print the gross profit for January and February
print("The gross profit for January and February are {} and {} USD respectively.".format(gross_profit_jan, gross_profit_feb))


# In[17]:


# Import pandas library
import pandas as pd


# In[19]:


# Import the data
income_statement = pd.read_csv("C:/Users/jatin/Downloads/TSLA-Income-Statement.csv")


# In[20]:


income_statement


# In[21]:


# Choose some interesting metrics
interesting_metrics = ['Revenue', 'Gross profit', 'Total operating expenses', 'Net income']

# Filter for rows containing these metrics
filtered_income_statement = income_statement[income_statement.metric.isin(interesting_metrics)]

# See the result
print(filtered_income_statement)


# In[22]:


revenue_metric = ['Revenue']

# Filter for rows containing the revenue metric
filtered_income_statement = income_statement[income_statement.metric.isin(revenue_metric)]

# Get the number of columns in filtered_income_statement
n_cols = len(filtered_income_statement.columns)

# Insert a column in the correct position containing the column 'Forecast'
filtered_income_statement.insert(n_cols, 'Forecast', 13000) 

# See the result
print(filtered_income_statement)


# In[23]:


month = 0


# In[24]:


# Create the list for sales, and empty lists for debtors and credits
sales = [500, 350, 700]
credits = [] 
debtors = []

# Create the statement to append the calculated figures to the debtors and credits lists
for mvalue in sales: 
    credits.append(mvalue * 0.6)
    if month > 0:
        debtors.append(credits[month] + credits[month-1])
    else:
        debtors.append(credits[month]) 
    month += 1
# Print the result
print("The ‘Debtors’ are {}.".format(debtors))


# In[25]:


debtors_jan = 1500


# In[26]:


# Calculate the bad debts for February
bad_debts_feb = 500 * 0.3

# Calculate the feb debtors amount
debtors_feb = (debtors_jan  - bad_debts_feb)

# Print the debtors for January and the bad debts and the debtors for February
print("The debtors are {} in January, {} in February. February's bad debts are {} USD.".format(debtors_jan, debtors_feb, bad_debts_feb))


# In[27]:


# Set the cost per unit
unit_cost = 0.25

# Create the list for production units and empty list for creditors
production = [1000,1200]
creditors = []

# Calculate the accounts payable for January and February
for mvalue in production: 
    creditors.append(mvalue * unit_cost * 0.5)
    
# Print the creditors balance for January and February
print("The creditors balance for January and February are {} and {} USD.".format(creditors[0], creditors[1]))


# In[28]:


# Create the variables
debtors_end = 650
sales_tot = 12500

# Calculate the debtor days variable
ddays_ratio = (debtors_end/sales_tot) * 365

# Print the result
print("The debtor days ratio is {}.".format(ddays_ratio))


# In[29]:


# Get the variables
cogs_tot = 4000
creditors_end = 650

# Calculate the days payable outstanding
dpo = (creditors_end/cogs_tot)*365

# Print the days payable outstanding
print("The days payable outstanding is {}.".format(dpo))


# In[30]:


# Get the variables
cogs_tot = 4000
creditors_end = 650
av_inv = 1900
sales_tot = 10000
ob_assets = 2000
cb_assets = 7000


# In[31]:


# Calculate the dii ratio 
dii_ratio = (av_inv/cogs_tot )*365

# Print the result
print("The DII ratio is {}.".format(dii_ratio))


# In[32]:


# Calculate the Average Assets
av_assets = (ob_assets + cb_assets)/2

# Calculate the Asset Turnover Ratio
at_ratio = sales_tot/av_assets

# Print the Asset Turnover Ratio
print("The asset turnover ratio is {}.".format(at_ratio))


# In[34]:


# Import the data
balance_sheet = pd.read_csv("C:/Users/jatin/Downloads/F-Balance-Sheet.csv")


# In[35]:


balance_sheet


# In[36]:


# Create the filter metric for Receivables
receivables_metric = ['Receivables']

# Create a boolean series with your metric
receivables_filter = balance_sheet.metric.isin(receivables_metric)

# Use the series to filter the dataset
filtered_balance_sheet = balance_sheet[receivables_filter]


# In[37]:


filtered_balance_sheet


# In[38]:


# Extract the zeroth value from the last time period (2017-12)
debtors_end = filtered_balance_sheet['2017-12'].iloc[0]


# In[39]:


debtors_end


# In[40]:


sales = 156776


# In[41]:


# Calculate the debtor days ratio
ddays = (debtors_end / sales) * 365

# Print the debtor days ratio
print("The debtor day ratio is {:.0f}. A higher debtors days ratio means it takes longer to collect cash from debtors.".format(ddays))


# In[42]:


ddays = 99
sales = 156776


# In[43]:


# Calculate the forecasted sales 
f_sales = sales * 1.1

# Solve for the forecasted debtors' ending balance
f_debtors_end = ddays  * f_sales  / 365

print("If sales rise by 10% and the debtor days decrease to {:.0f} then the forecasted closing balance for debtors will be {:.0f}.".format(ddays, f_debtors_end))


# In[44]:


# From previous step
f_sales = sales * 1.10
f_debtors_end = ddays * f_sales / 365

# Get the number of columns in the filtered balance sheet
n_cols = len(filtered_balance_sheet.columns)

# Append a Forecast column of the forecasted debtors' end balance
filtered_balance_sheet.insert(n_cols,'Forecast', f_debtors_end)

# See the result
print(filtered_balance_sheet)


# In[45]:


# Create a list for quarters and initialize an empty list qrtlist
quarters = [700, 650]
qrtlist = []

# Create a for loop to split the quarters into months and add to qrtlist
for qrt in quarters:
 month = round(qrt / 3, 2)
 qrtlist = qrtlist + [month,month,month]
 
# Print the result
print("The values per month for the first two quarters are {}.".format(qrtlist))


# In[46]:


# Create a months list, as well as an index, and set the quarter to 0
months = [100, 100, 150, 250, 300, 10, 20]
quarter = 0
index = 1
quarters = []

# Create for loop for quarter, print result, and increment the index
for sales in months:
    quarter += sales
    if index % 3 == 0 or index == len(months):
        quarters.append(quarter)
        quarter = 0
    index = index + 1
    
print("The quarter totals are Q1: {}, Q2: {}, Q3: {}".format(quarters[0], quarters[1], quarters[2]))


# In[47]:


# Import the datetime python library
from datetime import datetime

# Create a dt_object to convert the first date and print the month result
dt_object1 = datetime.strptime('14/02/2018', '%d/%m/%Y')
print(dt_object1)

# Create a dt_object to convert the second date and print the month result
dt_object2 = datetime.strptime('2 March 2018', '%d %B %Y')
print(dt_object2)


# In[48]:


# Set the variable for the datetime to convert
dt = '14/02/2018'

# Create the dictionary for the month values
mm = {'01': 'January', '02': 'February', '03': 'March'}

# Split the dt string into the different parts
day, month, year = dt.split('/')

# Print the concatenated date string
print(day + ' ' + mm[month] + ' ' + year)


# In[49]:


# Set the index to start at 0
index = 0

# Create the dictionary for the months
tt = {'Jan': 0, 'Feb': 0, 'Mar': 0 }


# In[50]:


tt


# In[51]:


data = {'Description':  ['Sales'],
        '14-Feb': ['3000'],
        '19-Mar': ['1200'],
        '22-Mar': ['1500']}

df = pd.DataFrame (data, columns = ['Description', '14-Feb', '19-Mar', '22-Mar'])

print (df)


# In[61]:


# Initialize an empty dictionary to store the totals for each month
tt = {}

# Initialize the index
index = 0

# Create a for loop that will iterate over the date and amount values in the dataset
for date, amount in df.items():
    # Split the day and month from the date string
    if index > 0:
        day, month = date.split('-')
        
        # If the month doesn't exist in the dictionary, add it with an initial value of 0
        if month not in tt:
            tt[month] = 0
        
        # Add the amount to the corresponding month
        tt[month] += float(amount[0])
    
    # Increment the index in each iteration
    index += 1

# Print the final result
print(tt)


# In[62]:


df1 = pd.DataFrame()


# In[63]:


totals = {'Jan': 0, 'Feb': 0, 'Mar': 0}
calendar = {'01': 'Jan', '02': 'Feb', '03': 'Mar'}


# In[65]:


totals = {'Jan': 0, 'Feb': 0, 'Mar': 0}
calendar = {'01': 'Jan', '02': 'Feb', '03': 'Mar'}

# Iterate over the DataFrame with .items() method
for date, amount in df1.items():
    day, month, year = date.split('-')
    
    # Map the numeric month to the corresponding name using the calendar dictionary
    month_name = calendar[month]
    
    # Add the amount to the corresponding month's total
    totals[month_name] += float(amount[0])

# Print the totals for each month
print(totals)


# In[66]:


df1


# In[67]:


df2 = pd.DataFrame()


# In[68]:


for date, amount in df2.items():
        day, month, year = date.split('/')
        totals[calendar[month]] += float(amount[0])

print(totals)


# In[69]:


df2


# In[70]:


# Create the combined list for sales and probability
sales_probability = ['0|0.05', '200|0.10', '300|0.40', '500|0.20', '800|0.25'] 
weighted_probability = 0

# Create a for loop to calculate the weighted probability
for pair in sales_probability:
    parts = pair.split('|')
    weighted_probability += float(parts[0]) * float(parts[1])

# Print the weighted probability result
print("The weighted probability is {}.".format(weighted_probability))


# In[71]:


# Create the computevariance function
def computevariance(amount, sentiment):
 if (sentiment < 0.6):
  res = amount + (amount * 0.02)
 elif (sentiment > 0.8):
  res = amount + (amount * 0.07)
 else:
  res = amount + (amount * 0.05)
 return res


# In[72]:


amount=500


# In[73]:


amount


# In[74]:


# Compute the variance for jan, feb and mar
jan = computevariance(500, 0.5)
feb = computevariance(500, 0.65)
mar = computevariance(500, 0.85)

print("The forecast sales considering variance due to market sentiment is {} for Jan, {} for Feb, and {} for Mar.".format(jan, feb, mar))


# In[75]:


base_sales_price=15


# In[76]:


sales=750


# In[77]:


# Set the Sales Dependency
if sales >= 350:
    sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
else:
    sales_dep = sales * base_sales_price

# Print the results
print("The sales dependency is {} USD.".format(sales_dep))


# In[78]:


base_cost_price=7


# In[79]:


# Set the Cost Dependency
if sales >= 500:
    cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
else:
    cost_dep = sales * base_cost_price
    
# Print the results
print("The cost dependency is {} USD.".format(cost_dep))


# In[80]:


# Create the sales_usd list
sales_usd = [700, 350, 650]


# In[81]:


# Create the sales_usd list
sales_usd = [700, 350, 650]

# Create the if statement to calculate the forecast_gross_profit
for sales in sales_usd:
    if sales > 350:
        sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
    else:
        sales_dep = sales * base_sales_price
    if sales > 500:
        cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
    else:
        cost_dep = sales * base_cost_price
    forecast_gross_profit = sales_dep - cost_dep
    # Print the result
    print("The gross profit forecast for a sale unit value of {} is {} USD.".format(sales, forecast_gross_profit))
    


# In[82]:


emp_leave = 6


# In[83]:


# Set the admin dependency
if emp_leave > 0:
    admin_dep = emp_leave  * 80

# Print the results
print("The admin dependency for August is {} USD.".format(admin_dep))


# In[84]:


admin_usd = [1500, 1500, 1500]
emp_leave = [6, 6, 0]
forecast_gross_profit = [4850, 2800, 4600]
index = 0

for admin in admin_usd:
    temp = emp_leave[index]
    if temp > 0:
        admin_dep = emp_leave[index]* 80 + admin
    else: 
         admin_dep = admin 
    forecast_net_profit = forecast_gross_profit[index] - admin_dep
    print(forecast_net_profit)
    index += 1
    print("The forecast net profit is:")


# In[85]:


base_cost_price = 7
base_sales_price = 15


# In[86]:


def dependencies(base_cost_price, base_sales_price, sales_usd):
    res = []
    for sales in sales_usd:
        if sales >= 350:
            sales_dep = (350 * base_sales_price) + ((sales - 350) * (base_sales_price - 1))
        else:
            sales_dep = sales * base_sales_price
        if sales >= 500:
            cost_dep = (500 * base_cost_price) + ((sales - 500) * (base_cost_price + 2))
        else:
            cost_dep = sales * base_cost_price
        res.append(sales_dep - cost_dep)
    return res


# In[87]:


forecast1 = dependencies(7, 15, [700, 350, 650])


# In[88]:


forecast2 = dependencies(7, 15, [700, 220, 520])

print("The original forecast scenario is {}:".format(forecast1))
print("The alternative forecast scenario is {}:".format(forecast2))


# In[89]:


# Set the two results
forecast1 = dependencies(7, 15, [700, 350, 650])
forecast2 = dependencies(7, 15, [700, 220, 520])

# Create an index and the gap analysis for the forecast
index = 0
for value in forecast2:
    print("The gap between forecasts is {}".format(value - forecast1[index]))
    index += 1


# In[90]:


# Import the data
netflix_f_is = pd.read_csv("C:/Users/jatin/Downloads/Netflix.csv")


# In[91]:


netflix_f_is


# In[92]:


# Create a filter to select the sales row from the netflix_f_is dataset
sales_metric = ['Sales']

# Filter for rows containing the Sales metric
filtered_netflix_f_is = netflix_f_is[netflix_f_is.metric.isin(sales_metric)]

# Extract the 2019 Sales forecast value
forecast1 = netflix_f_is['2019 fc'].iloc[0]

# Print the resulting forecast
print("The sales forecast is {}.".format(forecast1))


# In[93]:


n_subscribers_per_pp=500


# In[94]:


n_subscribers_per_pp=500


# In[95]:


# Set the success percentage to 78%
pct_success = 0.78

# Calculate the dependency for the subscriber base
n_subscribers = n_subscribers_per_pp * pct_success

# See the result
print("The dependency for the subscriber base is {}.".format(n_subscribers))


# In[96]:


# From previous steps
sales_metric = ['Sales']
filtered_netflix_f_is = netflix_f_is[netflix_f_is.metric.isin(sales_metric)]
forecast1 = filtered_netflix_f_is["2019 fc"].iloc[0]
pct_success = 0.78
n_subscribers = n_subscribers_per_pp * pct_success

# Calculate the ratio between forecast sales and subscribers
sales_subs_ratio = forecast1 / n_subscribers

# See the result
print("The ratio between subscribers and sales is 1 subscriber equals ${:.2f}.".format(sales_subs_ratio))


# In[97]:


# Set the proportion of successes to 65%
pct_success2 = 0.65

# Calculate the number of subscribers
n_subscribers2 = n_subscribers_per_pp * pct_success2

# Calculate the new forecast
forecast2 = n_subscribers2 * sales_subs_ratio


# In[98]:


forecast2


# In[99]:


# From previous step
pct_success2 = 0.65
n_subscribers2 = n_subscribers_per_pp * pct_success2
forecast2 = n_subscribers2 * sales_subs_ratio

# Insert a column named AltForecast, containing forecast2
filtered_netflix_f_is.insert(len(filtered_netflix_f_is.columns), 'AltForecast', forecast2)

# Insert a column named Gap, containing the difference
filtered_netflix_f_is.insert(len(filtered_netflix_f_is.columns), 'Gap', (forecast1-forecast2))

# See the result
print(filtered_netflix_f_is)


# In[4]:


import streamlit as st

# A function to compute variance, which might have been used in the notebook
def computevariance(base_value, multiplier):
    return base_value * (1 + multiplier)

# Interactive input for amount
amount = st.number_input('Enter the base amount', value=500)

# Compute the variance for Jan, Feb, and Mar based on user input
jan = computevariance(amount, 0.5)
feb = computevariance(amount, 0.65)
mar = computevariance(amount, 0.85)

# Display the result
st.write(f"The forecast sales considering variance due to market sentiment is {jan} for Jan, {feb} for Feb, and {mar} for Mar.")

# Placeholder for other logic from the notebook
# Example code from sales and COGS dependencies can be added here

# Interactive sales dependency input
sales_dep = st.text_area('Sales Dependency Instructions', '''Set sales dependency as follows:
- The sale price is net after 1 USD commission.
- Commissions paid increase from 1 USD to 2 USD for every unit sold above 350.''')

st.write("Sales Dependency Explanation:")
st.write(sales_dep)


# In[6]:


import streamlit as st

# Function to compute variance
def computevariance(base_value, multiplier):
    return base_value * (1 + multiplier)

# Input for base amount
amount = st.number_input('Enter the base amount', value=500)

# Compute the variance for Jan, Feb, and Mar based on user input
jan = computevariance(amount, 0.5)
feb = computevariance(amount, 0.65)
mar = computevariance(amount, 0.85)

# Display the forecast results
st.write(f"The forecast sales considering variance due to market sentiment is {jan} for Jan, {feb} for Feb, and {mar} for Mar.")


# In[9]:


import streamlit as st
import pandas as pd
import pandas_datareader as web

# Your code logic here
# For example:
def compute_variance(base_value, multiplier):
    return base_value * (1 + multiplier)

# Streamlit app layout
st.title("Sales Forecasting App")

# Input field for base amount
amount = st.number_input('Enter the base amount', value=500)

# Compute forecast
jan = compute_variance(amount, 0.5)
feb = compute_variance(amount, 0.65)
mar = compute_variance(amount, 0.85)

# Display results
st.write(f"Forecast sales for Jan: {jan}, Feb: {feb}, Mar: {mar}")


# In[ ]:




