# # Numpy Exercises

# ## Use the following code for the questions:
# ## a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

import numpy as np


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### How many negative numbers are there?

neg_array = a[(a < 0)]
print('A 1 dimensional array of all the negative elements of a looks like this: \n')
print(neg_array)


neg_count = (a < 0).sum()
print('There are {} negative numbers in a'.format(neg_count))


# ### How many positive numbers are there?

pos_array = a[(a > 0)]
print('A 1 dimensional array of all the positive elements of a looks like this: \n')
print(pos_array)


pos_count = (a > 0).sum()
print('There are {} positive numbers in a'.format(pos_count))


# ### If you were to add 3 to each data point, how many positive numbers would there be?

a_plus_3 = a + 3
print('An array that looks like [a] but each point is 3 greater: ')
print(a_plus_3)

pos_plus_3 = a_plus_3[(a_plus_3 > 0)]
print(
    'A 1 dimensional array of all the positive elements of [a + 3] looks like this: \n')
print(pos_plus_3)

pos_count_3 = (a_plus_3 > 0).sum()
print('There are {} positive numbers in a'.format(pos_count_3))


# ### If you squared each number, what would the new mean and standard deviation be?

a_squared = a ** 2
print('A version of [a] with all elements squared: ')
print(a_squared)

a_mean = a.mean()
dev = a.std()
print('The mean of [a] is {} and the standard deviation is {}'.format(
    a_mean, dev))
squared_mean = a_squared.mean()
squared_dev = a_squared.std()
print('The mean of [a^2] is {} and the standard deviation is {}'.format(
    squared_mean, squared_dev))


# ### A common statistical operation on a dataset is called centering. This means to adjust the data such that the center of data is at 0.  This is done by subtracting the mean from each data point. Center the data set.

print('[a] still looks like this: ')
print(a)
print(f'The mean of a is {a_mean}')
a_normed = a - int(a_mean)
print('A centered version of [a] looks like this: ')
print(a_normed)


# ### Calculate the z-score for each data point.  Recall that the z-score is given by z = (x − μ) / σ

z_ray = (a - a_mean) / dev
print(f'Z-scores for each element in [a] represented by: \n{z_ray}')


# ### #8: More Numpy Exercises!

# ### Use python's built in functionality/operators to determine the following:
#
# ### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ### Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = 0
for n in a:
    sum_of_a += n
print(sum_of_a)


# ### Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min_of_a)


# ### Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum_of_a / len(a)
print(mean_of_a)


# ### Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = 1
for n in a:
    product_of_a *= n
print(product_of_a)


# ### Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = [n ** 2 for n in a]
print(squares_of_a)


# ### Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = [n for n in a if n % 2 == 1]
print(odds_in_a)


# ### Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = [n for n in a if n % 2 == 0]
print(evens_in_a)


# ### What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# #### Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

sum_of_b = 0
for l in b:
    for n in l:
        sum_of_b += n
print(sum_of_b)


# ### Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# #### sum_of_b = 0
# #### for row in b:
# ####    sum_of_b += sum(row)

b = np.array(b)

sum_of_b = b.sum()
print(sum_of_b)


# ### Exercise 2 - refactor the following to use numpy.

# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = b.min()
print(min_of_b)


# ### Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
print(max_of_b)


# ### Exercise 4 - refactor the following using numpy to find the mean of b

# mean_of_b = (sum(b[0]) + sum(b[1])) / (len([b[0]]) + len(b[1]))
mean_of_b = b.mean()
print(mean_of_b)


# ### Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

#product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = b.prod()
print(product_of_b)


# ### Exercise 6 - refactor the following to use numpy to find the list of squares

# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = b ** 2
print(squares_of_b)


# ### Exercise 7 - refactor using numpy to determine the odds_in_b

# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b[b % 2 == 1]
print(odds_in_b)


# ### Exercise 8 - refactor the following to use numpy to filter only the even numbers

# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# ### Exercise 9 - print out the shape of the array b.

print(b.shape)


# ### Exercise 10 - transpose the array b.

b_tp = np.transpose(b)
print(b_tp)


b_one_dim = b.reshape(1, 6)
print(b_one_dim)


# ### Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b_six_dim = b.reshape(6, 1)
print(b_six_dim)


# ############################ Setup #3 #######################
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)


# ### Exercise 1 - Find the min, max, sum, and product of c.

min_c = c.min()
max_c = c.max()
sum_c = c.sum()
prod_c = c.prod()
print(min_c)
print(max_c)
print(sum_c)
print(prod_c)


# ### Exercise 2 - Determine the standard deviation of c.

c_dev = c.std()
print(c_dev)


# ### Exercise 3 - Determine the variance of c.

c_var = c.var()
print(c_var)


# ### Exercise 4 - Print out the shape of the array c

print(c.shape)


# ### Exercise 5 - Transpose c and print out transposed result.

c_tpse = np.transpose(c)
print(c_tpse)


# ### Exercise 6 - Multiply c by the c-Transposed and print the result.

c_by_ct = c * c_tpse
print(c_by_ct)


# ### Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

sum_prod = c_by_ct.sum()
print(sum_prod)


# ### Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

prod_prod = c_by_ct.prod()
print(prod_prod)


# ###################### Set-up #4: ##################################

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# ### Exercise 1 - Find the sine of all the numbers in d

d = np.array(d)
sin_d = np.sin(d)
print(sin_d)


# ### Exercise 2 - Find the cosine of all the numbers in d

cs_d = np.cos(d)
print(cs_d)


# ### Exercise 3 - Find the tangent of all the numbers in d

tn_d = np.tan(d)
print(tn_d)


# ### Exercise 4 - Find all the negative numbers in d

neg_d = d[d < 0]
print(neg_d)


# ### Exercise 5 - Find all the positive numbers in d

pos_d = d[d > 0]
print(pos_d)


# ### Exercise 6 - Return an array of only the unique numbers in d.

uni_d = np.unique(d)
print(uni_d)


# ### Exercise 7 - Determine how many unique numbers there are in d.

sum_u = np.unique(d).size
print(sum_u)

# ### Exercise 8 - Print out the shape of d.

print(d.shape)


# ### Exercise 9 - Transpose and then print out the shape of d.

d_tpse = np.transpose(d)
print(d_tpse.shape)


# ### Exercise 10 - Reshape d into an array of 9 x 2

shaped_d = d.reshape(9, 2)
print(shaped_d)
