import numpy as np
import time
import matplotlib.pyplot as plt

def partition(l,start,end,pivot):
    l[pivot],l[end] = l[end],l[pivot]
    index = start

    for i in range(start,end):
        if l[i] < l[end]:
            l[i],l[index] = l[index],l[i]
            index += 1

    l[index],l[end] = l[end],l[index]
    return index

def quicksort(l, start,end):
    if start >= end:
        return l

    if len(l)%2==0:
        pivot = len(l)/2
    else:
        pivot = len(l)/2-0.5

    new_pivot = partition(l,start,end,pivot)
    quicksort(l,start,new_pivot-1)
    quicksort(l,new_pivot+1,end)

def QS(l):
    if len(l) == 0:
        print 'empty list'
    if len(l) == 1:
        print 'only 1 element in list'
    if len(l)!=len(np.unique(l)):
        print 'deleted duplicates'
    for i in l:
        if type(i) == str:
            print 'not a number'
    l = np.unique(l)
    quicksort(l,0,len(l)-1)
    return l

#print QS([3,4,5,5])
'''
def Random_list(size):
    l = np.random.randint(0,100000,size = (1, size))
    return l

#make 2 lists for plotting; x=size of list to sort, y=run time
x = []
y = []

for i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 999]:
    for n in range(100):
        a = Random_list(i)[0]
        start = time.time()
        QS(a)
        run_time = time.time() - start
        x.append(i)
        y.append(run_time)
x = x*np.log(x)

print len(y)

plt.scatter(x,y)
plt.xlabel('xlogx where x = elements in list')
plt.ylabel('run time (s)')
plt.title('time complexity of quick sort')
plt.show()
'''
