import os
with open('4.5_import_exercises.py') as f:
    lines = f.read()
lines = lines.split('\n')
# print(lines)
new_lines = []
count = 1
for line in lines:
    new_lines.append(str(count) + '    ' + line)
    count += 1

[print(line) for line in new_lines]

grocery_list = ['tofu', 'broccoli', 'noodles']


def make_grocery_list(groceries):
    with open('my_grocery_list.txt', 'w') as f:
        for item in groceries:
            f.write('%s\n' % item)


def show_grocery_list(groce_file):
    with open(groce_file) as f:
        lines = f.read()
    lines = lines.split('\n')
    new_groceries = []
    for line in lines:
        new_groceries.append(line)
    [print(line) for line in new_groceries]


def buy_item():
    item = input(
        'What item would you like to remove from your grocery list?: ')
    new_groceries = []
    temp_groc_file = 'temp_groceries.txt'
    with open('my_grocery_list.txt') as groceries:
        lines = groceries.read()
    lines = lines.split('\n')
    for line in lines:
        if line.startswith(item) or line == '\n':
            continue
        else:
            new_groceries.append(line)
    with open(temp_groc_file, 'w')as temp_groc:
        for item in new_groceries:
            temp_groc.write(str(item) + '\n')
    os.remove('my_grocery_list.txt')
    os.rename(temp_groc_file, 'my_grocery_list.txt')


make_grocery_list(grocery_list)
show_grocery_list('my_grocery_list.txt')
buy_item()
show_grocery_list('my_grocery_list.txt')
