'''#1a: prompt the user for a day of the week, 
print out whether the day is Monday or not'''

day_of_week = input('What day of the week is it today? ')
if day_of_week.lower() == 'monday':
     print('LASAGNA')

'''#1b: prompt the user for a day of the week,
 print out whether the day is a weekday or a weekend'''

day_of_week = input('What day of the week is it today? ')
if day_of_week.lower() in('monday', 'tuesday', 'wednesday', 'thursday', 'friday'):
     print('WERK DAY')
elif day_of_week.lower() in('saturday', 'sunday'):
    print('WEEKEND FUN TIMES WOW')
else:
    print('HI CAN YOU FOLLOW INSTRUCTIONS THANK')

'''create variables and make up values for

the number of hours worked in one week
the hourly rate
how much the week's paycheck will be
write the python code that calculates the weekly paycheck. 
You get paid time and a half if you work more than 40 hours'''

weekly_hours_worked = float(input("How many hours did you work this week? "))
garbage_rate = float(input("What do you make per hour: $"))
paycheck = 0
if weekly_hours_worked <= 40.0:
    paycheck = weekly_hours_worked*garbage_rate
    print(f'Wow friendguy you made {"{0:.2f}".format(round(paycheck,2))} dollars')
else:
    paycheck = 40.0 * garbage_rate
    paycheck += (weekly_hours_worked - 40.00)*garbage_rate*1.5
    print(f'OVERTIME CITY BRUH YOU MADE {"{0:.2f}".format(round(paycheck,2))} DOLLHAIRS')

'''#2a: Create an integer variable i with a value of 5.
Create a while loop that runs so long as i is less than or equal to 15
Each loop iteration, output the current value of i, then increment i by one.'''
print('this is the first subexercise 2a and it is a very simple loop here it is thanks')
i = 5
while i <= 15:
    print(i, end = ' ')
    i +=1

print(' ')
'''Create a while loop that will count by 2's 
starting with 0 and ending at 100. 
Follow each number with a new line.'''

print('count by 2s starting with 0 ending at 100')
i = 0
while i <= 100:
    print(i)
    i +=2

print('backwards by 5s from 100 to -10')
i -= 2
while i >= -10:
    print(i)
    i -= 5

new_i = 2
while new_i < 1000000:
    print(new_i, end = ' ')
    new_i = new_i**2
print(' ')
i = 100
while i >= 5:
    print(i)
    i -= 5
'''#2b: For Loops
Write some code that prompts the user for a number
 then shows a multiplication table up through 10 for that number.'''

ux_num = input('Hey guy enter a number, make it an integer pls: ')
while not ux_num.isdigit():
    ux_num = input('integer please: ')
ux_num = int(ux_num)
for i in range(1,11):
    print(f'{ux_num} X {i} = {ux_num*i}')

numstring = ''
for i in range(1,10):
    numstring = str(i)*i
    print(numstring)

'''#2c: break and continue
Prompt the user for an odd number between 1 and 50.
 Use a loop and a break statement to continue prompting the user 
 if they enter invalid input. 
 (Hint: use the isdigit method on strings to determine this). 
 Use a loop and the continue statement to output all the odd numbers 
 between 1 and 50, except for the number the user entered.'''

ux_odd = input('Please enter a positive odd number less than 50: ')
while not ux_odd.isdigit():
    ux_odd = input('Please enter a positive odd number less than 50: ')
while (int(ux_odd) > 50) or (int(ux_odd) % 2 == 0):
    ux_odd = input('Please enter a positive ODD number LESS than 50: ')
for i in range(1,51):
    if int(ux_odd) == i:
         print("SKIPPING")
         continue
    elif i%2 == 0:
        continue
    else:
        print(f'Here is an odd number: {i}')

''' #2d : The input function can be used to prompt for input and use that 
input in your python code. Prompt the user to enter a positive number 
and write a loop that counts from 0 to that number. (Hints: first make 
sure that the value the user entered is a valid number, also note that 
the input function returns a string, so you'll need to convert this to 
a numeric type.)'''

count = 0
some_number = input('hey guy please to enter some positive int thanks: ')
while not some_number.isdigit():
    some_number = input('I SAID NUMBER PLEASE: ')
# while count <= some_number:
#     print(count)
#     count += 1
for n in range(1, int(some_number)+1):
    print(n)

'''#2e: Write a program that prompts the user for a positive integer.
 Next write a loop that prints out the numbers from the number 
 the user entered down to 1.'''
 
some_number = input('hey guy please to enter some positive int thanks: ')
while not some_number.isdigit():
    some_number = input('I SAID NUMBER PLEASE: ')
count = int(some_number)
while count >= 1:
    print(count)
    count -= 1

'''#3: FIZZBUZZ:
One of the most common interview questions
for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test 
basic looping and conditional logic skills.

Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".'''

for i in range(1,101):
    if i%3 == 0 or i%5 == 0:
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        else:
            print('Buzz')
    else:
        print(i)

'''Display a table of powers
enter an int
display a table of squares abnd cubes from 1 to the value entered
ask user if want to continue
assume valid entries
only continue with consent'''
cust_num = int(input('What number would you like to go up to? :'))
print('Here is your table!')
print('number | squared | cubed')
print('------ | ------- | -----')
for i in range(1,cust_num+1):
    print("{0:7}".format(f'{i}')+ '|' + "{0:9}".format(f'{i**2}')+ '|' + f'{i**3}')
feedback = input('Would you like to do this with a different number y/n: ')
while feedback == 'y':
    cust_num = int(input('What number would you like to go up to? :'))
    print('Here is your table!')
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1,cust_num+1):
        print("{0:7}".format(f'{i}')+ '|' + "{0:9}".format(f'{i**2}')+ '|' + f'{i**3}')
    feedback = input('Would you like to do this with a different number y/n: ')

'''#5: Convert a given number grade into a letter grade
prompt user for grade betweebn 0 and 100
display corresponding letter grade
prompt user to continue
assume user enters valid integers for grades
application should only continue with consent '''
raw_grade = int(input('Please input a numerical grade (0-100): '))
if raw_grade >= 88:
    print('A')
elif raw_grade >= 80:
    print('B')
elif raw_grade >= 67:
    print('C')
elif raw_grade >= 60:
    print('D')
else:
    print('F')
consent = input('Would you like to input another grade? y/n: ')
while consent == 'y':
    raw_grade = int(input('Please input a numerical grade (0-100): '))
    if raw_grade >= 88:
        print('A')
    elif raw_grade >= 80:
        print('B')
    elif raw_grade >= 67:
        print('C')
    elif raw_grade >= 60:
        print('D')
    else:
        print('F')
    consent = input('Would you like to input another grade? y/n: ')

''' #6: Create a list of dictionaries where each dictionary represents 
a book that you have read. Each dictionary in the list should have the 
keys title, author, and genre. Loop through the list and print out 
information about each book.'''

library = [{'title': 'Moby Dick', 'author': 'Dwayne Johnson', 'genre': 'whalecore'}, 
{'title': 'Jims Guide to Jams', 'author': 'JimJams', 'genre': 'self-help'},
 {'title': 'Atlas Shrugged', 'author': 'Actually the Devil', 'genre': 'fiction'},
  {'title': 'The Road', 'author': 'Hardcastle Mcormick', 'genre': 'sadness'},
  {'title': 'A Place to Go', 'author': 'Diego von Traphouse', 'genre': 'self-help'}, 
  {'title': 'Five Tings', 'author': 'Fakey McPatois', 'genre': 'fiction'},
  {'title': 'Handfuls of Fiddlefaddle', 'author': 'Jim Jackal', 'genre': 'Historical Fiction'}, 
  {'title': 'Old Fashioned Jollops', 'author': 'Henry of Henrys Old Fashioned Jollops', 'genre': 'whalecore'}]
for feature in library:
    print('Title: ' + feature['title'])
    print('Author: ' + feature['author'])
    print('Genre: ' + feature['genre'])


'''#6a Prompt the user to enter a genre, then loop through your books list 
and print out the titles of all the books in that genre.'''

ux_genre = input('Pls2enter a book genre plsthx: ').lower()
while ux_genre.isdigit():
    ux_genre = input('you could try a word, dude: ')
print('List of all books in library with designated genre: ')
for feature in library:
    if ux_genre == feature['genre'].lower():
        print('Title: ' + feature['title'])
        print('Author: ' + feature['author'])
        print('Genre: ' + feature['genre'])
    