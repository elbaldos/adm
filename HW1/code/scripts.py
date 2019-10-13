### PROBLEM 1
## Introduction
# Say "Hello, World!" With Python
my_string = "Hello, World!"
print(my_string)

# Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0: 
    print("Weird")
else:
    if n in range(2,6): print("Not Weird")
    elif n in range(6,21): print("Weird")
    else: print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b)
print(a-b)
print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())

for i in range(0,n):
    print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 100 != 0:
        if year % 4 == 0: leap = True
    if year % 400 == 0: leap = True
    return leap

# Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

x = range(1, n+1)

for i in x:
    print(i, end = '')

## Data types 
# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

l = [ [i , j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k != n ]

print(l)

# Find the Runner-Up Score! 
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr) #set could have as input also a map, not necesasrily a list
    s.remove(max(s))
    print(max(s))

# Nested Lists
if __name__ == '__main__':
    l = [[input(), float(input()) ] for _ in range(int(input())) ]
    grades = [row[1] for row in l]
    s = set(grades)
    s.remove(min(s))
    name_list = [row[0] for row in l if row[1] == min(s)]
    name_list.sort(reverse=False)
    for i in name_list:  print(i)

# Finding the percentage
if __name__ == '__main__':
    import statistics
    n = int(input())
    #Creation of the Dictionary
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
    #*line: all the rest after the first splitting goes into 'line'
    #    scores = list(map(float, line))
    #    student_marks[name] = scores
        student_marks.update({name :  list(map(float, line)) })
    
    #DICTIONARIES interesting
    #You can Add a dictionary to another dictionary

    query_name = input()
    avg = '%.2f' % round(statistics.mean(student_marks[query_name]), 2)
    #round() is rounding, but 5 is not 5.00
    #the statement '%.2f' % set the number of decimal
    print(avg)

# Lists
if __name__ == '__main__':
    N = int(input())
    l = []
    for index in range(N):
        command, *listInst = input().split()
        if listInst: listInst = list(map(int, listInst))
        #instructions
        if command == 'insert': l.insert(listInst[0], listInst[1])
        elif command == 'print': print(l) 
        elif command == 'remove': l.remove(listInst[0])
        elif command == 'append': l.append(listInst[0])
        elif command == 'sort': l.sort(key=int, reverse=False)
        elif command == 'pop': l.pop()
        elif command == 'reverse': l.reverse()
    # eval("l." + cmd) would have been smarter
    # where    cmd =  command + "("   +  ",".join(listInst)  +    ")"
    # eval() execute the instruction passed as a string
    # it  parses the expression passed to this method and execute the expression
    # in this case, we need a string and we don't have to cast into integer the string: we don't need line 6
    # print has to be managed separately

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    #With tuples you cannot change the position = ()
    #Lists are completely dinamic and you can change elements = []
    print(hash(tuple(integer_list)))

## Strings 
# Capitalize! (Wrong Answer)
def solve(s):
    newS = ''
    for nameWord in s.split():
        #newS += nameWord.capitalize() without next 5 lines
        index = 0
        for character in nameWord:
            if index == 0: newS += character.upper()
            else: newS += character.lower()
            index += 1
        newS += " "
    return newS.rstrip()


# sWAP cASE
import string

def swap_case(s):
    #newS = s.swapcase()  #it already exists
    newS = ''
    for letter in s:
        if letter in set(string.ascii_uppercase): newS += letter.lower()
        elif letter in set(string.ascii_lowercase): newS += letter.upper()
        else: newS += letter
    return newS


# String Split and Join
def split_and_join(line):
    # write your code here
    # line.replace(" ", "-", [line.count(" ")] ) #whit replace
    #with default in [count] parameter you replace all the occurencies
    newS = ""
    arr = line.split(" ")
    newS = "-".join(arr)
    return newS

# What's Your Name?
def print_full_name(a, b):
    a = a.strip()
    b = b.strip()
    print("Hello " + a + " " + b + "! You just delved into python.")


# Mutations
def mutate_string(string, position, character):
    #string[4] = 'H' #it doesn't work, 'str' object does not support item assignment
    lst = list(string)
    lst[position] = character
    return ''.join(lst)

# Find a string
def count_substring(string, sub_string):
    #string.count(sub_string, 0, len(string) ) #Doesn't work correctly for the overlapping
    count = 0
    index = 0
    while True:
        index = string.find(sub_string, index) #if nothing is found, it returns -1
        if index >= 0:
            count += 1
            index += 1
        else: break
    
    return count

# String Validators
if __name__ == '__main__':
    s = input()
    lst = list(s)
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for character in lst:
        if character.isalnum(): alnum = True
        if character.isalpha(): alpha = True
        if character.isdigit(): digit = True
        if character.islower(): lower = True
        if character.isupper(): upper = True
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


# Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    #print(reverse_cone.rjust(thickness*6))
    print(( (c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)  ).rjust(thickness*6)) 

# Text Wrap
def wrap(string, max_width):
    # textwrap.fill(string, max_width) is equivalent
    divid = len(string)
    divis = max_width
    quot = divid // divis
    remain = divid % divis
    newS=''
    line = 0
    
    for i in range(quot):
        newS += string[i*max_width:(i+1)*max_width] + '\n'
        line += 1
    if line != 0: newS += string[line*max_width:]
    return newS


# Designer Door Mat
#Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split()) #This must be an odd number
# The number of line of the cones is connected with the dimension of the problem
coneLine = n // 2

#Top Cone
for i in range(coneLine): print(('.|.'*(i*2+1)).center(m, '-'))

#Welcome Message
print('WELCOME'.center(m, '-'))    

#Bottom Cone
for i in range(coneLine): print(('.|.'*((coneLine-i)*2-1)).center(m, '-'))

# String Formatting
 def print_formatted(number):
    binLength = number.bit_length()
    # The following conversion are not necessaries
    #octa, hexa, bina = oct(number), hex(number), bin(number)
    #'0x' prefix represent hexadecimal
    #'0b' prefix is for binary
    #'0o' prefix is for octal
    # octa.lstrip('0o')

    for i in range(1,number+1):
        print("{0:{width}} {1:{width}o} {2:{width}X} {3:{width}b}".format(i, i, i, i, width = binLength))


# Alphabet Rangoli
def print_rangoli(size):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    beltLength = size*2-1 + (size-1)*2  #Number of Character + Number of "-"
    # The number of line of the cones is connected with the dimension of the problem
    # There is a center letter which rolls toward the bounds

    # The lines of the two cones are simmetric
    lst = []
    # Putting into a list the set of the single line of the cone
    for i in range(size):
        s = "-".join(letters[i:size])
        lst.append((s[::-1]+s[1:]).center(beltLength, "-"))
    # We obtained the bottom cone and the center line
    
    # We have to create the upper cone from the previous object
    # lst[:0:-1] reverse the array and stop at the position 0-1 (excluding the 1st line)
    print("\n".join(lst[:0:-1] + lst))



# The Minion Game
def minion_game(string):
    # your code goes here
    kevinScore = 0
    stuartScore = 0
    vowels = 'AEIOU'
    
    # Calculating Scores
    # From any character, counting of how many substring I can type
    # The rule is number of words = length(string) - index(character) whitin the string 
    for i in range(len(string)):
        if string[i] in vowels: kevinScore += (len(string)-i)
        else: stuartScore += (len(string)-i)

    # Printing the output (print is not present in the blocked way of invoking)
    out = "Draw"
    if kevinScore > stuartScore: out = "Kevin " + str(kevinScore)
    elif kevinScore < stuartScore: out = "Stuart " + str(stuartScore)
    print(out)

 
# Merge the Tools!

## Sets
#The Captain's Room  (Wrong Answer)
import sys

# Read input from STDIN. Print output to STDOUT
k = int(sys.stdin.readline())
listRoomPeople = list(map(int, sys.stdin.readline().strip().split()))
setRoom = set(listRoomPeople)

# Searching the unique element with #PEOPLE = 1 (The Captain)
strOut = ''
for i in setRoom:
    if listRoomPeople.count(i) == 1:
        strOut = str(i)
        break
# With List of Comprehension
# captainRoom = [ str(i) for i in setRoom if listRoomPeople.count(i) == 1]
# strOut = captainRoom[0]

# Output
sys.stdout.write(strOut)

#Introduction to Sets
def average(array):
    setH = set(array)
    L = list(setH)
    average = sum(L) / len(L)
    return average
#No Idea!
import sys

# Read input from STDIN. Print output to STDOUT
n , m = map(int, sys.stdin.readline().split())
myList = list(map(int, sys.stdin.readline().split()))
setLike = set(map(int, sys.stdin.readline().split()))
setNotLike = set(map(int, sys.stdin.readline().split()))


# Lists Approach (not working, exceeding time limit)
#listLike = list(setLike)
#listNotLike = list(setNotLike)

# Calculating the score of happiness

#for elem in myList:
#    happiness += (+1)*listLike.count(elem)
#    happiness += (-1)*listNotLike.count(elem)

# Sets Approach
happiness = sum([(elem in setLike) - (elem in setNotLike) for elem in myList])
# (elem in setLike) turns True if elem is in setLike, then you SUM

# Output
strHappy = str(happiness)
sys.stdout.write(strHappy)

#Symmetric Difference
import sys
#Read input from STDIN. Print output to STDOUT
n1 = sys.stdin.readline()
set1 = set(sys.stdin.readline().split())
n2 = sys.stdin.readline()
set2 = set(sys.stdin.readline().split())

# Operation on Sets
sd = set1.symmetric_difference(set2)
lsd = list(sd)
lsd.sort(key=int, reverse=False)
s = "\n".join(lsd)

# Printing with sys.stdout
sys.stdout.write(s)

#Set .add() 
import sys
# print(len(set([str(input()) for x in range(int(input()))])))
# One Line without add()

#Read input from STDIN. Print output to STDOUT
# Dimension of the Sample
strDim = sys.stdin.readline()

# Initialitazion Set
setAlpha = set()
# Adding elements to set by input STDIN
n = int(strDim)
for i in range(n):
    line = sys.stdin.readline().strip() # dirty imput
    setAlpha.add(line)

# Operation on Sets
count = len(setAlpha)

# Printing with sys.stdout
# print: first converts the object to a string (if it is not already a string). It will also put a space before the object if it is not the start of a line and a newline character at the end.
# Using stdout, you need to convert the object to a string yourself and there is no newline character.
countStr = str(count)
sys.stdout.write(countStr)

#Set .discard(), .remove() & .pop()
import sys

# Setting dimensions and set
n = int(input())
s = set(map(int, input().split()))

# Operation on the set
m = int(input())
for i in range(m):
    command, *lstEl = input().strip().split()
    if lstEl: lstEl = list(map(int, lstEl))
    
    # Building the statement for eval() and executing
    if command.lower() == "pop": s.pop()
    else: [ eval("s." + command + "(" + str(lstEl[j]) + ")") for j in range(len(lstEl)) ]

lstSet = list(s)
strOut = str(sum(lstSet))
sys.stdout.write(strOut)

#Set .union() Operation
import sys

#Read input from STDIN. Print output to STDOUT
nEng = sys.stdin.readline()
setEng = set(map(int,sys.stdin.readline().split()) )
nFre = sys.stdin.readline()
setFre = set(map(int,sys.stdin.readline().split()) )

#Union
setSchool = setEng | setFre
# Operation
lstSchool = list(setSchool)

# Output
strOut = str(len(lstSchool))
sys.stdout.write(strOut)

#Set .intersection() Operation
import sys

#Read input from STDIN. Print output to STDOUT
nEng = sys.stdin.readline()
setEng = set(map(int,sys.stdin.readline().split()) )
nFre = sys.stdin.readline()
setFre = set(list(map(int,sys.stdin.readline().split()) ) ) #Trying with lists

#Union
setSchool = setEng.intersection(setFre) #Works also with lists in the input
#Equivalent: setEng & setFre #it only operates on the set of elements in set

# Operation
lstSchool = list(setSchool)

# Output
strOut = str(len(lstSchool))
sys.stdout.write(strOut)

#Set .difference() Operation
import sys

#Read input from STDIN. Print output to STDOUT
nEng = sys.stdin.readline()
setEng = set(list(map(int,sys.stdin.readline().split()) )  ) #Trying with lists
nFre = sys.stdin.readline()
setFre = set(map(int,sys.stdin.readline().split()) ) 

#Union
setJustEng = setEng.difference(setFre)
#Equivalent: setEng - setFre #it only operates on the set of elements in set

# Operation
lstJustEng = list(setJustEng)

# Output
strOut = str(len(lstJustEng))
sys.stdout.write(strOut)


#Set .symmetric_difference() Operation
import sys

#Read input from STDIN. Print output to STDOUT
nEng = sys.stdin.readline()
setEng = set(map(int,sys.stdin.readline().split()) )  
nFre = sys.stdin.readline()
setFre = set(map(int,sys.stdin.readline().split()) ) 

#Union
setSymDif = setEng ^ setFre
#Equivalent: setEng.symmetric_difference(setFre)

# Operation
lstSymDif = list(setSymDif)

# Output
strOut = str(len(lstSymDif))
sys.stdout.write(strOut)

#Set Mutations
import sys

# Read input from STDIN. Print output to STDOUT

# Settings of the base set
n = int(sys.stdin.readline())
leftSet = set(map(int, sys.stdin.readline().split()))

# Operations List Dimension
m = int(sys.stdin.readline())

# Operations on the leftSet
for i in range(m):
    command, *dimSet = sys.stdin.readline().strip().split() # '*'is not necessary here
    #'*' in the assignment creates a list in the case we have more space for splicing in the string, in this case we have to use map(int, dimSet) for casting into an integer
    # because we have an iterable
    if dimSet: dimSet = map(int, dimSet)
    # COMMENT: it would have been more efficient the followings line of code:
    # command, dimSet = sys.stdin.readline().strip().split()
    # if dimSet: dimSet = int(dimSet)

    rightSet = set(map(int, sys.stdin.readline().split()))

    # Building the statement for eval() and executing
    eval("leftSet." + command + "(rightSet)")

# Output
lstSet = list(leftSet)
strOut = str(sum(lstSet))
sys.stdout.write(strOut)

#Check Subset
import sys

# Read input from STDIN. Print output to STDOUT
# Number of test cases
n = int(sys.stdin.readline())

for i in range(n):
    n1 = int(sys.stdin.readline())
    s1 = set(map(int, sys.stdin.readline().split()))
    n2 = int(sys.stdin.readline())
    s2 = set(map(int, sys.stdin.readline().split()))

    # Checking on the sets
    strOut = str(False)
    if n1 <= n2:
        strOut = str(s1.issubset(s2))
        # The above code checks if s1 is a subset of s2 
        
        # Output
        sys.stdout.write(strOut + '\n')   
    else:
        sys.stdout.write(strOut + '\n')


#Check Strict Superset
import sys

# Read input from STDIN. Print output to STDOUT
sampleSet = set(map(int, sys.stdin.readline().split()))
nSS = len(sampleSet)
n = int(sys.stdin.readline())

# Reverse Checking
strOut = str(True)
for i in range(n):
    testingSet = set(map(int, sys.stdin.readline().split()))
    nTS = len(testingSet)
    
    # Checking on the sets
    if nSS >= nTS:
        if not sampleSet.issuperset(testingSet):
            strOut = str(False)

# Output
sys.stdout.write(strOut)

##Collections
# collection.Counter() (incomplete)
import sys
from collections import Counter

# Setting dimensions and set
n = int(sys.stdin.readline())   # Shoes
myList = list(map(int, sys.stdin.readline().strip().split()))  #Sizes
m = int(sys.stdin.readline())   # Customers
earnings = 0

# Collections.Counter()
counterShoes = Counter(myList)

# Operation above the Counter
for i in range(m):
    (1 == 1)

# Output
strOut = str(earnings)
sys.stdout.write(strOut)



### PROBLEM 2
#Birthday Cake Candles

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    set_height = set(ar)
    max_elem = max(set_height)
    count = 0
    for elem in ar:
        if elem == max_elem: count += 1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
