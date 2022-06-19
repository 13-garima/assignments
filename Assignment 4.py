
#Q1) Python program to find floor(integer) division.
#Ans 1

'''
import math
import random
from random import randint
minvalue=100
maxvalue= 1000

value_1 =  random.randint(minvalue,maxvalue)
value_2 =  random.randint(minvalue,maxvalue)

floor_div = value_1//value_2

print("Value_1 = ",value_1)
print("Value_2 = ",value_2)

print("Result = ",floor_div)
'''
#Output 1
'''
Value_1 =  226
Value_2 =  181
Result =  1

Value_1 =  864
Value_2 =  842
Result =  1

Value_1 =  886
Value_2 =  500
Result =  1

Value_1 =  887
Value_2 =  936
Result =  0
'''

#Q2) Some of the examples of simple if statement.
# Ans 2a

'''
a = 10
b =45

print("Value of a =",a)
print("Value of b =",b)

if a==b:
    print("a is equal to b")

if a>b: 
    print("a is greater than b")
    
if a<b:
    print("b is greater than a")
'''
#Output 2a
'''
Value of a = 10
Value of b = 45
b is greater than a
'''

#Ans 2b
'''
str_1 = "Happy"
str_2 = "Paper"

print("value of str_1 = ",str_1)
print("value of str_2 =",str_2)

if len(str_1)==len(str_2):
    print("Strings are equivalent")
'''
#Output2b
'''
value of str_1 =  Happy
value of str_2 = Paper
Strings are equivalent
'''
#2c
'''
user_input = str(input("Enter a string = "))
print("The user input is = ",user_input)
sample = "Nayasa"

if len(user_input)==len(sample):
    print("Sucess!!!!")
    
if len(user_input)>len(sample):
    print("Better luck next time!")
'''
#Output 2c
''''
Enter a string =  Induction
The user input is =  Induction
Better luck next time!

Enter a string =  Indian
The user input is =  Indian
Sucess!!!!
'''


#Q3) Some of the examples of simple if-else statement
#Ans 3a
'''
str_1 = "Python For Data Science"
str_2 = str(input("Enter a string = "))

if str_1[:6] in str_2:
    print("Match")
    
else :
    print("Not matched")
'''
#Output 3a
'''
Enter a string =  Python
Match

Enter a string =  Happy
Not matched
'''
#Ans 3b
'''
str_1 = str(input("Enter a string = "))

if str_1 == len("Information"):
    print("Match")
    
else :
    print("Not matched")
'''
#Output 3b
'''
Enter a string =  Accurate
Not matched
'''

#Q4) Take input from a user that is age and check eligibility for voting or not.
#Ans 4
'''
user_input = int(input("Enter your birth year = "))

age = 2022 - user_input

print("Age calculated = ",age)

if age>=18:
    print("Eligible to vote")
    
else :
    print("Not eligible")
'''
#Output 4

'''
Enter your birth year =  1997
Age calculated =  25
Eligible to vote

Enter your birth year =  2010
Age calculated =  12
Not eligible
'''


#Q5)Find the largest of three numbers using nested if-else.
#Ans 5
'''
import math
import random
from random import randint
minvalue=100
maxvalue= 1000

A = random.randint(minvalue,maxvalue)
B = random.randint(minvalue,maxvalue)
C = random.randint(minvalue,maxvalue)

print("Value of A = ",A)
print("Value of B = ",B)
print("Value of C = ",C)

if A>B:
    print("A is greater than B")
    
    
    if A>C:
        print("A is greater than C")
       
else:
        print("B is greatest")
'''
        
#Output 5
'''
Value of A =  183
Value of B =  611
Value of C =  120
B is greatest

Value of A =  758
Value of B =  280
Value of C =  455
A is greater than B
A is greater than C
'''

#Q6) Calculate discount based on the sale amount.
'''
import math
import random
from random import randint
minvalue=100
maxvalue= 10000

cost_price = random.randint(minvalue,maxvalue)

minvalue1=10
maxvalue1= 900

selling_price = random.randint(minvalue1,maxvalue1)

discount = cost_price-selling_price
percent_discount = (discount/cost_price)*100
print("Cost price = ",cost_price)
print("Selling price = ",selling_price)
print ("Discount = ",discount)
print("Percent discount = ",percent_discount)
'''
#Output 6
'''
Cost price =  1496
Selling price =  779
Discount =  717
Percent discount =  47.92780748663101
'''



#Q7 Calculate discount based on the sale amount using Nested if-else.
#Ans 7
'''
import math
import random
from random import randint
minvalue1=10
maxvalue1= 90000

selling_price = random.randint(minvalue1,maxvalue1)
print("Selling price = ",selling_price)

if (selling_price>0):
    if selling_price <= 5000:
        discount = selling_price*0.05
    elif selling_price <= 15000:
        discount = selling_price*0.12
    elif selling_price <= 25000:
        discount = selling_price*0.2
    else :
        discount = selling_price*0.3
    
    print("Discoun :",discount)
    print("Amount paid :",selling_price-discount)

else:
    print("Invalid")
'''
#Output 7
'''
Selling price =  77295
Discoun : 23188.5
Amount paid : 54106.5
'''


#Q8)Write a program of Ternary Operator.
#Ans 8
'''
import random
from random import randint
minvalue=100
maxvalue= 1000

J = random.randint(minvalue,maxvalue)
K = random.randint(minvalue,maxvalue)
print("Value of Number = ",J)
print("Value of Number = ",K)

maximum = J if J>K else K

print("The maximum number =",maximum)
'''

#Output 8
'''
Value of Number =  518
Value of Number =  693
The maximum number = 693

Value of Number =  398
Value of Number =  315
The maximum number = 398
'''

#Q9 Design a simple calculator using if – elif – else statements.
#Ans 9
'''
import math
import random
from random import randint
minvalue=10
maxvalue= 1000

M = random.randint(minvalue,maxvalue)
N = random.randint(minvalue,maxvalue)

print("Value of M = ",M)
print("Value of N = ",N)

def addition(M,N):
    add = M+N
    print(add)
    
def subtract(M,N):
    sub = M-N
    print(sub)
    
def multiply(M,N):
    multiplication = M+N
    print(multiplication)
    
user_input = (input("Enter an operator : "))

if user_input == "+":
    addition(M,N)

elif user_input == "-":
    subtract(M,N)
    
elif user_input == "*":
    multiply(M,N)

else:
    print("Invalid")
'''   
#Output 9
'''
Value of M =  790
Value of N =  180
Enter an operator :  +
970

Value of M =  710
Value of N =  618
Enter an operator :  *
1328

Value of M =  756
Value of N =  409
Enter an operator :  -
347

Value of M =  626
Value of N =  458
Enter an operator :  9
Invalid
'''


#Q10 Write an example of for loop.
#Ans 10
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 25

Number = random.randint(minvalue,maxvalue)
print("Value of Number = ",Number)

def pyramid(Number):
    
    shape = Number-1
    
    for i in range(0,Number):
        for j in range(0,shape):
            print(end=" ")
            
        shape = shape-1
        
        for j in range(0,i+1):
            print("-- ",end="")
            
        print("\r")
        

pyramid(Number)
'''
#Output 10
'''
Value of Number =  14
             -- 
            -- -- 
           -- -- -- 
          -- -- -- -- 
         -- -- -- -- -- 
        -- -- -- -- -- -- 
       -- -- -- -- -- -- -- 
      -- -- -- -- -- -- -- -- 
     -- -- -- -- -- -- -- -- -- 
    -- -- -- -- -- -- -- -- -- -- 
   -- -- -- -- -- -- -- -- -- -- -- 
  -- -- -- -- -- -- -- -- -- -- -- -- 
 -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- 
'''
            
