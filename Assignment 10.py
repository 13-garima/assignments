#Q1) Python program to find the maximum odd number in given numbers of input.
#Ans 1
'''
class odd:
    def odd(self, o_list):
        i = -1
        for n in o_list:
            n = int(n)
            if(n % 2 == 1 and n > i):
               
                
                i = n
 
        print("Largest odd number is ", i)
o_list= [1, 13, 349, 8, 6, 120]
 

obj = odd()
obj.odd(o_list)
'''

#Output   
'''
Largest odd number is  349
'''


#Q2) Convert the binary number to decimal without using inbuilt library.
#Ans 2
'''
def binaryToDecimal(n):
    num = n;
    dec_value = 0;
    base = 1;
     
    temp = num;
    while(temp):
        last_digit = temp % 10;
        temp = int(temp / 10);
         
        dec_value += last_digit * base;
        base = base * 2;
    return dec_value;
 

num = 10101001;
print(binaryToDecimal(num));
'''
#Output 
'''
169
'''

#Q3) Convert the decimal number to binary without using an inbuilt library.
#Ans 
'''
def decToBinary(n):
     

    binaryNum = [0] * n;
 
    # counter for binary array
    i = 0;
    while (n > 0):
 
        # storing remainder
        # in binary array
        binaryNum[i] = n % 2;
        n = int(n / 2);
        i += 1;
 
    for j in range(i - 1, -1, -1):
        print(binaryNum[j], end = "");
 
n = 17;
decToBinary(n);

'''
#Output
'''
10001
'''



#Q5)Python program to find the maximum multiple from given N input numbers.
# Ans
'''
n = 7

l =[7,12,14,15,21,56]
j = 56
for i in l:
    if i%n==0 and i==j:
        print("Max multiple = ",i)
        i+=1
        break
else :
        print("Max multiple is not in the list")
'''       
#Output
'''
Max multiple =  56
'''

#Q6)Python program to find the least multiple from given N input numbers.
#Ans 6
'''
n = 8

l =[7,12,14,16,15,21,24,56,72,96]
j = 16
for i in l:
    if i%n==0 and i==j:
        print("Least multiple = ",i)
        i+=1
        break
else :
        print("Least multiple is not in the list")
'''      
#Output
'''
Least multiple =  16
'''

#Q8)Python program to print the current Date.
#Ans 8
'''
from datetime import date

today = date.today()
print("Today date is: ", today)
'''
#Output
'''
Today date is:  2022-06-20
'''

#Q9)Python program to print the calendar current year.
#Ans
'''
import calendar
  
def printcalendar(year):
       
     print(calendar.calendar(year))
  

year = 2022
printcalendar(year)
'''
#Output
'''
2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

'''


#Q10)Python program to print the calendar of the year which is given by the user.
#Ans
'''
import calendar
  
def printcalendar(year):
       
     print(calendar.calendar(year))
  

year = 2010
printcalendar(year)

'''

#Output
'''
2010

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

'''




