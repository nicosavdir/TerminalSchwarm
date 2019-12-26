import time
import random as r

max = 9999

Array = []
for k in range(80):
    Array.append(r.randint(0,max))

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
    oida=0
    sort = False
    while(sort==False):
        oida+=max/10
        sort= True
        for i in range (0,n-1):
            if(A[i]>A[i+1]):
                c=A[i]
                A[i]=A[i+1]
                A[i+1]=c

                sort = False
            time.sleep(0.01)

            for j in range(n):
                if A[j] < oida:
                    print(bcolors.WARNING + str(A[j]), end=' ')
                elif A[j]> 1000 and A[j]<= oida:
                    print(bcolors.FAIL + str(A[j]), end=' ')
                elif A[j]> 1000 and A[j]<= 2000:
                    print(bcolors.OKGREEN + str(A[j]), end=' ')
                else:
                    print(bcolors.ENDC + str(A[j]), end=' ' )




Bubble(Array,length)
