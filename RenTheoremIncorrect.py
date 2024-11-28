import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#Theorem 1
def max_probability1(p, k):
    return (2 + 2 * math.sqrt(p/(1-p)))*math.pow(4 * p * (1-p), k)
def min_probability1(p, k):
    return math.pow((4*p*(1-p)), k) / math.sqrt(k)


def p1(i, p):
    return math.pow(((1-p)/p), i-1) * (1 - (1-p)/p)
def p2(j, n, q):
    return math.comb(n, j) * math.pow(q, j) * math.pow((1-q), (n-j))
def f1(i, p):
    return math.pow(((1-p)/p), i)
def f2(j, n, q):
    return sum(p2(l, n, q) for l in range(j+1, n+1))

#Theorem 2
def min_probability2(k, p):
    total = f1(k, p)
    for i in range(1, k+1):
        inner = 0
        for j in range(0, k-i+1):
            inner += p2(j, 2*k+1-i, 1-p) * f1(2*k+2-2*i-2*j, p)
        total +=p1(i, p) * (f2(k-i, 2*k+1-i, 1-p) + inner) 

    return total
 
def max_probability2(k, p):
    total = f1(k, p)
    for i in range(1, k+1):
        inner = 0
        for j in range(0, k-i+1):
            inner = p2(j, 2*k+1-i, 1-p) * f1(2*k+2-2*i-2*j, p)
            total +=p1(i, p) * (f2(k-i, 2*k+1-i, 1-p) + inner) 

    return total
#test cases
#print(max_probability1(.75, 11))
#print(min_probability1(.75, 11))
print(max_probability2(10, .9))
print(min_probability2(10, .9))
print(max_probability2(40, .75))
print(min_probability2(40, .75))
#print(max_probability2(60, .75))
#print(min_probability2(60, .75))
