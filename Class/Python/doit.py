import sys

def doit(L):
    for i in range(sys.getsizeof(L)):
        print(" "*i + L[i])
