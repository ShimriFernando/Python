# OPERATORS IN PYTHON

#1.Arithmetic operators
x = 15
y = 16
#Addition
print(x+y)
#Subtraction
print(x-y)
#Multiplication
print(x*y)
#Division
print(x/y)
#Modulus
print(x%y)
#Exponential
print(x**y)
#Floor Divsion
print(x//y)

#2.Assignment Operators
#equal to
a = 5
b = 6
#Increment
b += 1
print(b)
#Decrement
a -= 3
print(a)
#Multiplication increment
b *= 2
print(b)
#Division decrement
a /= 2
print(a)
#Modulus assignment
b %= 3
print(b)
#Floor division assignment
b //= 2
print(b)
#Exponential assignment
a **= 3
print(a)

#3.Comparison Operators
c = 10
d = 20
#Less than
if(c < d):
    print("c is less than d")
#Lesser than or equal to
    if(c <= d):
        print("c is lesser than/ equal to d")
#Not equal to
        if(c != d):
            print("c not equal to d")
#Greater than
            if(c > d):
                print("c is greater than d")
#Greater than or equal to
                if(c >= d):
                    print("c is greater than/equal to d")
#Equal to
                    if(c == d):
                        print("d is equal to d")
else:
    print("python is fun")


#4.Logical operator
e = 5
f = 6
#AND operator
if(e < 10 and f < 20):
    print("and returns true if both statements are true")
#OR operator
    if(e < 5 or f < 10):
        print("or returns true if one statement is true")
#NOT AND operator
        if(not e < 10 and f < 20):
            print("not inverts the returns")
else:
    print("python is fun")


#5.Identity operators
class Identity_Operators:
    def __init__(self, x, y):
        self.x = x
        self.y = x
ls = Identity_Operators('hello', 'world')
print(ls.x)
print(ls.y)
#IS operator
if (ls.x is ls.y):
    print("is returns true is both the variables are the same object")
#IS NOT operator
    if(ls.x is not ls.y):
        print("is not returns true is both the variables are not the same object")


#6.Membership operators
        if(ls.x in ls.y):
            print("y is a member in x")
            if(ls.x not in ls.y):
                print("y is not a member of x")
else:
    print("python is fun")


#7.Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:

#  Operator	Name	                           Description

#  & 	        AND	                Sets each bit to 1 if both bits are 1
#  |	        OR	                Sets each bit to 1 if one of two bits is 1
#  ^	        XOR	                Sets each bit to 1 if only one of two bits is 1
#  ~ 	        NOT	                Inverts all the bits
#  <<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#  >>	        Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off




# REFERENCE:
# https://www.w3schools.com/python/python_operators.asp



# Done by: Shimri

