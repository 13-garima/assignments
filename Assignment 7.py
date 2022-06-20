#Q1)Count the total number of bits in a given number.
#Ans 1
'''
import random
from random import randint

minvalue=1
maxvalue =20

v = random.randint(minvalue,maxvalue)
print("The value generated is :: ",v)
def bin_count(n):
    n = bin(v)[2:]
    print ("Binary form of value is :: ",n)
    print("Number of bits::",len(n))
    
    
bin_count(v)
'''
#Output 1
'''
The value generated is ::  12
Binary form of value is ::  1100
Number of bits:: 4

'''

#Q2  Generate random numbers using NumPy library in Python.
# Ans 2
'''
import numpy as np

print("Arrray of numbers : ",np.random.rand(3,2))
print("Sample : ",np.random.randn())
'''
#Output 2
'''
Arrray of numbers :  [[0.6538875  0.81888981]
 [0.42751029 0.95568633]
 [0.92315325 0.46675125]]
Sample :  -0.3406335892330567

'''


#Q3) Generate random integers between 0 and 9 in Python using the inbuilt method.
# Ans 3
'''
import numpy as np

print("Random integers : ",np.random.randint(10,size=(1,9)))
'''
# Output 3
'''
Random integers :  [[0 0 5 9 8 7 7 2 5]]
Random integers :  [[8 0 3 4 6 9 1 2 3]]
'''


#Q4) Program to print a Fibonacci Series.
#Ans 4
'''
import random
from random import randint

minvalue = 1
maxvalue = 40

fib_value = random.randint(minvalue,maxvalue)
print("Value = ",fib_value)

v1= 0
v2=1
print("value = ",{0},v1)
print("value = ",{1},v2)

for i in range(2,fib_value):
    v3 = v1+v2
    v1 = v2
    v2 = v3
    print("value = ", {i},v3)
'''
#Output 4
'''
Value =  22
value =  {0} 0
value =  {1} 1
value =  {2} 1
value =  {3} 2
value =  {4} 3
value =  {5} 5
value =  {6} 8
value =  {7} 13
value =  {8} 21
value =  {9} 34
value =  {10} 55
value =  {11} 89
value =  {12} 144
value =  {13} 233
value =  {14} 377
value =  {15} 610
value =  {16} 987
value =  {17} 1597
value =  {18} 2584
value =  {19} 4181
value =  {20} 6765
value =  {21} 10946

'''

#Q5 Program to calculate the Nth term of a Fibonacci Series.
# Ans 5
'''
def fib(n):
    a=0
    b=1
    if n<0:
        print("Invalid")
    elif n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return b
print(fib(10))
'''
#Output 5
'''
34
'''

#Q6) Python program to check whether the given number is a prime number or not.
#Ans 6)
'''
import random
from random import randint

minvalue = 1
maxvalue = 40
value = random.randint(minvalue,maxvalue)
print("Value = ",value)

for i in range(2,value):
    if value%i==0:
        print("Not Prime")
        break
else:
    print("Prime")
'''
#Output 6
'''
Value =  28
Not Prime


Value =  31
Prime
'''

#Q8) Python program for None keyword.
#Ans 8
'''
value = None

if value is None:
    print("Value is none")
else:
    print("Value = ",value)
'''   
#Output 8
'''
Value is none
'''


#Q9) Python program for pass statement in Python.
#Ans 9
'''
list_ = [1,2,3,5,6,10,45]

for i in list_:
    if i == 5:
        pass
    else:
        print(i)

'''        
#Output 9
'''
1
2
3
6
10
45
'''

#Q10) Python program to define an empty function using a pass statement.
#Ans 10
'''
def function():
    pass
'''





