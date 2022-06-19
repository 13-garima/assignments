'''
# Q1) How to print spaces in Python Programming Language?

# Ans 1:

#1) print space by using " "

a = "Mount Everest is the highest peak in the world "
height = 29029

print(a + " " + str(height)+" "+ "feet")

#2) using rjust() : adding space at start of the string
'''
#The rjust() method in python returns a new string. The length of the new string is provided as the input parameter. 
#The length is increased by adding character at the left side of the original string.
'''

new_string_rsjust = len(a)+ 3
r_new_string = a.rjust(new_string_rsjust)
print(" ")
print("Space added in the start: right justified")
print(r_new_string)

#3) using ljust() : adding space at end of the string

new_string_ljust = len(a)+ 5
l_new_string = a.ljust(new_string_ljust)
print(" ")
print("Space added at the end: left justified")
print(l_new_string)

#using center(): adding space at both ends

new_string_center = len(a)+ 18
c_new_string = a.center(new_string_center)
print(" ")
print("Bring the string at center")
print(c_new_string)

#4) using format function:

print(" ")
print("using format function")
print("{0} {1}.\n".format(a,height))

#5) usin \n

print("First line.\nSecond line.\n ")

#6) Using for loop 
l = ["Top 3","Mount Everest","Godwin Austen","Kangchenjunga"]
for m in l :
    print(m,end =" ")

'''

#Output1
'''
Mount Everest is the highest peak in the world  29029 feet
 
Space added in the start: right justified
   Mount Everest is the highest peak in the world 
 
Space added at the end: left justified
Mount Everest is the highest peak in the world      
 
Bring the string at center
         Mount Everest is the highest peak in the world          
 
using format function
Mount Everest is the highest peak in the world  29029.

First line.
Second line.
 
Top 3 Mount Everest Godwin Austen Kangchenjunga
'''




'''
#Q2)Python Program to Printing different messages by using different variations of the print() method.

# 1) Message 1
print("Python and Data Science")

#2) Message 2 : end=" "
a = "Python"
b ="and Data Science"
print(a,b,end= " ")

#3) Message 3 : concatenation
print(a + b)

#4)Message 4: seprator

print(a,b,sep="----")

#5) Message 5 : flush
print(a,b,flush ="flush")

#6) Messgae 6 : \n
print("Python.\n","Data Science")


'''

#Output 2

'''
Python and Data Science
Python and Data Science Pythonand Data Science
Python----and Data Science
Python and Data Science
Python.
 Data Science

'''


'''
#Q3)Multiple value assignment to the variable.

a = "Python"
a= 123
a=4.5

print("Value of a is ",a,".\n","Type of a is:",type(a))


'''

#Output 3
'''
Value of a is  4.5 .
 Type of a is: <class 'float'>
'''

'''

#Q4 Python Program to print given text using a user-defined method.

def user_def():
    user_input= input("Enter a sentence :")
    print("User entered the following sentence.\n",user_input)
    
user_def()
'''

#Output 4
'''
Enter a sentence : Python and data science
User entered the following sentence.
 Python and data science

'''

'''
#Q5 Python Program to Printing different values (integer, float, string, Boolean, complex).

def values():
    integer = int(input("Enter an integer :"))
    print(integer)
    point = input("Enter a floating point number :")
    print(point)
    string= str(input("Enter a string:"))
    print(string)
    complex_ = input("Enter a complex number")
    print(complex_)
values()

def check():
    user_input = int(input("Enter a number: "))
    print(user_input%2==0)
    
check()
        


'''
#Output 5
'''
Enter an integer : 455
455
Enter a floating point number : 8.99
8.99
Enter a string: 900
900
Enter a complex number 40
40
Enter a number:  6890
True

'''

'''
#Q6)Python Program to Declare different types of variables print their values.

#integer

a = int(input("Enter a value : "))
b = float(input("Enter a value : "))
c = str(input("Enter a value : "))
#d = complex(input("Enter a value : "))

print(a,b,c,end=" ")


'''
#Output 6
'''
Enter a value :  23
Enter a value :  2.3
Enter a value :  23
23 2.3 23 
'''


'''
#Q7 Python program to demonstrate variables scope (Global and Local variables).

a = "Python"
global a

def demo():
    print(a,"is global variable value")
    b1 ="Data Science"
    print(b1,"is local variable")
    
demo()


try:
    print(b1)
    
except Exception as e:
    print("Error local variable can't be called")
'''
#Output 7
'''
Python is global variable value
Data Science is local variable
Error local variable can't be called

'''

'''
#Q8 How to determine the type of a variable or object in Python.
#Q9 How to determine the id of a variable or object in Python.

class demo1():
    str_a = "Python and Data science"
    print(str_a)
    
obj = demo1()
print("Type of object is : ",type(obj))
print("Id of object is : ",id(obj))

'''
#Output 8,9
'''
Python and Data science
Type of object is :  <class '__main__.demo1'>
Id of object is :  2412924093968

'''

'''
#Q10) Create number variables (int, float, and complex) and print their types in Python.

p,q = 10,10.200
c = complex(30)

print(p,q,c,end= " ")
print(type(p),type(q),type(c),end=" ")


'''
#Output 10
'''
10 10.2 (30+0j) <class 'int'> <class 'float'> <class 'complex'>

'''






