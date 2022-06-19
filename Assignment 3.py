#Q1) Create a function as isEven() to check given number is even or odd in Python.

# Ans 1
'''
import random
from random import randint
minvalue=0
maxvalue= 100
num = random.randint(minvalue,maxvalue)

def isEven():
    print("Value generated is :",num)
    if (num%2==0):
        print("The given number is even")
        
    else:
        print("Given number is odd")
        
isEven()
'''

#Output 1
'''
Value generated is : 97
Given number is odd

Value generated is : 81
Given number is odd

Value generated is : 60
The given number is even

Value generated is : 37
Given number is odd

'''

#Q2.Create a function to return the absolute value to the given input in Python.
#Ans 2
'''
import random
from random import randint
minvalue= -100
maxvalue= -1
num = random.randint(minvalue,maxvalue)

def absolute_value():
    print("The random negative number is ", num)
    print("The absolute value of number is ",abs(num))

absolute_value()
'''

#Output 2
'''
The random negative number is  -93
The absolute value of number is  93

The random negative number is  -11
The absolute value of number is  11

The random negative number is  -86
The absolute value of number is  86

The random negative number is  -45
The absolute value of number is  45

'''

#Q3.Python program to find the power of a number using the math library.

#Ans 3

'''
import math
import random
from random import randint
minvalue=1
maxvalue= 100
num1 = random.randint(minvalue,maxvalue)
exp = random.randint(minvalue,maxvalue)

def power():
    print("The number generated is = ",num1)
    print("The exponent generated is = ",exp)
    print("Power of number = ",pow(num1,exp))

power()

'''


#Output 3
'''
The number generated is =  62
The exponent generated is =  48
Power of number =  108343059611908889576658785098365751087861024022010602436511655403717182115047324778496
​
The number generated is =  4
The exponent generated is =  42
Power of number =  19342813113834066795298816

The number generated is =  29
The exponent generated is =  87
Power of number =  16928786085125636217954685526539591476599450947979275450903188345458171206851597191594097186523156446465868041540741828707650709

The number generated is =  64
The exponent generated is =  21
Power of number =  85070591730234615865843651857942052864


'''

#Q4) Python program to print the version information.
#Ans 4
'''
import sys

print("Information of version is.\n",sys.version_info)
'''


#Output 4
'''
Information of version is.
 sys.version_info(major=3, minor=9, micro=7, releaselevel='final', serial=0)
'''

#O5.Python program to find sum of all digits of a number.

# Ans 5
'''
import math
import random
from random import randint
minvalue=300
maxvalue= 10000
num2 = random.randint(minvalue,maxvalue)

def addition():
    print("The random value generated is :",num2)
    sum_value = 0
    for i in str(num2):
        sum_value = sum_value+int(i)
    print("Sum = ",sum_value)
    
addition()
'''



#Output 5
'''
The random value generated is : 7413
Sum =  15

The random value generated is : 3839
Sum =  23

The random value generated is : 3839
Sum =  23

The random value generated is : 7974
Sum =  27
'''


#Q6) Python program to find the power of a number using while loop.

# Ans 6
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 100

num3 = random.randint(minvalue,maxvalue)
exp1 = random.randint(minvalue,maxvalue)
output =1
print("The value of number = ",num3)
print("The value of exponent = ",exp1)

while exp1!=0:
    output = output*num3
    exp1 = exp1-1
    
print(output)
'''

#Output 6
'''
The value of number =  28
The value of exponent =  49
81422331814338578443094572348365901791639019487418361547332031566839808

The value of number =  3
The value of exponent =  61
127173474825648610542883299603


The value of number =  48
The value of exponent =  32
630550095814788844423632687832745817333905738742890496

The value of number =  13
The value of exponent =  19
1461920290375446110677

'''

#Q7)Python program to find the power of a number using for loop.

#Ans 7
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 100

num4 = random.randint(minvalue,maxvalue)
exp2 = random.randint(minvalue,maxvalue)
output =1
print("The value of number = ",num4)
print("The value of exponent = ",exp2)

for exp4 in range(exp2, 0, -1):
    output=output*num4

print("Answer = " + str(output))

'''
#Output 7
'''
The value of number =  78
The value of exponent =  55
Answer = 116199202651939761471633660833941520148303569004941768734342378480814421120342141311313248182414325317632

The value of number =  14
The value of exponent =  73
Answer = 464886146511675512184781529230310759569090675635563199653956477629674515058124652544

The value of number =  73
The value of exponent =  26
Answer = 2795080775372854558800260190932141897521953107089

The value of number =  40
The value of exponent =  98
Answer = 10043362776618689222137263077132266265763768711142455220633600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
'''




#Q8.Python program to find the power of a number using recursion.
# Ans 8
'''
import math
import random
from random import randint
minvalue=0
maxvalue= 100

num5 = random.randint(minvalue,maxvalue)
exp3 = random.randint(minvalue,maxvalue)

print("The value of number = ",num5)
print("The value of exponent = ",exp3)

if exp3==0:
    print("The output = 1")
else :
    print("The power =",pow(num5,exp3))
'''    

#Output 8
'''
The value of number =  37
The value of exponent =  79
The power = 7725670851459014258846004833207284020766233204849776182251768477126628899442149506902915459933306325684446616631808266718573

The value of number =  61
The value of exponent =  24
The power = 7045568477354647704120453346932251277539041

The value of number =  100
The value of exponent =  40
The power = 100000000000000000000000000000000000000000000000000000000000000000000000000000000

The value of number =  83
The value of exponent =  69
The power = 2608485181860273522718017380957915212218241947417338667861914832429423041801106811104803708422934576203824921820391201060931775260803

'''










#Q9.Python program to find the power of a number using the function.

#Ans 9
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 100

num6 = random.randint(minvalue,maxvalue)
exp4 = random.randint(minvalue,maxvalue)

def power():
    print("The value of number = ",num6)
    print("The value of exponent = ",exp4)
    
    power = pow(num6,exp4)
    print("The power of number generated =",power)
    
power()
'''
#Output 9
'''
The value of number =  26
The value of exponent =  81
The power of number generated = 4100541255028480090859025036114684248138311212746959682913884801288203877480821967992945808043646919726928049995776

The value of number =  50
The value of exponent =  58
The power of number generated = 346944695195361418882384896278381347656250000000000000000000000000000000000000000000000000000000000

The value of number =  16
The value of exponent =  62
The power of number generated = 452312848583266388373324160190187140051835877600158453279131187530910662656

The value of number =  20
The value of exponent =  29
The power of number generated = 53687091200000000000000000000000000000


'''

#Q10. Python program to reverse a given number (Using 2 Techniques).
#Ans 10a
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 100

num7 = random.randint(minvalue,maxvalue)
print("The value of number = ",num7)

s = str(num7)

print("The reverse of number generated is",s[::-1])

'''

#Output 10a
'''
The value of number =  85
The reverse of number generated is 58

The value of number =  43
The reverse of number generated is 34

The value of number =  53
The reverse of number generated is 35

The value of number =  54
The reverse of number generated is 45

'''

#Ans 10 b
'''
import math
import random
from random import randint
minvalue=1
maxvalue= 1000

num8 = random.randint(minvalue,maxvalue)
print("The value of number = ",num8)
s2 = str(num8)

print(list(reversed(s2)))
'''

#Output 10 b
'''
The value of number =  734
['4', '3', '7']

The value of number =  604
['4', '0', '6']

The value of number =  491
['1', '9', '4']

The value of number =  501
['1', '0', '5']

'''
















    
