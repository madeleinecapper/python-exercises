# ## Use pandas to convert the following list to a numeric series:

from pydataset import data
import numpy as np
import pandas as pd

dol_list = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']


dol_frame = pd.Series([float(n.replace('$','').replace(',','')) for n in dol_list])
print('list as a series: ')
print(dol_frame)
print()


# ## Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

df = data('mpg') # load the dataset and store it in a variable
print(data('mpg', show_doc=True)) # view the documentation for the dataset

# ### How many rows and columns are there?
print('\nA data frame with 234 rows and 11 variables\n')



# ### What are the data types?

# manufacturer: string, model: string,displ: float, year: int, cyl: int, 
# trans: str, drv: str, cty: int, hwy: int, fl: str, class: str
print(df.dtypes)


#  ### Do any cars have better city mileage than highway mileage?

df['cty_over_hwy'] = df.cty > df.hwy
count_over_hwy = df.groupby('cty_over_hwy')['model'].count()
print(count_over_hwy)
print('No: all 234 cars have better highway milage')
print()


# ### Create a column named milelage_difference this column should contain the difference between highway and city milelage for each car.
del df['cty_over_hwy']

df['milelage_difference'] = df.hwy - df.cty
print(df[['model', 'milelage_difference']])
print()

# ### On average, which manufacturer has the best miles per gallon?

del df['milelage_difference']
df['mpg_avg'] = (df.cty + df.hwy) / 2
avg_mpg = df.groupby('manufacturer')['mpg_avg'].mean().sort_values(ascending=False)
print(avg_mpg)
print('\n Honda has the best average miles per gallon\n')


# ### How many different manufacturers are there?

del df['mpg_avg']

manus = df.groupby('manufacturer')['manufacturer'].count()
print(manus)
print(f'There are {manus.shape[0]} manufacturers')


# ### How many different models are there?

mods = df.groupby('model')['model'].count()
print(mods)
print(f'There are {(mods.shape)[0]} models')


# ### Do automatic or manual cars have better miles per gallon?

df['mpg_avg'] = (df.cty + df.hwy) / 2
df['automatic'] = df.trans.str.startswith('auto')
avg_mpg = df.groupby('automatic')['mpg_avg'].mean().sort_values()
print(avg_mpg)
print('manual vehicles have a better mpg from this sample at 22.22 mpg')
print()


# ## Load the mammals dataset

df = data('Mammals') # load the dataset and store it in a variable
print(data('Mammals', show_doc=True)) # view the documentation for the dataset

# How many rows and columns are there?
print(df.shape)
# 107 rows, 4 columns

# What are the data types?
print(df.dtypes)

# What is the the weight of the fastest animal?
weights = df[['weight','speed']].sort_values(by='speed', ascending = False).iloc[0:1]
print(weights)

# What is the overal percentage of specials?
grouped_specs = df.groupby('specials').count().apply(lambda x: 100* x /float(x.sum()))
print(grouped_specs['weight'])

# How many animals are hoppers that are above the median speed? What percentage is this?
df['above_med'] = df.speed > df.speed.agg(np.quantile(0.5))
num_fast_hops = df.groupby('above_med')[['hoppers']].count()
perc_fast_hops = df.groupby('above_med')[['hoppers']].count().apply(lambda x: 100* x /float(x.sum()))
print(num_fast_hops)
print()
print(perc_fast_hops)
print()

def get_db_url(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)

from env import user, host, pw

import pandas as pd

conn = get_db_url('employees', user, host, pw)

emp_df = pd.read_sql('SELECT * FROM employees', conn)
titles_df = pd.read_sql('SELECT * FROM titles', conn)

# of employees with each title
import matplotlib.pyplot as plt
num_titles = titles_df.groupby('title')['emp_no'].count()
print(num_titles)
num_titles.plot.bar()
plt.show()

# Visualize how frequently employees change titles.
title_changes = titles_df.groupby('emp_no')[['title']].count()
title_changes.plot.hist()
plt.show()

# Join the employee and titles datasets

joined_df = emp_df.set_index('emp_no').join(titles_df.set_index('emp_no'))

print(joined_df)
print()

# For each title, find the hire date of the employee that was hired most recently with that title.
joined_df['hire_date'] = pd.to_datetime(joined_df.hire_date)
new_emps_by_title = joined_df.groupby('title')['hire_date'].max()
print(new_emps_by_title)
print()

conn = get_db_url('chipotle', user, host, pw)


chip_df = pd.read_sql('SELECT * FROM orders', conn)


chip_df['item_float'] = chip_df.item_price.str.replace('$','').str.strip().astype(float)\

# Total price for each order
totaled_orders = chip_df.groupby('order_id')['item_float'].sum()
print(totaled_orders)
print()

# Most popular 3 items?
most_pop = chip_df.groupby('item_name')['id'].count().sort_values(ascending = False).iloc[0:3]
print(most_pop)
print()


# Which item has produced the most revenue?
most_muns = chip_df.groupby('item_name')['item_float'].sum().sort_values(ascending = False).iloc[0:1]
print(most_muns)