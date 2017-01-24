import numpy as np
import time
import matplotlib.pyplot as plt

def BubbleSort(l):
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
                l[num], l[num+1] = l[num+1], l[num]
    return l
'''
l = [2, 2]
bubbled = BubbleSort(l) 
#print bubbled

def Random_list(size):
    l = np.random.randint(0,100000,size = (1, size))
    return l

#make 2 lists for plotting; x=size of list to sort, y=run time
x = []
y = []

for i in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
    for n in range(100):
        a = Random_list(i)[0]
        start = time.time()
        BubbleSort(a)
        run_time = time.time() - start
        x.append(i)
        y.append(run_time)
y = np.sqrt(y)
plt.scatter(x,y)
plt.xlabel('elements in list')
plt.ylabel('sqrt of run time (sqrt(s))')
plt.title('time complexity of bubble sort')
plt.show()
'''
