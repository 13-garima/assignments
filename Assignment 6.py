#Q1)Find factorial of a given number (Using 2 Techniques).

#Ans 1
'''
import random
from random import randint

minvalue = 1
maxvalue = 50

value = random.randint(minvalue,maxvalue)

print("Value = ",value)

f = 1
for i in range(1,value+1):
    f = f*i
   
print("Factorial = ",f)
'''
#Output 1:
'''
Value =  37
Factorial =  13763753091226345046315979581580902400000000

Value =  16
Factorial =  20922789888000
'''

#Q2)Find the factorial of a number using function
#Ans 2
'''
import random
from random import randint

minvalue = 1
maxvalue = 50

value = random.randint(minvalue,maxvalue)

print("Value = ",value)

def fact(value):
    f=1
    for i in range(1,value+1):
        f= f*i
    return f        

        
result=fact(value)
print("Factorial of value = ",result)
'''
#Output 2
'''
Value =  13
Factorial of value =  6227020800

Value =  27
Factorial of value =  10888869450418352160768000000
'''


#Q3)Find the factorial of a number using recursion.
#Ans 3
'''
import sys
print("Recursion limit =",sys.getrecursionlimit())
import random
from random import randint

minvalue = 1
maxvalue = 50

value = random.randint(minvalue,maxvalue)

print("Value = ",value)

def fact(value):
    if (value==0):
        return 1
    return value*fact(value-1)


result = fact(value)
print("Factorial using recurssion = ",result)
'''

#Output 3
'''
Recursion limit = 3000

Value =  8
Factorial using recurssion =  40320

Value =  11
Factorial using recurssion =  39916800

Value =  22
Factorial using recurssion =  1124000727777607680000

Value =  24
Factorial using recurssion =  620448401733239439360000
'''

#Q4)Write functions to find the square of a given number.
#Ans 4
'''
import math
from math import pow
import random
from random import randint

minvalue = 5
maxvalue = 500

value = random.randint(minvalue,maxvalue)

def square():
    print("Sqaure by multiplication")
    value_square = value * value
    print("Value  =",value)
    print("Square = ",value_square)

    
square()

minvalue = 1
maxvalue = 5000

value2 = random.randint(minvalue,maxvalue)
def square_2():
    print("Sqaure using exponent")
    value_square2 = value2 ** 2
    print("Value  =",value2)
    print("Square = ",value_square2)
    
square_2()


minvalue = 10
maxvalue = 1000

value3 = random.randint(minvalue,maxvalue)
def square_3():
    print("Sqaure using pow built-in method")
    value_square3 = int(pow(value3,2))
    print("Value  =",value3)
    print("Square = ",value_square3)
    
square_3()

'''


#Output 4
'''
Sqaure by multiplication
Value  = 210
Square =  44100
Sqaure using exponent
Value  = 4938
Square =  24383844
Sqaure using pow built-in method
Value  = 558
Square =  311364

Sqaure by multiplication
Value  = 58
Square =  3364
Sqaure using exponent
Value  = 4071
Square =  16573041
Sqaure using pow built-in method
Value  = 197
Square =  38809


'''   

#Q5)Write functions to find a cube of a given number.
#Ans 5
'''
import math
from math import pow
import random
from random import randint

minvalue = 1
maxvalue = 100

value = random.randint(minvalue,maxvalue)

def cube():
    print("Cube by multiplication")
    c = value * value*value
    print("Value  =",value)
    print("Cube = ",c)

    
cube()

minvalue = 100
maxvalue = 5000

value2 = random.randint(minvalue,maxvalue)
def find_cube():
    print("Cube using exponent")
    c2 = value2 ** 3
    print("Value  =",value2)
    print("Cube = ",c2)
    
find_cube()


minvalue = 1
maxvalue = 1000

value3 = random.randint(minvalue,maxvalue)
def cube_find():
    print("Cube using pow built-in method")
    c3 = int(pow(value3,3))
    print("Value  =",value3)
    print("Cube = ",c3)
    
cube_find()

'''

#Output 5
'''
Cube by multiplication
Value  = 5
Cube =  125
Cube using exponent
Value  = 544
Cube =  160989184
Cube using pow built-in method
Value  = 874
Cube =  667627624


Cube by multiplication
Value  = 33
Cube =  35937
Cube using exponent
Value  = 4620
Cube =  98611128000
Cube using pow built-in method
Value  = 873
Cube =  665338617


'''

#Q6)Write functions to find the square root of a given number. (Using 2 Techniques).
# Ans 6
'''
import math
from math import sqrt

import random
from random import randint

minvalue = 4
maxvalue = 1000

value = random.randint(minvalue,maxvalue)

def root():
    print("Sqrt method")
    print("Value  =",value)
    print("Root = ",int(sqrt(value)))

    
root()

minvalue = 1
maxvalue = 100

value1 = random.randint(minvalue,maxvalue)

def root1():
    print("Pow method")
    print("Value1  =",value1)
    print("Root = ",int(pow(value1,1/2)))

root1()
'''

#Output 6
'''
Sqrt method
Value  = 448
Root =  21
Pow method
Value1  = 97
Root =  9

Sqrt method
Value  = 664
Root =  25
Pow method
Value1  = 4
Root =  2
'''

#Q7) Write a program for BMI (Body Mass Index) calculator.

#Ans 7
'''
weight = int(input("Enter your weight in gm = ")) 
height = float(input("Enter your height in feet = "))

kg =  weight/1000
m = height / 3.28
cal_height = m*m

print("Weight in kg =",kg)
print("Height in meter = ",m)


BMI = kg/cal_height
print(BMI)

def weight_status():
    if BMI < 18.5:
        print("Under weight")
        
    elif BMI>=18.25 and BMI<25:
         print("Normal weight")
    
    elif BMI>=25 and BMI<30:
         print("Over weight")
            
weight_status() 
    
'''

# Output 7
'''
Enter your weight in gm =  60000
Enter your height in feet =  5
Weight in kg = 60.0
Height in meter =  1.524390243902439
25.82016
Over weight

Enter your weight in gm =  58000
Enter your height in feet =  5.4
Weight in kg = 58.0
Height in meter =  1.6463414634146343
21.39873799725651
Normal weight

'''

# Q8)  Program to print Odd and Even numbers from the given list of integers
# Ans 8
'''
import random
from random import randint

minvalue = 1
maxvalue = 100

a =  random.randint(minvalue,maxvalue)
b =  random.randint(minvalue,maxvalue)
c =  random.randint(minvalue,maxvalue)
d =  random.randint(minvalue,maxvalue)
e =  random.randint(minvalue,maxvalue)
f =  random.randint(minvalue,maxvalue)

l =[a,b,c,d,e,f]

print("List = ",l)

for i in l:
    if(i%2!=0):
        print({i},"odd")
    else:
        print({i},"even")
'''        
#Output 8
'''
List =  [13, 44, 27, 50, 33, 96]
{13} odd
{44} even
{27} odd
{50} even
{33} odd
{96} even

List =  [88, 81, 85, 8, 66, 65]
{88} even
{81} odd
{85} odd
{8} even
{66} even
{65} odd
'''




