# ## Calculate the mean, median, min, and max for the shoe sizes and favorite numbers

import numpy as np
import pandas as pd

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


stu_mean = students.shoe_sizes.agg(np.mean)
print(stu_mean)
print()


stu_min = students.shoe_sizes.agg(np.min)
print(stu_min)
print()

stu_max = students.shoe_sizes.agg(np.max)
print(stu_max)
print()


mean_fav_num = students.favorite_number.agg(np.mean)
print(mean_fav_num)

max_fav_num = students.favorite_number.agg(np.max)
print(max_fav_num)


min_fav_num = students.favorite_number.agg(np.min)
print(min_fav_num)

# ###  2: Sort the data frame by the students shoe size

sorted_shoes = students.sort_values(by='shoe_sizes')
print(sorted_shoes)
print()

# ### Sort the data frame by the side of the classroom, then by their student number


sorted_sides = students.sort_values(by='student_number').sort_values(by='side_of_classroom')
print(sorted_sides)
print()

# ### Find the number of students on each side of the classroom


num_by_side = students.groupby(side_of_classroom)['name'].count()
print(num_by_side)

# ### Find the average shoe size for each side of the classroom

avg_shoe_by_side = students.groupby(side_of_classroom)['shoe_sizes'].mean()
print(avg_shoe_by_side)
print()

# ### Find the maximum favorite number for each side of the classroom


max_by_side = students.groupby(side_of_classroom)['favorite_number'].max()
print(max_by_side)
print()

# ### Create a pie chart that visualizes the number of students on each side of the classroom.


import matplotlib.pyplot as plt
students.groupby(side_of_classroom)['name'].count().plot.pie()
plt.show()

# ### Create a histogram of the shoe sizes in the classroom

students.shoe_sizes.plot.hist()
plt.show()

# ### Create a histogram of the favorite numbers in the classroom

students.favorite_number.plot.hist()
plt.show()

# ### Create a scatter plot of shoe size vs favorite number

students.plot.scatter(x='shoe_sizes', y='favorite_number')
plt.show()