print('Hello, World!')
print(1+2)
print()
print("The end","or is it?","keep watching to learn more about Python",3)

#strings 
print('Today is a good day to learn Python.')
print("Python is fun.")
print("Python's string are easy to use")
print("Hello" + " World")
greeting ="hello"
name = "Bruce"
print(greeting + ' '+ name)

##
#The Escape Character 
#\n next line
#\t tab to next stop 
#\\ – literal backslash
#\' – single quote
#\" – double quote
splitstring = "This string has been\nsplitover\nseveral\nlines"
print(splitstring)

tabbedstring="1\t2\t3\t4\t5"
print(tabbedstring)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
#or
print("The pet shop owner said\"No, no, 'e's uh,...he's resting\".")
print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")
anotherSplitString = """This string has been \
split over \
several \
lines"""
print(anotherSplitString)

print('Number\t 1 \t The Larch')

#Each \\ is interpreted as a single backslash (\), because in strings, a single backslash is an escape character.
print("C:\\users\\timbuchalka\\notes.txt") #recommended
#Prefixing the string with r tells Python it's a raw string, meaning backslashes are treated literally — no escaping.
print(r"C:\users\timbuchalka\notes.txt")

##
#Variables
# 1. Begins with a letter / underscore _ character
# 2. case sensitive 
# 3. double quoation / single doesn't matter 
age = 24
print(age)
print(type(greeting))
print(type(age))

age = '2 years'
print(age)
print(type(age))

age_in_words = "2 years"
print(name + " is " + age + " years old")
print(type(age))

##
# Python Data Types 
# 1. Numeric: int, float, complex 
# 2. iterator 
# 3. sequence (which are also iterators)
# 4. mapping 
# 5. file
# 6. class 
# 7. exception 
a = 12 
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 4 integer division, rounded down towards minus infinity 
print(a % b)  # 0 modulo: the remainer after integer division 

# Expression 
for i in range (1, a//b):
    print(i)

# Operator precedence 
# 1. PEMDAS: Parentheses, Exponents, Multiplication / Division, Addition / Subtraction 
# 2. BEDMAS: Brackets, Exponents, Division / Multiplication, Addition / Substraction 
# 3. BODMAS: Brackets, Order, Division / Multiplication, Addition / Subtraction 
# 4. BIDMAS: Brackets, Index, Division / Multiplication, Addition / Subtraction 
# 5. Equal precedence - evaluate from left to right. 
print(a+b/3-4*12)

# The str string data type 
#         012345678901234
#      -  543210987654321
parrot = "Norweigian Blue"
print(parrot)
print(parrot[3])
# "we win"
print(parrot[3] + parrot[4]+ ' ' + parrot[3] + parrot[5] + parrot[9])
print(parrot[3] + parrot[4]+ parrot[10] + parrot[3] + parrot[5] + parrot[9])
print(parrot[-12] + parrot[-11]+ parrot[-5] + parrot[-12] + parrot[-10] + parrot[-6])
print(parrot[3-15] + parrot[4-15]+ parrot[10-15] + parrot[3-15] + parrot[5-15] + parrot[9-15])

# Slicing 
parrot = "Norweigian Blue"
print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[6:])
print(parrot[:6] + parrot[6:])

# Slicing with negative numbers 
parrot = "Norweigian Blue"
print(parrot[-14:-8]) #orweig
print(parrot[-4:-2])  #bl
print(parrot[-4:12])  #b
print(parrot[-4:-12]) # 

# Using a step in a slice 
# 1. The slice starts at index position 0
# 2. It extends up to (but not including) position 6 
# 3. We step through the sequence in steps of 2 
# eg. parrot[0:6:2] = Nre
# eg. parrot[0:6:3] = Nw
#         012345678901234
#      -  543210987654321
parrot = "Norweigian Blue"
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4]) # ,,,,,,
seperators = number[1::4]
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

#slicing backwards 
# make sure the start value is greater than the stop value 
letters="abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
backwards = letters[25:-1:-1]
backwards = letters[::-1]
print(backwards)
# qpo
letters="abcdefghijklmnopqrstuvwxyz"
print(letters[16:13:-1])
# edcba 
letters="abcdefghijklmnopqrstuvwxyz"
print(letters[4::-1])
# the last 8 characters in reverse order 
letters="abcdefghijklmnopqrstuvwxyz"
print(letters[26:17:-1])
print(letters[:-9:-1])
# Other practices 
print(letters[-4:]) #wxyz
print(letters[-1:]) # get the last letter
print([letters[:1]]) # get the first letter 
print(letters[0]) # get the first lettter  / if string is empty, return error 

# string operators 
# Python 3 has 5 sequence types built in:
# 1) the string type; 2) list; 3) tuple; 4) range; 5) bytes and bytearray 
# A sequence is definied as an ordered set of items. 
# eg. "Hello World" - contains 11 items, each item is a character 
# A list eg. ["computer","monitor","keyboard","mouse","mouse mat"] - contains 5 items, each item is a string 

computer_parts =["computer","monitor","keyboard","mouse","mouse mat"] 
print(computer_parts[1]) # monitor
print(computer_parts[1][0]) # monitor [0] index = m


