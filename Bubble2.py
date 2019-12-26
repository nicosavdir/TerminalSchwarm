import time
import random as r

Array = []
for k in range(1000000):
    Array.append(r.randint(0,9999))

length= len(Array)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Bubble(A,n):
    i=0
    sort = False
    while(sort==False):
        sort= True
        for i in range (0,n-1):
            if(A[i]>A[i+1]):
                c=A[i]
                A[i]=A[i+1]
                A[i+1]=c
                sort = False
            time.sleep(0.01)
            for a in n:
                print (A[a])
        '''
if x%2 == 0 :
    print(bcolors.WARNING + x + bcolors.ENDC)
    '''
Bubble(Array,length)
