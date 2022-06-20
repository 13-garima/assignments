#Q1) Python program to find the power of a number using exponential operator available in python.
#Ans 1
'''
import random 
from random import randint

minvalue = 1
maxvalue =100

value = random.randint(minvalue,maxvalue)
print("Value =",value)
minvalue1 = 2
maxvalue1 =10

exp_value = random.randint(minvalue1,maxvalue1)
print("Power = ",exp_value)
print("Exponential value = ",pow(value,exp_value))
'''
#Output 1
"""
Value = 47
Power =  4
Exponential value =  4879681

Value = 80
Power =  4
Exponential value =  40960000

"""

#Q3)Find all Prime numbers less than or equal to N using the Sieve of Eratosthenes algorithm in Python.
#Ans 3

#Sieve of Eratosthenes ALgorithm
# find all prime numbers upto n
# works better with small range
'''
import random 
from random import randint

minvalue = 1
maxvalue =100

num = random.randint(minvalue,maxvalue)
print("Value =",num)
minvalue1 = 2
maxvalue1 =10

def eratosthenes(num):
    prime = [True for i in range(num+1)]
    
    p = 2
    while(p*p<=num):
        if (prime[p]==True):
            for i in range(p*p,num+1,p):
                prime[i]=False
        p +=1
        
    
    for p in range(2,num+1):
        if prime[p]:
            print(p,end=" ")
            
if __name__ == '__main__':
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    eratosthenes(num)
'''  

#Output 3
'''
Value = 44
Following are the prime numbers smaller
than or equal to 44
2 3 5 7 11 13 17 19 23 29 31 37 41 43 

Value = 71
Following are the prime numbers smaller
than or equal to 71
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
'''

#Q4) Check whether the binary representation of a given number is a palindrome or not in if it is palindrome then print “YES IT IS” otherwise print “NO”
#Ans
'''
import random
from random import randint
maxvalue = 1
minvalue = 100
a= random.randint(maxvalue,minvalue)
print(a)
bina = bin(a)

print(bina)
stra=str(bina)
print(stra[2:],stra[2:len(stra)])

for i in stra:
    if stra[2:]==stra[2:len(stra)]:
        print("palindrome")
        break
else:
    print("Not a palindrome")
'''

#Output
'''
33
0b100001
100001 100001
palindrome

'''
