#Q1) Python program for Zip, Zap, and Zoom game.
#Ans 1
'''
def main():
    zzz(15)
    zzz(9)
    zzz(25)
    zzz(31)
 
 
def zzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Zoom")
    elif number % 3 == 0:
        print("Zip")
    elif number % 5 == 0:
        print("Zap")
    else:
        print("Invalid number!")
 
 
main()
'''
#Output 1
'''
Zoom
Zip
Zap
Invalid number!

'''

#Q2) Python program to convert temperature from Celsius to Fahrenheit.
#Ans 2
'''
def cels_to_fahre(cels):
     
        fahrenheit = 1.8*cels + 32
        
        print("The value of temperature in celsius was",cels)
        print("The value of temperature in fahrenheit is ",fahrenheit)
        
cels = int(input("Enter value of temperature :"))
cels_to_fahre(cels)
'''
#Output 2
'''
Enter value of temperature : 34
The value of temperature in celsius was 34
The value of temperature in fahrenheit is  93.2
'''

#Q3) Python program to convert temperature from Fahrenheit to Celsius.
#Ans 3
'''
def fahren_to_cel(fahren):
     
        celsius = ((fahren-32)*5)/9
        
        print("The value of temperature in fahrenheit was",fahren)
        print("The value of temperature in celsius is ",celsius)
        
fahren = int(input("Enter value of temperature :"))
fahren_to_cel(fahren)

'''
#Output 3
'''
Enter value of temperature : 109
The value of temperature in fahrenheit was 109
The value of temperature in celsius is  42.77777777777778
'''

#Q4) Python program to count the number of trailing zeros in Factorial of a given number
#Ans 4
'''
def zeros(z):
    count = 0
    i=5
    while(z/i>=1):
        count = count + int(z/i)
        i= i*5
        
    return int(count)

z = 200
print("Zero = ",zeros(z))
'''   
#Output 4
'''
Zero =  49
'''
#Q5) Python program for swapping of two integers. (Using 2 Techniques).
#Ans 5
x = 10
y = 50
x, y = y, x
print("Value of x:", x)
print("Value of y:", y)

a = 70
b = 20
a = a + b  
b = a - b 
a = a - b
 
print("Value of a:", a)
print("Value of b:", b)

#Output 5
'''
Value of x: 50
Value of y: 10
Value of a: 20
Value of b: 70
'''

#Q6) Python program for swapping of two integers without using the third variable
#Ans 6
x = 20
y = 657
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

#Output
'''
Before swapping: 
Value of x :  20  and y :  657
After swapping: 
Value of x :  657  and y :  20

'''

#Q7) Python program to find who is the winner of the day.
#Ans 7
'''
#import tkinter and random library from python
import tkinter
from tkinter import *
import random 
from random import randint
#defining root for plot of tkinter window
root = tkinter.Tk()
root.title("Lucky Draw generator")
root.geometry("400x400")

#list of data random names
#names=["Liam","Olivia","Noah","Emma","Oliver","Charlotte","Elijah","Amelia","James","Ava","William","Sophia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Theodore","Harper"]


#function to find the winner
def winner():
    names=["Liam","Olivia","Noah","Emma","Oliver","Charlotte","Elijah","Amelia","James","Ava","William","Sophia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Theodore","Harper","Azalea","Calla","Dahlia","Daisy","Daffodil","Ivy","Orchid","Petunia","Violet","Kate","Ruth","Rose","Beth","Jean","Ann","Eve","Blaire","Paige","Gail","Noah","Emma","Oliver","Charlotte","Elijah","Amelia","James"]
    #unique name check
    name_set= set(names)
    #convert to list
    name_list = list(name_set)
    
    #index of name_list
    index_names = len(name_list)-1
    # find a random winner
    winner_name = randint(0,index_names)
    

    winner_label = Label(root,text=name_list[winner_name],font=("Serif",20))
    winner_label.pack(pady=50)
    
   



# top label
label = Label(root,text="LUCKY DRAW !!!!!",font=("Serif",24))
label.pack(pady=20)



#top button
winner =Button(root,text="And THE WINNER IS ",font=("Serif",24),command=winner)
winner.pack(pady=20)



root.mainloop()

'''

#Q8) Python program for the Tower of Hanoi
#Ans 8
'''
def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         

n = 3
TowerOfHanoi(n,'A','B','C')
'''
#Output 8
'''
Move disk 1 from source A to destination B
Move disk 2 from source A to destination C
Move disk 1 from source B to destination C
Move disk 3 from source A to destination B
Move disk 1 from source C to destination A
Move disk 2 from source C to destination B
Move disk 1 from source A to destination B
'''

#Q9) Python program to find the standard deviation.
#Q10) Python program to find the variance
# Ans
'''
import statistics
 
list_1 = [1, 2, 3, 4, 5]
 
print("Standard Deviation = ",(statistics.stdev(list_1)))
 
print("Variance = ",(statistics.variance(list_1)))
'''
#Output
'''
Standard Deviation =  1.5811388300841898
Variance =  2.5
'''

















