#Q2)Python program to convert centimeter to Inches.
#Ans 2
'''
import random
from random import randint
maxvalue = 100
minvalue = 1
cn = random.randint(minvalue,maxvalue)
print("Centimeter = ",cn)
inches = cn/2.54

print("Inches = ",inches)
'''
#Output 2
'''
Centimeter =  14
Inches =  5.511811023622047
'''

#Q3)Python program to convert meters into yards.
#1 Meter = 1.09361 Yard
#Ans
'''
import random
from random import randint
maxvalue = 100
minvalue = 1
meter = random.randint(minvalue,maxvalue)
yard = meter*1.09361

print("Meter = ",meter,"meter")
print("Yard = ",yard,"yard")
'''
#Output
'''
Meter =  32 meter
Yard =  34.99552 yard
'''

#Q4)Python program to convert yards into meters.
#yard_to_meter = yard / 1.09361
#Ans
'''
import random
from random import randint
maxvalue = 100
minvalue = 1
yard = random.randint(minvalue,maxvalue)
meter = yard/1.09361


print("Yard = ",yard,"yard")
print("Meter = ",meter,"meter")
'''
#Output
'''
Yard =  29 yard
Meter =  26.517679977322814 meter
'''

#Q5) Python program to capitalize on the character without using a function.
#Ans
'''
A="a"
a ="A"
B="b"
b="B"
print("ASCII value 'a' = ",ord(A),"ASCII value 'A' = ",ord(a))
print("ASCII value 'b' = ",ord(B),"ASCII value 'B' = ",ord(b))
temp = a
a = A
A = temp

temp1 = b
b =B
B= temp1

print("Swapping : : ",a,A)
print("Swapping : : ",b,B)
'''
#Output
'''
ASCII value 'a' =  97 ASCII value 'A' =  65
ASCII value 'b' =  98 ASCII value 'B' =  66
Swapping : :  a A
Swapping : :  b B
'''

#Q6) Python program to lowercase the character without using a function.
#Ans
'''
U="U"
u ="u"

print("ASCII value 'u' = ",ord(u))
print("ASCII value 'U' = ",ord(U))
temp = U
U = u
u = temp



print("Swapping : : ",u,U)

'''
#Output
'''
ASCII value 'u' =  117
ASCII value 'U' =  85
Swapping : :  U u
'''

#Q7)Python program to find perfect number.
'''
import random
from random import randint
maxvalue = 100
minvalue = 1
n = random.randint(minvalue,maxvalue)
print("Number =",n)
sum =1
for i in range(1,n-1):
    if n%i==0:
        
        sum = sum+i
print("Sum of divisors =",sum)
if sum==n:
    print("Number is perfect")
    
else:
    print("Number is not perfect")
 '''   

#Output 
'''
Number = 94
Sum of divisors = 51
Number is not perfect

Number = 21
Sum of divisors = 12
Number is not perfect

Number = 25
Sum of divisors = 7
Number is not perfect

Number = 82
Sum of divisors = 45
Number is not perfect

'''

#Q8) Python program to print perfect numbers from the given numbers of integers.
#Ans 8
'''
def perfect_Number(n):  
   if n < 1:
      return False

   sum = 0
   for i in range(1,n):
      if n%i==0:
         sum += i
   return sum == n

min_value = 1
max_value = 1000


print('Perfect numbers from 1 to 100 are:',(min_value, max_value))
for i in range(min_value, max_value+1):
   if perfect_Number(i):
      print(i, end='.\n')
'''      
#Output 8
'''
Perfect numbers from 1 to 100 are: (1, 1000)
6.
28.
496.
'''

#Q9) Python program to find the greatest integer using floor() method.
#Ans 9
'''
import math   
print ("math.floor(-23.11) : ", math.floor(-23.11))
print ("math.floor(300.16) : ", math.floor(300.16))
print ("math.floor(300.72) : ", math.floor(300.72))
'''
#Output 9
'''
math.floor(-23.11) :  -24
math.floor(300.16) :  300
math.floor(300.72) :  300
'''

#Q10) Python program to find the maximum even number in given numbers of input.
#Ans 10
'''
class even:
    def even(self, e_list):
        i = -1
        for n in e_list:
            n = int(n)
            if(n % 2 == 0 and n > i):
               
                # replace current largest even
                i = n
 
        print("Largest even number is ", i)
e_list= [1, 130, 34, 8, 6, 120]
 

obj = even()
obj.even(e_list)
'''

#Output 10:
'''
Largest even number is  130
'''





