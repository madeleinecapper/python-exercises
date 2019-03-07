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

grocery_list = ['tofu','broccoli','noodles']
def make_grocery_list(groceries):
    with open('my_grocery_list.txt', 'x') as f:
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
    item = input('What item would you like to remove from your grocery list?: ')
    with open('my_grocery_list.txt', 'x') as groceries:
        for line in lines:
            if line.startswith('item'):
                continue
            else:
                new_groceries.append(line)
        for item in new_groceries:
            string_groceries += str(item) + '\n'
        f.write(string_groceries)
        