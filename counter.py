import numpy as np
import time
import matplotlib.pyplot as plt

def BubbleSort(l):
    asn_counter = 0
    cond_counter = 0
    if len(l) == 0:
        print 'empty list'
    if len(l) == 1:
        print 'only 1 element in list'
    for i in l:
        if type(i) == str:
            print 'not a number'
    for i in range(len(l)-1,0,-1):
        for num in range(i):
            if l[num] > l[num+1]:
                cond_counter += 1
                l[num], l[num+1] = l[num+1], l[num]
                asn_counter += 1
    return l, asn_counter, cond_counter

def partition(l,start,end,pivot, asn_counter, cond_counter):
    l[pivot],l[end] = l[end],l[pivot]
    index = start
    for i in range(start,end):
        if l[i] < l[end]:
            cond_counter += 1
            l[i],l[index] = l[index],l[i]
            asn_counter += 1
            index += 1

    l[index],l[end] = l[end],l[index]
    asn_counter += 1
    return index, asn_counter, cond_counter

def quicksort(l, start,end, asn_counter, cond_counter):
    if start >= end:
        cond_counter += 1
        return l

    if len(l)%2==0:
        cond_counter += 1
        pivot = len(l)/2
        asn_counter += 1
    else:
        pivot = len(l)/2-0.5
        asn_counter += 1

    new_pivot, asn_counter, cond_counter = partition(l,start,end,pivot, asn_counter, cond_counter)
    asn_counter += 1
    quicksort(l,start,new_pivot-1, asn_counter, cond_counter)
    quicksort(l,new_pivot+1,end, asn_counter, cond_counter)
    return asn_counter, cond_counter

def QS(l):
    asn_counter = 0
    cond_counter = 0
    if len(l) == 0:
        print 'empty list'
    if len(l) == 1:
        print 'only 1 element in list'
    for i in l:
        if type(i) == str:
            print 'not a number'
    asn_counter, cond_counter = quicksort(l,0,len(l)-1, asn_counter, cond_counter)
    return l, asn_counter, cond_counter


def Random_list(size):
    l = np.random.randint(0,100000,size = (1, size))
    return l


'''
Bubble_dict = {}
for i in range(100):
    l = Random_list(10)
    b, asn_counter, cond_counter = BubbleSort(l[0])
    Bubble_dict[i] = [asn_counter, cond_counter]
all_bubble_asn = []
all_bubble_cond = []
for key, value in Bubble_dict.iteritems():
    all_bubble_asn.append(value[0])
    all_bubble_cond.append(value[1])

x= all_bubble_asn
y= all_bubble_cond

plt.scatter(x,y)
plt.xlabel('assignment counts')
plt.ylabel('conditional counts')
plt.title('bubble sort for 100 random lists of 10 elements')
plt.show()
'''


quick_dict = {}

for i in range(100):
    l = Random_list(10)
    q, asn_counter, cond_counter = QS(l[0])
    quick_dict[i] = [asn_counter, cond_counter]
all_bubble_asn = []
all_bubble_cond = []

all_qs_asn = []
all_qs_cond = []
for key, value in quick_dict.iteritems():
    all_qs_asn.append(value[0])
    all_qs_cond.append(value[1])

x= all_qs_asn
y= all_qs_cond

plt.scatter(x,y)
plt.xlabel('assignment counts')
plt.ylabel('conditional counts')
plt.title('quick sort for 100 random lists of 10 elements')
plt.show()
