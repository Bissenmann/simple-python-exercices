'''
1.- Ask 10 ages of some of your friends and find the sum, max, min, average and standard deviation.
2.- Do the same with Kms traveled per day.
3.- Ask a string and create a function that returns it backwards.
4.- Ask a string and count the number of vocals and its length.
5.- Ask the parameters of a quadratic equation and return its roots.
6.- Find the ratio between a fibonacci number and its predecessor.
7.- Code a function that returns a Farey sequence of order n.
'''

# Exercise 1: Friends ages
import numpy as np
ages = []
friends = int(input("How many friends do you have? :"))

for i in range(friends):
    ages.append(int(input("How old is your friend? :")))

print(
"\n sum: ", sum(ages),
"\n min: ", min(ages),
"\n max: ", max(ages),
"\n avg: ", sum(ages)/len(ages),
"\n standard variation: ", np.std(ages)
)

#Exercise 2: Kilometers
import numpy as np
kms = []
steps = int(input("How many times did you take the car? :"))

for i in range(steps):
    kms.append(int(input("How many kilometers? :")))

print(
"\n sum: ", sum(kms),
"\n min: ", min(kms),
"\n max: ", max(kms),
"\n avg: ", sum(kms)/len(kms),
"\n standard variation: ", np.std(kms)
)

#Exercise 3: invert string
string = str(input("write anything :"))
string[::-1]

#Exercise 4: Count string
string = str(input("write anything :"))
len(string)

#Exercice 5: Quadratic form calculator (not finished)

import math

print("Where the quadratic form can be written with a,b,c as ax^2 + bx + c = 0")
a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))
d= (b^2)-(4*a*c)

if d >= 0:
    r1= (-b + math.sqrt(d))/2*a
    r2= (-b - math.sqrt(d))/2*a
elif d == 0:
    d
else:
    print("quadratic form is of complex form")

# Exercice 6: Ratio of fibonacci number (not finished)
def fib(n):    # write Fibonacci series up to n """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b

fib(2000)

# Exercise 7: Farey sequence in Python (not finished)
