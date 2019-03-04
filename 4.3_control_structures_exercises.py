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
else:
    while count <= some_number:
        print(count)
        count += 1
