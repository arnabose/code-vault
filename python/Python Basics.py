#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


print(''' Triple single quote is used to print multiple lines using one print
1. this is line one
2.this is line two
3.this is line three

we also can use triple single quote as well as triple double quote''')


# In[3]:


print(4)


# In[4]:


pip


# In[5]:


# is used for single line comment


# In[7]:


print("Arnab",4) #It can print more than one values. comma generates a space value in output


# In[8]:


print(10*67)   
"""It can print simple equations"""


# In[9]:


#Escape Sequence
print("Hey,I am a good boy and you are a good girl")
print("Hey,I am a good boy \nand you are a good girl")          # \n = new line
print("Hey,I am a \"good boy\" and you are a good girl")        # \" = use to add "" 
print("Hey,I am a \\good boy\\ and you are a good girl")        # \\ = use to add \
print("Hey,I am a good boy \tand you are a good girl")          # \t = tab


# In[10]:


#Print
print("Arnab",4)                      # It can print more than one values
print(12,10,2002,sep="~")                # Separate using ~. Usally the elements are separeted by space default.
print(12,10,2002,sep="~",end="009\n")    # end is print end of that print. Usally new line is created after a print statement but because of the end statement we have to use \n for the new line.
print("Hello")


# # Python Variables and Data Types

# In[11]:


# Variables-> Varibles is like a container that holds data.
# Data Type-> Data Type specifies the type of value a variable holds
# Numerical->int,float,complex
# Text-> str
# Sequenced->list,tuple
# Mapped->dist, set

a=123                                           # int
print(a)
b=4.12                                          #float
print(b)
c="Arnab"                                     # string
print(c)
d=True                                          # bool (True, False)
e=None                                          # none (to mark a variable nothing)
a1=7
print(a+a1)                                     # perform operations with same data type
print("The type of variable a is",type(a))      # type-> show the type of variable
print("The type of variable b is",type(b))
print("The type of variable c is",type(c))
print("The type of variable d is",type(d))
print("The type of variable e is",type(e))


# # Operators

# Arithmatic Operator

# In[12]:


print(5+2)         # +(Addition) Operator perform sum
print(5-2)         # -(Subtraction) Operator perform sub
print(5*2)         # *(Multiplication) Operator perform mul
print(5**2)        # **(Exponential) Operator shows the power of a value
print(5/2)         # /(Division) Operator perform float div
print(5//2)        # //(Floor Division) Operator perform int div
print(5%2)         # %(Modulus) operator shows the remainder


# Assignment operators

# In[13]:


a= 4+12                 #assign the value of 4+12 in a
print(a)


# In[14]:


b = 12
print(b)
b += 4                  #increament the value of b by 4, and then assign it
print(b)
b -= 3                  #decreament the value of b by 3, and then assign it
print(b)
b *= 2                  #multiply the value of b by 2, and then assign it
print(b)
b /= 4                  #divide the value of b by 4, and then assign it
print(b)


# Comparison operator

# In[15]:


d = 5<4
print(d)             #comparison operators always returns boolean value (True/False)


# Logical Operator

# In[16]:


e = True or False          #it performs logical "OR" operation
print(e)
f = False and True         #it performs logical "AND" operation, for more, refer truth table
print(f)
g = not(True)              #performs "NOT" operation
print(g)


# In[17]:


# CALCULATOR
a=20
b=10
print("Sum of",a,"and",b,"is",a+b)        #print statement by default sets a space when we use comma
print("Sub of",a,"and",b,"is",a-b)
print("Mul of",a,"and",b,"is",a*b)
print("Div of",a,"and",b,"is",a//b)


# # Typecasting

# In[18]:


# TYPE CASTING -> The conversion of one data type to another data type
# Explicit type casting -> done by programmer
a="10"                         #str variable
print(type(a))
b="20"                         #str variable
print(type(b))
print(int(a)+int(b))           #type cast to int, and addition operation performed
print(type(int(a)+int(b)))


# In[19]:


# Implicit type casting -> done by python
a=1.2
print(type(a))
b=2
print(type(b))
print(a+b)
print(type(a+b))


# # Input Function

# In[20]:


# USER INPUT
a=input("Enter your name: ")
print("My name is",a)


# In[21]:


x=input("Enter first number:")     # python take a input as string datatype
y=input("Enter second number:")
print(x+y)                         # concat the string
print(int(x)+int(y))               # so, if we want to perform calculation, change the data type into int and then add


# # String

# strings are immutable. which means we cannot change the value of a sting once it initialised.

# In[22]:


# STRING -> String is like an array.It store characters in array
name="Arnab"
aname='Bikash'
text='''hlw            
my name is bose
"I am a boy"'''      # if we want to write a paragraph where space,next line,"" is present then we use'''
print(name)
print(aname)
print(text)


# In[23]:


name="Arnab"
print(name[0])             # String is like an array.
print("Using for loop")
for c in name:
    print(c)               # prints each iteration to a new line       
    
for i in name:
    print(i, end="")        # prints each iteration side wise


# STRING SLICING

# In[24]:


fruit="Mango"
#if we count from start, then index starts with 0
print(fruit[0])
#if we count from end, then index starts with -1 (negative counting)
print(fruit[-1])

print(len(fruit))    # returns lenth of string

print(fruit[0:5])    # variable_name[start index : end index+1] it excludes last index, so we did +1

print(fruit[:5])     # automatically start with 0

print(fruit[1:])     # automatically prints till end of string

print(fruit[:])      # prints the whole string

print(fruit[1:3])    # start from index 1 to 3, excluding 3

print(fruit[-4:-1])  # printing the string from last, but it excludes last index

print(fruit[::-1])   # reverse the string; here interval is -1, so it starts printing from last. str[start:end:interval]

print(sorted(fruit)) # converts the string in a list and sort in alphabetical order


# Slicing with Skip Value

# In[25]:


a= "0123456789"
print(a[1:7:2])     # var_name[start_index : end_index : skip_interval]
b= "elephant"
print(b[0:6:3])


# String Functions

# In[26]:


car= "Volkswagen"
print(len(car))               # len() -> length of string
print(car.endswith("gen"))    # var_name.endswith("")   -> check the given value with last of string. returns boolian value 
print(car.startswith("vol")) # var_name.startswith("") -> check the given value with start of string. case sensitive


# In[27]:


car = "bmw is a gERMAn car brand"
print(car.capitalize())               #capitalize the initial letter of string
print(car.title())                    #Capitalize the initial of each string into upper case
print(car.lower())                    #convert the whole string into lower case
print(car.upper())                    #convert the whole string into upper case

print(car.find("gERMAn"))             #returns the index value of desired string initial value.
print(car.find("audi"))               #returns -1 if not found

print(car.replace("bmw","volvo"))     #replaces all occurence of string with given value
print(car.strip())


# In[28]:


flower = " rose "
print(flower.strip())       #used to remove unwanted characters from starting and ending of a string (removes space by default)
place = "####Kashmir###"
print(place.strip('#'))
print(place.lstrip('#'))    #removes left side 
print(place.rstrip('#'))    #removes right side


# # List

# in python, list are containers to store a set of values of any data type. it is denoted with []. we can change the value of any element inside a list. List are mutable.

# In[29]:


cars= ["bmw", "mercedes", True, 12, "audi", 4.12]
print(type(cars))
print(cars[1])          #prints 1st index
cars[4] = "gogo"        #we can replace value of given index in a list
print(cars)

print(cars[1:4])       # list_name[start_index : end_index]     it ignores the end index (end-1)


# methods of list

# In[30]:


cars.append("volvo")        #adds the value at the end of list
print(cars)


# In[31]:


l = [12,4,21,1,7,99,10]

l.reverse()                #reverse all the elements of list
print(l)

l.insert(4,99)             #list.insert(index_value, item_value) 
print(l)

l.remove(99)              #it will remove given value from list. If more than one value is present, then it will remove the frist index value
print(l)

l.sort()                   #sorts the value of list in ascending order
print(l)


# In[32]:


l.pop(3)                   #it will delete the given index value, and returns the value stored on that index


# # Tuple

# Tuple is immutabel. Value of tuple cannot be changed once assigned. Tuple are containers to store a set of values of any data type.

# In[33]:


t = (9,6,1,4,12,21,7) 
print(type(t))


# In[34]:


a = (3)                     #python will considered it as an integer
print(type(a))
a = (3,)                    #to make it an tuple of one element, put a comma
print(type(a))


# methods of tuple

# In[35]:


print(t.count(12))          #counts occurance of given element in tuple


# In[36]:


# unpacking elements of tuple
t1 = (4,12,7)
x,y,z= t1
print(x,y,z)


# # Dictionary

# dictionary helps to store key value pairs. Dictionary is mutable, indexed, unordered, and cannot comtain duplicate values

# In[37]:


d = {}                            #empty dictionary

food = {"key" : "value", 
         "pizza": 200,
         "burger": 150,
         "momo": 60,
         "patties":45
}
print(food, type(food))

print(food["pizza"])             #return the value of key

print(food.keys())               #return the name of keys
print(food.values())             #return the values of keys
print(food.items())              #return the key value pairs as a list
print(food.get("momo"))          #return the value of key. If key is not present, it will return None

food.update({"pizza":199})       #update the value of provided key, since dictionary is mutable. we can also add value similar way
print(food)

print(food.pop("burger", ))      #dictionary.pop(key, default_value) it will delete the key value pair, and return the value 


# # Sets

# set is a collection of non repeatable data. Set can contain different data types. set is unindexed.

# In[38]:


s = ()                        #an empty set 
s = {12,4,7,21,1,30,5,5,5}
print(s)                     #prints unique valus only, because set cannot contain duplicate values

s.add("gogo")                #adds value to a set
print(s)

print(len(s))               #len of set

s.remove(30)                #removes element from set
print(s)

s.clear()                   #removes all elements from set
print(s)


# Set Operations

# In[39]:


s1 = {1,2,3,4,5,6}
s2 = {2,4,8,12}

print(s1.union(s2))             #prints all the unique values present in both sets
print(s1.intersection(s2))      #prints common values present in both sets

print(s1 - s2)                  #It returns a set difference. Elements present in s1 but NOT in s2.
print(s2 - s1)                  #Elements present in s2 but NOT in s1.

a = {2, 4}
print(a.issubset(s1))           # True, as subset is a set, whose all elements are contained inside of another set. 


# # Conditional statement

# In[40]:


marks = int(input("Enter your marks: "))
if marks >= 90:                                        #checks the condition
    print("Grade A")                                   #gap is known as indentation. which indicates the block of a code 
elif marks >= 70:                                      #used for conditional statement
    print("Grade B")                     
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# In[41]:


#Two or more if statement in one program
marks = int(input("Enter your marks: "))

#if statement 1 (runs independently)
if marks == 0:
    print("your marks is 0")
    
#if statement 2
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")                     
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# In[42]:


# and returns True only if both conditions are True.
# or returns True if at least one condition is True.
# not reverses the result.

name = input("Enter name: ")
age = int(input("Enter age: "))

if (name == "Susmita" or name == "Arnab") and age >= 18:
    print("Access Allowed")
else:
    print("Access Denied")


# # Loops

# while loop

# In[43]:


i = 1
while (i<6):                   # this block will execute untill the condition is false
    print(i)
    i += 1                     # must to increase the value, else it will be an infinite loop


# In[44]:


#printing elements of list using while loop
flowers = ["lotus","rose","Lily",12,"tulip"]

i=0
while (i < len(flowers)):
    print(flowers[i])
    i = i+1


# for loop

# In[45]:


for i in range (4):           # range starts from 0 to n-1
    print(i)


# In[46]:


for i in range (0,100,12):           #range (start, stop, step_size)
    print(i)


# In[47]:


#printing elements of list using for loop (can also be done with string, tuple)
flowers = ["lotus","rose","Lily",12,"tulip"]

for i in flowers:
    print(i)


# In[48]:


#for loop can also ve executed with else
s = "Puppy"

for i in s:
    print(i)
else:
    print("is cute")                # prints when forloop is fully executed


# Break, Continue and Pass

# In[49]:


for i in range(100):
    if (i==4):
        break                       # break forcefully exits the loop
    print(i)


# In[50]:


for i in range(10):
    if (i==4):
        continue                       # continue skips the iteration
    print(i)


# In[51]:


for i in range(100):
    pass                         #pass is used to skip or do nothing, without pass,this incomplete for loop will throw error

i=0
while(i<4):
    print(i)
    i +=1


# # Function

# In[52]:


#avg of 3 numbers using python

def avg():                                   #function definition
    a= int(input("Enter 1st number: "))
    b= int(input("Enter 2nd number: "))
    c= int(input("Enter 3rd number: "))  
    print((a+b+c)/3)

avg()                                        #function calling


# In[53]:


#function with arguments

def msg(name1, name2):
    print(f"Have a good day {name1} and {name2}")
    print("Have a good day " + name1 + " and " + name2)
    print("Have a good day", name1,"and",name2)
    
msg("Arnab","Client")                               #passing arguments while function calling


# In[54]:


#function with return value

def msg(name):
    print(f"Have a good day {name}")
    return "okay"

value = msg("Arnab")                     #return value stored in variable
print(value)


# In[55]:


#function with default argument

def msg(name, ending="Thank you"):
    print("Have a good day", name)
    print(ending)
    
msg("Gogo")                             #function calling without passing value vor "ending", so it will return default value
msg("Gogo","Thanks")                    #function calling by passing value vor "ending"


# # Recursion

# a function calls itself

# In[56]:


"""
factorial(0)= 1
factorial(1)= 1
factorial(2)= 2*1
factorial(3)= 3*2*1
factorial(4)= 4*3*2*1
factorial(5)= 5*4*3*2*1

factorial(n)= n * (n-1)*(n-2)*....*3*2*1

factorial(n)= n * factorial(n-1)
"""

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

a=int(input("Enter a number: "))
print(f"Factorial of {a} is {factorial(a)}")


# # Taking inputs from user

# In[57]:


# Single input string
name = input("Enter your name: ")
print(name)


# In[58]:


# Single integer input
age = int(input("Enter age: "))
print(age)


# In[59]:


# Single float input
price = float(input("Enter price: "))
print(price)


# In[61]:


# Multiple Inputs in One Line (Space Separated)
a, b = map(int, input().split())
print(a, b)


# In[62]:


# Multiple Inputs in One Line (Comma Separated)
arr = list(map(int,input().split(',')))        #if user give a string "12,5,3,1,8", then it will convert entire sting in integer
print(arr)


# In[63]:


# List of Integers (space ceparated) (array input)
# .split()         -> splits the sting (space separated).                                          Ex: ['1' '2' '3' '4' '5']
# .split(',')      -> splits the sting (comma separated).                                          Ex: ['1','2','3','4','5']
# .map(int, )      -> it changes datatype (int,float) to every item in an iteration (list, tuple). Ex: [1,2,3,4,5]

arr = list(map(int, input().split()))
print(arr)


# In[64]:


# List of Strings 
words = input().split()
print(words)


# In[65]:


# Taking N Inputs Using Loop
n = int(input())
arr = []

for _ in range(n):                     # _ means I dont care about variable name
    arr.append(int(input()))

print(arr)


# In[28]:


# 2D matrix input
rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]
print(matrix)


# In[13]:


# 2D matrix input (another type)

rows, cols = map(int, input("Enter row and column: ").split())   # input() → takes "3 3" (string);    size of row and column
                                                                 # .split() → ['3', '3']
                                                                 # map(int, ...) → converts to integers → [3, 3]
matrix = []                                                      # creates an empty list

for i in range(rows):
    row = list(map(int, input().split()))                        # input() → "1 2 3"
                                                                 # .split() → ['1','2','3']
                                                                 # map(int, ...) → [1,2,3]
                                                                 # list() → [1,2,3]
    matrix.append(row)

print(matrix)


# In[29]:


# character input
ch = input()[0]
print(ch)


# In[33]:


# Boolean input
flag = input().lower() == "true"
print(flag)


# # Output

# In[5]:


student = [('susmita', 89), ('arnab', 56), ('arpan', 45), ('bikash', 32), ('priya', 78)]

for name, marks in student:                       #for printing two elements inside a list
    print(name, marks)


# Round off of float

# In[9]:


num = 12.123454356476453
print(f"{num:.3f}")


# # Lambda Function
# A lambda function is a small anonymous (nameless) function written in one line.

# In[36]:


def cube(x):
    return x*x*x

# instead of writing the above function, we can write the same using lambda

mul = lambda x : x*x*x              # lambda argument: expression

print(cube(3))
print(mul(3))


# In[37]:


add = lambda a,b : a+b
print(add(4,12))


# In[38]:


arr = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, arr))          #multiplies each element of array with 2
print(result)


# filter()

# In[39]:


# filter() is used to select elements from an iterable (like list) based on a condition.
# It keeps elements that return True.

arr = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, arr))        # filter(function, iterable_name)        iterable menas list/tuple
print(evens)


# In[41]:


#sorted

pairs = [(1, 3), (4, 1), (5, 2), (3, 9)]

pairs.sort()                        # by default it sorts the list based on the first element of tuple.
print(pairs)

pairs.sort(key=lambda x: x[1])      # For each element x in pairs, use x[1] (second value of tuple) for comparison.
                                    # key is a function that tells Python: “On what basis should I sort the elements?” 
print(pairs)


# Sorting

# In[66]:


smartphone = ["samsung","apple","vivo","xiaomi","1+","lyf"]
smartphone.sort(key=len)            # sort using condition (key)
print(smartphone)

smartphone.sort()                   # sort the entire string alphabetically 
print(smartphone)

