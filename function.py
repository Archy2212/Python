# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:15:44 2019
least difference will Return the smallest difference between any two numbers
    among a, b and c.
@author: ARCHY MATHUR
"""
#program1(Normal Function)
def least_difference(a,b,c):
    """least difference will Return the smallest difference between any two numbers
    among a, b and c."""
    diff1=abs(a-b)
    diff2=abs(b-c)
    diff3=abs(c-a)
    return(min(diff1,diff2,diff3))
print(least_difference(1,10,100),least_difference(5,6,7))
help(least_difference)

#program2(Function with Default Arguments)
def greet(who="Archy"):
    print("Hello "+who)
greet()
greet("Ashi")
greet(who="Ambuj")

#program3(Function applied to functions)
def mul_by_5(x):
    return 5*x

def mul_by_10(x):
    return 10*x

def call(fn,arg):
    return fn(arg)

def squared_call(fn,arg):
    return fn(fn(arg))

print(call(mul_by_5,3),
call(mul_by_10,3),
squared_call(mul_by_5,3),
sep="\n")

#program4(Higher Order Function)
def mod_5(x):
    return x % 5

print(
'Highest number?',
max(100,22,14),
'highest number with modulo 5?',
max(100,22,14,key=mod_5),
sep="\n"
)