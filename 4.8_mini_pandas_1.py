import numpy as np
import pandas as pd

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

student_number = list(range(1, len(students) + 1))
shoe_sizes = np.random.choice(np.arange(6, 14, 0.5), len(students))
side_of_classroom = np.random.choice(['left', 'right'], len(students))
favorite_number = np.random.randint(1, 11, len(students))

#2: Use the code to generate a dataframe for students named students

students = pd.DataFrame({'name': students, 
                        'student_number': student_number,
                        'shoe_sizes': shoe_sizes,
                        'side_of_classroom': side_of_classroom, 
                        'favorite_number': favorite_number
                        })

# ~~Walkthrough: 
# df = pd.DataFrame(dict(name=students,
#                       student_no=student_number, 
#                       shoe_sizes=shoe_sizes, 
#                       side=side_of_classroom,
#                       favorite_number = favorite_number))

# 3: Print out the shape of the data frame
print('Shape of Students: ')
print(students.shape)
print()

# 4: Print out the names of the columns of the dataframe.
print('Columns in Students: ')
print(students.columns)
print()

# 5: Rename 2 of your columns in the dataframe

print('Let\'s rename student_number and favorite_number to truncate \'ber\': ')
students.rename(columns = {'student_number': 'student_num', 'favorite_number': 'favorite_num'}, inplace=True)
print(students)
print()

# 6: create a new data frame based on the one you have.  
# The new data frame should only have columns for
#  shoe size and side of the classroom

shoe_side = pd.DataFrame({'shoe size': students.shoe_sizes, 
                            'side_of_classroom': students.side_of_classroom
                        })

# ~~Walkthrough:
# students[['side_of_classroom', 'shoe_sizes']]

print('Let\'s see a new dataframe with only shoe size and side of class: ')
print(shoe_side)
print()

# 7: Create a new data frome that has all of the columns, but only 5 rows

df_5_rows = students.iloc[0:5]
print('DataFrame with only the first five rows: ')
print(df_5_rows)
print()
# OR: students.head()

# 8: Create a new data frame that has only columns for 
# only favorite number and name, and only includes 7 rows.
sub_frame = students.loc[0:6,['name','favorite_num']]
print(sub_frame)
print()

# ~~Walkthrough:
# students[['favorite_num','student_name']].head(7)
# OR:
# students.sample(7)[['favorite_num', 'student_name']]

# 9: Create a new column for the ratio of shoe size to favorite number.
#  Name this ss_to_fn

ss_to_fn = students.shoe_sizes / students.favorite_num
students['ss_to_fn'] = ss_to_fn
print(students)
print()

# 10: Create a new column that contains the z-score for the shoe size
def z_score(shoe):
    z = (shoe - students.shoe_sizes.mean()) / students.shoe_sizes.std()
    return z
students['shoe_z_score'] = students.shoe_sizes.apply(z_score)

# ~~Walkthrough method:
# students['shoe_z_score'] = (shoe - students.shoe_sizes.mean()) / students.shoe_sizes.std()

print(students)
print()
# 11: Transform the side_of_the_classroomn columns such that the valiues
# are either R or L
def r_or_l(some_string):
    if some_string == 'right':
        return 'R'
    else:
        return 'L'

students['side_of_classroom'] = students.side_of_classroom.apply(r_or_l)

# ~~Walkthrough example:
#students.side.str[0].str.upper()

print(students)
print()

# 12: Find the names of all the students that have a shoe size 
# greater than the 3rd quartile of shoe sizes (You can use the 
# .quantile method on a series for this)

# large_feet = students.shoe_sizes.quantile(0.75)
# def big-shoes(size):
#     if size >= large_feet:
#         return size

big_feet_students = students[students.shoe_sizes >= students.shoe_sizes.quantile(0.75)]
print(big_feet_students)
print()
# 13:Find the names of all the students that have a shoe size less than the 
 # 1st quartile of shoe sizes

small_feet_students = students[students.shoe_sizes <= students.shoe_sizes.quantile(0.25)]
print(small_feet_students)
print()