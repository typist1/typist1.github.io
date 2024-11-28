import math
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd
e = 2.71828182845904523536028747135266249775724709369995957496696762772
#Theorem 1
def max_probability1(p, k, l, d):
    a = p * math.pow(e, (l * d * -1))
    #print(a)
    return ((2 + 2 * math.sqrt(a/(1-a))))*math.pow(4 * a * (1-a), k)
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
def max_probability2(k, p, l, d):
    a = p * math.pow(e, (l * d * -1))
    total = f1(k, a)
    for i in range(1, k+1):
        inner = 0
        for j in range(0, k-i+1):
            inner += p2(j, 2*k+1-i, 1-a) * f1(2*k+1-2*i-2*j, a)
        total += p1(i, a) * (f2(k-i, 2*k+1-i, 1-a) + inner)

    return total 
def min_probability2(k, p):

    total = f1(k, p)
    for i in range(1, k+1):
        inner = 0
        for j in range(0, k-i+1):
            inner += p2(j, 2*k+1-i, 1-p) * f1(2*k+2-2*i-2*j, p)
        total +=p1(i, p) * (f2(k-i, 2*k+1-i, 1-p) + inner) 

    return total
#test cases
#print(max_probability1(.9, 10, 1/600, 10))
#print(min_probability1(.9, 10))
#print(max_probability1(.75, 11))
#print(min_probability1(.75, 11))
#print(max_probability2(10, .9, 1/600, 10))
#print(min_probability2(10, .9))
#print(max_probability2(0, .6, 1/600, 10))
#print(min_probability2(0, .6))
#print(max_probability2(40, .75))
#print(min_probability2(40, .75))
#print(max_probability2(60, .75))
#print(min_probability2(60, .75))

xCounts = np.arange(0, 101, 10)
xCounts2 = np.arange(1, 102, 10)
newCounts = np.arange(50, 91, 10)
max1 = []
for i in xCounts:
    a = max_probability1(.9, i, 1/600, 10)
    max1.append(a)

max2 = []
for i in xCounts2:
    a = max_probability2(i, .9, 1/600, 10)
    max2.append(a)

min1 = []
for i in xCounts2:
    a = min_probability1(.9, i)
    min1.append(a)

min2 = []
for i in xCounts2:
    a = min_probability2(i, .9)
    min2.append(a)

max11 = []
for i in newCounts:
    a = max_probability1(i/100, 6, 1/600, 10)
    print(a)
    max11.append(a)

min11 = []
for i in newCounts:
    a = min_probability1(i/100, 6)
    min11.append(a) 

max22 = []
for i in newCounts:
    a = max_probability2(6, i/100, 1/600, 10)
    max22.append(a)

min22 = []
for i in newCounts:
    a = min_probability2(6, i/100)
    min22.append(a)

'''
plt.yscale('log')
plt.title("Probability of Safety Violation vs. Confirmation Depth")
plt.ylabel("Probability of safety violation")
plt.xlabel("Confirmation Depth (k)")
'''
for i in range(0, 101, 20):
    '''
    plt.scatter(i, max_probability1(i/100, 6, 1/600, 10), color='blue')
    yCoord = '{:.3f}'.format(max_probability1(i/100, 6, 1/600, 10))
    plt.annotate(f'({i}, {yCoord})', (i,  max_probability1(i/100, 6, 1/600, 10)), xytext=(i-4,  max_probability1(i/100, 6, 1/600, 10)), ha='center', fontsize=8)

    plt.scatter(i, min_probability1(i/100, 6), color='orange')
    yCoord = '{:.3f}'.format(min_probability1(i/100, 6))
    plt.annotate(f'({i}, {yCoord})', (i,  min_probability1(i/100, 6)), xytext=(i-3.5,  min_probability1(i/100, 6)), ha='center', fontsize=8)
    '''

    '''
    plt.scatter(i, max_probability2(6, i/100, 1/600, 10), color='blue', alpha=0.7)
    yCoord = '{:.3f}'.format(max_probability2(6, i/100, 1/600, 10))
    if i == 50:
        plt.annotate(f'({i}, {yCoord})', (i,  max_probability2(6, i/100, 1/600, 10)), xytext=(i+1,  max_probability2(6, i/100, 1/600, 10)-.3), ha='center', fontsize=8)
    else:
        plt.annotate(f'({i}, {yCoord})', (i,  max_probability2(6, i/100, 1/600, 10)), xytext=(i-3,  max_probability2(6, i/100, 1/600, 10)), ha='center', fontsize=8)

    plt.scatter(i, min_probability2(6, i/100), color='orange', alpha=0.7)
    yCoord = '{:.3f}'.format(min_probability2(6, i/100))
    if i > 50: #don't print first annotation
        plt.annotate(f'({i}, {yCoord})', (i,  min_probability2(6, i/100)), xytext=(i-3,  min_probability2(6, i/100)), ha='center', fontsize=8)
    ''' 

    '''
    plt.scatter(i, max_probability1(.9, i, 1/600, 10), color='blue')
    yCoord = '{:.2e}'.format(max_probability1(.9, i, 1/600, 10))
    if i !=0:
        plt.annotate(f'({i}, {yCoord})', (i-1, max_probability1(.9, i, 1/600, 10)), xytext=(i-12, max_probability1(.9, i, 1/600, 10)), ha='center', fontsize=8)

    if i == 0:
        i+=1

    plt.scatter(i, min_probability1(.9, i), color='orange')
    yCoord = '{:.2e}'.format(min_probability1(.9, i))
    if i != 1:
        plt.annotate(f'({i}, {yCoord})', (i-1, min_probability1(.9, i)), xytext=(i-12, min_probability1(.9, i)), ha='center', fontsize=8)
    '''

    '''
    plt.scatter(i, max_probability2(i, .9, 1/600, 10), color='blue')
    yCoord = '{:.2e}'.format(max_probability2(i, .9, 1/600, 10))
    if i > 0:
        plt.annotate(f'({i}, {yCoord})', (i-1, max_probability2(i, .9, 1/600, 10)), xytext=(i-12, max_probability2(i, .9, 1/600, 10)), ha='center', fontsize=8)

    plt.scatter(i, min_probability2(i, .9), color='orange')
    yCoord = '{:.2e}'.format(min_probability2(i, .9))
    if i > 0:
        plt.annotate(f'({i}, {yCoord})', (i-1, min_probability2(i, .9)), xytext=(i-12, min_probability2(i, .9)), ha='center', fontsize=8)
    '''
'''
plt.plot(xCounts, max1, linestyle="--", label="Theorem 1 Maximum")
plt.plot(xCounts2, min1, label="Theorem 1 Minimum")
plt.text(50, math.pow(10, -10), '90% Honest')
plt.legend()
plt.savefig("1maxAndMin.png", dpi=500, transparent = True)
'''
'''
plt.text(50, math.pow(10, -10), '90% Honest')
plt.plot(xCounts, max1, linestyle="--", label="Theorem 1 Maximum")
plt.plot(xCounts2, min1, label="Theorem 1 Minimum")
plt.legend()
'''

'''
plt.text(55, 0.01, "Confirmation depth of 6")

plt.title("Probability of Safety Violation vs. Honest Percentage")
plt.ylabel("Probability of safety violation")
plt.xlabel("Honest Percentage (%)")
plt.yscale('log')
plt.legend()
'''

#0.001 probability of safety violation
honest = [70, 80, 90]
t1max = [56, 22, 10]
t1min = [30, 13, 6]
t2max = [47, 18, 8]
t2min = [43, 17, 7]

#based on 0.001 probability of safety violation
renTheorems_df = pd.read_excel("renTheorems.xlsx")
#print(renTheorems_df.to_string())
barplot = sns.barplot(data=renTheorems_df, x='Honest Percentage (%)', y='Confirmation Depth (k)', hue='Theorems', palette='YlOrBr')
plt.title("Confirmation Depth vs. Honest Percenage of each Theorem")
sns.set_style('dark') #white, whitegrid, dark, darkgrid, ticks
sns.set_context('paper') #talk, poster, paper
#sns.despine(left=True, bottom=True, right=True) #remove axes lines


for bar in barplot.patches:
    bar_height = int(bar.get_height())
    if bar_height > 0:
        barplot.annotate(format(bar_height),
                        xy=(bar.get_x() + bar.get_width() / 2, bar_height),
                        xytext=(0,0),
                        textcoords = "offset points",
                        ha='center', va='bottom')
plt.text(0.75, 37, "Probability of Safety\n Violation of 0.001")
plt.savefig("renTheoremBarChart.png", dpi=500, transparent = True)
plt.show()
