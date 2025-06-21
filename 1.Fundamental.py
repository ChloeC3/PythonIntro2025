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
#         012345678901234
#      -  543210987654321
parrot = "Norweigian Blue"
print(parrot[0:6:2])
print(parrot[0:6:3])
