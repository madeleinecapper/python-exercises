import numpy as np
import pandas as pd
import os
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

students = pd.DataFrame({'name': students, 
                        'student_number': student_number,
                        'shoe_sizes': shoe_sizes,
                        'side_of_classroom': side_of_classroom, 
                        'favorite_number': favorite_number
                        })

## 1: Save the students data to a csv file

data = students.to_csv('students.csv', encoding='utf-8', index=False)

## 2: Read the data from the csv file back into pandas.  
# What do you notice?

df = pd.read_csv('students.csv', sep=',')
print(df)

# separator keys are necessary to divide columns of datafranme.

# 3: Create a data frame based on the profiles.json file. 
# Explore this data frame's structure

df_jsn = pd.read_json('profiles.json')
print(df_jsn)
print()

for file in('students.csv'):
    try: 
        os.remove(file)
    except FileNotFoundError:
        pass

# 4 Write the code necessary to create a data frame based on 
# the results of a SQL query to the numbers database.

def get_connection(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)

from env import user, host, pw

import pandas as pd

conn = get_connection('numbers', user, host, pw)
qry = 'SELECT * FROM numbers'

df_sq = pd.read_sql(qry, conn)
print(df_sq)