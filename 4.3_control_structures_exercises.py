''' #1 : The input function can be used to prompt for input and use that 
input in your python code. Prompt the user to enter a positive number 
and write a loop that counts from 0 to that number. (Hints: first make 
sure that the value the user entered is a valid number, also note that 
the input function returns a string, so you'll need to convert this to 
a numeric type.)'''

count = 0
some_number = int(input('hey guy please to enter some positive int thanks: '))
if some_number <= 0:
    print('please follow instructions next time man why')
# else:
#     while count <= some_number:
#         print(count)
#         count += 1
else:
    for n in range(1,some_number+1):
        print(n)
'''#2: Write a program that prompts the user for a positive integer.
 Next write a loop that prints out the numbers from the number 
 the user entered down to 1.'''
 
some_number = int(input('hey guy please to enter some positive int thanks: '))
count = some_number
if some_number <= 0:
    print('please follow instructions next time man why')
else:
    while count >= 1:
        print(count)
        count -= 1

''' #3: Create a list of dictionaries where each dictionary represents 
a book that you have read. Each dictionary in the list should have the 
keys title, author, and genre. Loop through the list and print out 
information about each book.'''

library = [{'title': 'Moby Dick', 'author': 'Dwayne Johnson', 'genre': 'whalecore'}, 
{'title': 'JimJams', 'author': 'Jims Guide to Jams', 'genre': 'self-help'},
 {'title': 'Atlas Shrugged', 'author': 'Actually the Devil', 'genre': 'fiction'},
  {'title': 'The Road', 'author': 'Hardcastle Mcormick', 'genre': 'sadness'}]
for feature in library:
    print('Title: ' + feature['title'])
    print('Author: ' + feature['author'])
    print('Genre: ' + feature['genre'])


'''Prompt the user to enter a genre, then loop through your books list 
and print out the titles of all the books in that genre.'''

ux_genre = input('Pls2enter a book genre plsthx: ').lower()
print('List of all books in library with designated genre: ')
for feature in library:
    if ux_genre == feature['genre'].lower():
        print('Title: ' + feature['title'])
        print('Author: ' + feature['author'])
        print('Genre: ' + feature['genre'])
    