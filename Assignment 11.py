#Q2)Print all uppercase and lowercase alphabets.
#ASCII value of uppercase alphabets – 65 to 90.
#ASCII value of lowercase alphabets – 97 to 122.
#Ans 2
'''
print("Upper Case = ")
for i in range(65,90):

    print(chr(i),end=" ")
print("\n")    
print("Lower Case = ")
for i in range(97,122):

    print(chr(i),end=" ")
'''
#Output
'''
Upper Case = 
A B C D E F G H I J K L M N O P Q R S T U V W X Y 

Lower Case = 
a b c d e f g h i j k l m n o p q r s t u v w x y 
'''

#Q3)Find the Nth number which is both square and a cube of a number.
#Ans 3
'''
import math
n = 10

nth = pow(n,6)
sqrt = math.sqrt(nth)
c =  nth ** (1/3)
print(nth)
print(sqrt)
print(c)
'''
#Output
"""
1000000
1000.0
99.99999999999997
"""

#Q4) Program to find the execution time of a python program.
#Ans
from datetime import datetime
start = datetime.now()
l = [10,20,50,100]
for i in l:
    print(i)
end = datetime.now()

print("The time of execution of above program is :",
      str(end-start)[5:])

#Output
'''
10
20
50
100
The time of execution of above program is : 00.000968

#Q5) Find the day of the birthday for a given date in the future using DateTime library
#Ans
'''
import datetime
import calendar
 
def birthday(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
 

date = '13 11 1994'
print(birthday(date))
'''
#Output
'''
Sunday
'''


#Q6) Python program to find the GCD of the given numbers.
#Ans 6
'''
import math
minvalue = 10
maxvalue =100

value1= random.randint(minvalue,maxvalue)
minvalue1 = 1
maxvalue2 =1000
value2 = random.randint(minvalue1,maxvalue2)
print("First Value =",value1)
print("Second Value =",value2)


gcd = math.gcd(value1,value2)

print("GCD = ",gcd)
'''

#Output 6
'''
First Value = 76
Second Value = 704
GCD =  4

First Value = 20
Second Value = 305
GCD =  5
'''



#Q7) Python program to find the LCM of the given numbers.
#Ans 7
'''
import math
minvalue = 10
maxvalue =100

value1= random.randint(minvalue,maxvalue)
minvalue1 = 1
maxvalue2 =1000
value2 = random.randint(minvalue1,maxvalue2)
print("First Value =",value1)
print("Second Value =",value2)


lcm = math.lcm(value1,value2)

print("LCM = ",lcm)
'''
#Output 7
'''
First Value = 100
Second Value = 326
LCM =  16300

First Value = 52
Second Value = 494
LCM =  988
'''

Q8) Find the number of integers from 1 to N which contains digits Zeros(0’s)
#Ans
'''
n=1000
print("Digits containing 0 :")
for i in range(1,n):
    if i%10==0:
        print(i,end=" ")
'''
#output
'''
Digits containing 0 :
10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370 380 390 400 410 420 430 440 450 460 470 480 490 500 510 520 530 540 550 560 570 580 590 600 610 620 630 640 650 660 670 680 690 700 710 720 730 740 750 760 770 780 790 800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990 

'''

#9) Find the sum of all numbers below 1000 which are multiples of 2 or 4.
#Ans
'''
sum = 0
for i in range(1,1000):
    if i% 2==0 or i%4==0:
        
        sum = sum+i
print("Sum = ",sum)
'''
#Output 
'''
Sum =  249500
'''

#10)Python program to print the list of all keywords in python.
'''
import keyword
print(keyword.kwlist,end=" ")
'''
#Output 10
'''
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'] 
'''

#Q11) Print number with commas as thousands of separators in Python
#Ans
def place_value(number):
    return ("{:,}".format(number))
  
print(place_value(1000000))
#Output
'''
1,000,000
'''
