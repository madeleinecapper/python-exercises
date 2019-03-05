# '''#1 Define a function named is_two. 
# It should accept one input and 
# return True if the passed input is either the number 
# or the string 2, False otherwise.'''

# def is_two(arg):
#     if int(arg) == 2:
#         return True
#     else:
#         return False

# print(is_two(9))
# print(is_two(2))
# print(is_two('2'))

# '''#2 Define a function named is_vowel. 
# It should return True if the passed string is a vowel, 
# False otherwise.'''

def is_vowel(letter):
    if letter in('a','e','i','o','u'):
        return True
    else:
        return False

# print(is_vowel('a'))
# print(is_vowel('six'))
# print(is_vowel(8))

# ''' #3 Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.'''

def is_consonant(thing):
    if thing.isdigit():
        return False
    elif not is_vowel(thing):
        if len(thing) == 1:
            return True
        else:
            return False
    else:
        return False

# print(is_consonant('b'))
# print(is_consonant('asdfa'))
# print(is_consonant('6'))

# '''#4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the 
# word starts with a consonant.'''

def cap_cons(argument):
    if is_consonant(argument[0]):
        newstring = argument[0].upper() + argument[1:len(argument)+1]
        return newstring
    else:
        return argument

# print(cap_cons('sillystring'))
# print(cap_cons('applesauce'))

# ''' #5: Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.'''

def calculate_tip(percentage, bill_total):
    dollar_tip = percentage * bill_total
    return dollar_tip

print(calculate_tip(0.2,100.00))

#'''#6: Define a function named apply_discount,
#It should accept a original price, and a discount percentage,
#and return the price after the discount is applied'''

def apply_discount(price, discount_percentage):
    dollars_off = price * discount_percentage
    price -= dollars_off
    return price

print(apply_discount(100,0.2))

#'''#7: Define a function named handle_commas.
#It should accept a string that is a number
#that contains commas in it as inputand returns a number as output'''

def handle_commas(arg):
    commaless = arg.replace(',','')
    if commaless.isdigit():
        return commaless

print(handle_commas('g,g,g,,,ggggg'))
print(handle_commas('1,,3,,3,3,,000,,0,,,000,0'))