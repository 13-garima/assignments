
# Q1)Typecasting Input to Integer, Float.
'''
user_input = input("Enter a value :")
print("The value given by user is :",user_input)


def type_float():
        t_float = float(user_input)
        print("The value converted to float :",t_float)
        
def type_int():
        t_int = int(user_input)
        print("The value converted to integer :",t_int)


    
    


type_float()
type_int()
'''
#Output 1
'''
Enter a value : 100
The value given by user is : 100
The value converted to float : 100.0
The value converted to integer : 100

'''




#Q2)Program to define an integer value and print it.
'''

user_input = int(input("Enter a number : "))

u_int = int(user_input)
print("The number given by user is :",u_int)
print(type(u_int))


'''
#Output 2
'''
Enter a number :  456
The number given by user is : 456
<class 'int'>
​
'''


#Q3) Take User Input two integers numbers and find their addition.
'''
def addition():
    a_value = int(input("Enter a value for a: "))
    b_value = int(input("Enter a value for b: "))
    sum_ = a_value + b_value
    print("The sum of two integers is :",sum_)
    
    
addition()



'''

#Output 3
'''
Enter a value for a:  489
Enter a value for b:  709
The sum of two integers is : 1198

'''


#Q4)Python program to sum of two float numbers.
'''
def add_float():
    f1 = float(input("Enter first float value: "))
    f2 = float(input("Enter second float value : "))
    float_add = f1 + f2
    print("Value after addition is :",float_add)
    
    
add_float()


'''

#Output 4
'''
Enter first float value:  6.7
Enter second float value :  7.7
Value after addition is : 14.4

'''



#Q5)Python program to find the addition of two numbers (Using 4 Techniques)
'''
#1) add

a = 10
b = 20
sum1 = a+b
print("Simple technique :",sum1)

#2) add using function

def add(a,b):
    sum = a+b
    print("Addition using function :",sum)
    

add(30,30)


#3) add using user input and function

a = int(input("Enter a value for a : "))
b = int(input("Enter a value for b : "))

def add():
    sum = a+b
    print("Addition using function :",sum)
    

add()
    


#4) add using class

class addition():
    a=0
    b=0
    
    def __init__(self):
        self.a = 100
        self.b = 290
        
    def add(self):
        return self.a+ self.b
    
obj = addition()
print("Addition using class : ",obj.add())
        



    

'''
#Output 5
'''
Simple technique : 30

Addition using function : 60

Enter a value for a :  20
Enter a value for b :  80
Addition using function : 100

Addition using class :  390




'''


#Q6)Python program to print the ASCII value of a character.
'''
user_input = str(input("Enter a character :"))

for i in user_input:
    if len(user_input)>1:
        print("enter a single character")
        break
    else:
        print("The ASCII value of character is :",ord(user_input))



'''
#Output 6
'''
Enter a character : BCD
enter a single character

Enter a character : H
The ASCII value of character is : 72

'''


#Q7) Python program to calculate simple interest.
'''

principle = int(input("Enter a principle amount :"))
rate = float(input("Enter rate of interest : "))
time = int(input("Enter time : "))

simple_i = (principle*rate*time)/100

print("The simple interest calculated is :",simple_i)


'''
#Output 7
'''
Enter a principle amount : 1000
Enter rate of interest :  7
Enter time :  3
The simple interest calculated is : 210.0

'''


#Q8)Python program to calculate compound interest.
'''

principle = int(input("Enter a principle amount :"))
rate = float(input("Enter rate of interest : "))
time = int(input("Enter time : "))

compound_i = principle*(1+0.01*rate)*time

print("The compound interest calculated is :",compound_i)



'''
#Output 8
'''
Enter a principle amount : 1000
Enter rate of interest :  4
Enter time :  8
The compound interest calculated is : 8320.0
'''


#Q9)Python program to check the given year is a leap year or not.
'''
user_input = int(input("Enter your birth year"))

if (user_input%4==0):
    print("Year was leap year")
elif(user_input%400==0):
    print("Year was leap year") 
elif(user_input%100==0):
    print("Year was leap year") 
    
else:
    print("year was not a leap year")
'''
#Output 9
'''
Enter your birth year 1994
year was not a leap year
'''


#Q10) Simple pattern printing programs in Python.
'''
def triangle(t):
    
    s = t-1
    
    for i in range(0,t):
        for j in range(0,s):
            print(end=" ")
            
        s = s-1
        
        for j in range(0,i+1):
            print("T ",end="")
            
        print("\r")
        
t=7
triangle(t)
            





'''
#Output 10

'''
      T 
     T T 
    T T T 
   T T T T 
  T T T T T 
 T T T T T T 
T T T T T T T 
​

'''












