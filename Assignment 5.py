#Q1)Write an example for each loop
#Ans 1
#while loop
'''
import random
from random  import randint

maxvalue = 1
minvalue = 100

value  =   random.randint(maxvalue,minvalue)
print("The value generated = ",value)

v = 0
print("Order = ")
while v < value:
   
    print(v,end=" ")
    v = v + 1
'''    
#Output while loop
'''
The value generated =  51
Order = 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 

The value generated =  61
Order = 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 

The value generated =  12
Order = 
0 1 2 3 4 5 6 7 8 9 10 11 

The value generated =  99
Order = 
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 
'''

#for loop
'''
import random

minvalue = 1
maxvalue = 20



def binary_key(p):
    key = ""
    
    for i in range(p):
        value = str(random.randint(0,1))
        key += value
        print(key)
    
    return key

p = random.randint(minvalue,maxvalue)
print("Value generated is = ",p)
binary_string = binary_key(p)
print("Final value = ",binary_string)

'''

#Output for loop
'''
Value generated is =  11
1
10
101
1011
10111
101110
1011101
10111011
101110110
1011101101
10111011010
Final value =  10111011010

Value generated is =  13
0
00
001
0011
00111
001110
0011100
00111001
001110010
0011100101
00111001011
001110010110
0011100101101
Final value =  0011100101101

Value generated is =  16
1
10
100
1000
10000
100001
1000011
10000110
100001101
1000011011
10000110111
100001101110
1000011011101
10000110111011
100001101110111
1000011011101111
Final value =  1000011011101111

Value generated is =  7
1
10
101
1010
10101
101010
1010100
Final value =  1010100
'''

#Q2) Write an examples of loops (based on their control).

#Ans 2

# while loop
'''
user_input = int(input("Enter a number = "))
i = 0
while i< user_input:
    i=i+1
    print("1")
  #  i=i+1
    
user_input1 = input("Enter a string = ")
j =  0
while j< len(user_input1):
    j=j+1
    print("A")
   # j=j+1
'''
#Output
'''
Enter a number =  5
1
1
1
1
1
Enter a string =  FilterFiles
A
A
A
A
A
A
A
A
A
A
A
'''

#for loop
'''
str_1 = "Coaching Class"

print("Characters of string :.\n ")
for i in str_1:
     print(i,end="")
print(".\n")        
print("String printed number of index of string :.\n ")
for i in str_1:
     print(str_1,end="//")
 '''   

#Output
'''
Characters of string :.
 
Coaching Class.

String printed number of index of string :.
 
Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//Coaching Class//
'''

    
#Q3) Some other examples of looping.
#Ans 3
'''
import random
from random import randint

minvalue= 1
maxvalue = 100

value1 = random.randint(minvalue,maxvalue)
value2 = random.randint(minvalue,maxvalue)
value3 = random.randint(minvalue,maxvalue)
value4 = random.randint(minvalue,maxvalue)
value5 = random.randint(minvalue,maxvalue)
value6 = random.randint(minvalue,maxvalue)


List1= [value1,value2,value3,value4,value5,value6]

for x in List1 :
    print("The values generated = ",List1)
    print("Maximum value =",max(List1))
    print("Minimum value = ",min(List1))
    break
'''  


#Output 
'''
The values generated =  [4, 48, 73, 21, 7, 87]
Maximum value = 87
Minimum value =  4

The values generated =  [72, 77, 40, 62, 93, 4]
Maximum value = 93
Minimum value =  4

The values generated =  [2, 82, 59, 68, 94, 97]
Maximum value = 97
Minimum value =  2

The values generated =  [48, 24, 60, 10, 22, 23]
Maximum value = 60
Minimum value =  10

'''

#Q4 Write an Example of a break statement.

#Ans 4

#pattern generation
'''
row = 4

for i in range(0,row):
    a = 1
    print(a,end=' ')
    
    for j in range(row - i - 1, 0 ,-1):
        print('*',end=' ')
        a=a+1
        print(a,end=' ')
        print('\n')
        break
'''
        
#Output 4
'''
1 * 2 

1 * 2 

1 * 2 

1 
'''
    
#Q5 Write an Example of continue statement.

#Ans5
'''
i = 10
while i<25:
    i += 1
    if i == 3:
        continue
    print(i)
'''

#Output 5
'''
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
'''

#Q6 Write an Example of a pass statement.
#Ans 6
'''
import random
from random import randint

minvalue= 10
maxvalue = 100

a = random.randint(minvalue,maxvalue)
b = random.randint(minvalue,maxvalue)

print("Value of a = ",a)
print("Value of b = ",b)

if b>a:
    pass
else:
    print("A is greater")
'''
#Output 6
'''
Value of a =  45
Value of b =  21
A is greater


Value of a =  17
Value of b =  34
'''


#Q7 Program to print numbers from 1 to N (using range()).
# Ans 7
'''
import random
from random import randint

minvalue= 1
maxvalue = 50

N = random.randint(minvalue,maxvalue)
print("Value of N = ",N)
for i in range(1,N):
    print(i,end=" ")
'''
#Output 7
'''
Value of N =  28
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 

Value of N =  8
1 2 3 4 5 6 7 

Value of N =  47
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 
'''

#Q8 Program to print numbers from N to 1 (using range() ).
#Ans 8
'''
import random
from random import randint

minvalue= 1
maxvalue = 100

N = random.randint(minvalue,maxvalue)
print("Value of N = ",N)
for i in reversed(range(1,N)):
    print(i,end=" ")
'''


#Output 8
'''
Value of N =  48
47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

Value of N =  72
71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

Value of N =  42
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

Value of N =  91
90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
'''

#Q9 Print all numbers between 1 to 1000 which are divisible by 9 and must not be divisible by 3.
#Ans 9
'''

for i in range(1,1000):
    if (i%3!=0 ):
            print(i,end=" ")
    if (i%9==0 ):
                print(i,end=" ")
'''
        
#Output 9
'''
1 2 4 5 7 8 9 10 11 13 14 16 17 18 19 20 22 23 25 26 27 28 29 31 32 34 35 36 37 38 40 41 43 44 45 46 47 49 50 52 53 54 55 56 58 59 61 62 63 64 65 67 68 70 71 72 73 74 76 77 79 80 81 82 83 85 86 88 89 90 91 92 94 95 97 98 99 100 101 103 104 106 107 108 109 110 112 113 115 116 117 118 119 121 122 124 125 126 127 128 130 131 133 134 135 136 137 139 140 142 143 144 145 146 148 149 151 152 153 154 155 157 158 160 161 162 163 164 166 167 169 170 171 172 173 175 176 178 179 180 181 182 184 185 187 188 189 190 191 193 194 196 197 198 199 200 202 203 205 206 207 208 209 211 212 214 215 216 217 218 220 221 223 224 225 226 227 229 230 232 233 234 235 236 238 239 241 242 243 244 245 247 248 250 251 252 253 254 256 257 259 260 261 262 263 265 266 268 269 270 271 272 274 275 277 278 279 280 281 283 284 286 287 288 289 290 292 293 295 296 297 298 299 301 302 304 305 306 307 308 310 311 313 314 315 316 317 319 320 322 323 324 325 326 328 329 331 332 333 334 335 337 338 340 341 342 343 344 346 347 349 350 351 352 353 355 356 358 359 360 361 362 364 365 367 368 369 370 371 373 374 376 377 378 379 380 382 383 385 386 387 388 389 391 392 394 395 396 397 398 400 401 403 404 405 406 407 409 410 412 413 414 415 416 418 419 421 422 423 424 425 427 428 430 431 432 433 434 436 437 439 440 441 442 443 445 446 448 449 450 451 452 454 455 457 458 459 460 461 463 464 466 467 468 469 470 472 473 475 476 477 478 479 481 482 484 485 486 487 488 490 491 493 494 495 496 497 499 500 502 503 504 505 506 508 509 511 512 513 514 515 517 518 520 521 522 523 524 526 527 529 530 531 532 533 535 536 538 539 540 541 542 544 545 547 548 549 550 551 553 554 556 557 558 559 560 562 563 565 566 567 568 569 571 572 574 575 576 577 578 580 581 583 584 585 586 587 589 590 592 593 594 595 596 598 599 601 602 603 604 605 607 608 610 611 612 613 614 616 617 619 620 621 622 623 625 626 628 629 630 631 632 634 635 637 638 639 640 641 643 644 646 647 648 649 650 652 653 655 656 657 658 659 661 662 664 665 666 667 668 670 671 673 674 675 676 677 679 680 682 683 684 685 686 688 689 691 692 693 694 695 697 698 700 701 702 703 704 706 707 709 710 711 712 713 715 716 718 719 720 721 722 724 725 727 728 729 730 731 733 734 736 737 738 739 740 742 743 745 746 747 748 749 751 752 754 755 756 757 758 760 761 763 764 765 766 767 769 770 772 773 774 775 776 778 779 781 782 783 784 785 787 788 790 791 792 793 794 796 797 799 800 801 802 803 805 806 808 809 810 811 812 814 815 817 818 819 820 821 823 824 826 827 828 829 830 832 833 835 836 837 838 839 841 842 844 845 846 847 848 850 851 853 854 855 856 857 859 860 862 863 864 865 866 868 869 871 872 873 874 875 877 878 880 881 882 883 884 886 887 889 890 891 892 893 895 896 898 899 900 901 902 904 905 907 908 909 910 911 913 914 916 917 918 919 920 922 923 925 926 927 928 929 931 932 934 935 936 937 938 940 941 943 944 945 946 947 949 950 952 953 954 955 956 958 959 961 962 963 964 965 967 968 970 971 972 973 974 976 977 979 980 981 982 983 985 986 988 989 990 991 992 994 995 997 998 999 

'''












#Q10 Calculate the square of a given number (Using 3 Techniques).
#Ans 10
'''
import random
from random import randint

minvalue= 1
maxvalue = 50

N = random.randint(minvalue,maxvalue)
print("Value of N = ",N)

square = N*N
print("Square = ",square)

user_input = int(input("Enter a number = "))
square1 = user_input*user_input
print("Square = ",square1)

'''
# Output 10
'''
Value of N =  44
Square =  1936

Enter a number =  38457
Square =  1478940849

'''







            



   






