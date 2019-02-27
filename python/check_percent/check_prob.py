import itertools
import scipy.misc as scm
from fractions import Fraction
import random

def B(p,w,k):
    return scm.comb(w,k,1)*pow(Fraction(repr(p)),k)*pow(Fraction(repr(1-p)),w-k)

def check_prob(p,n,r):
    a = 0
    b = 0
    for i in range(n+1-r,2*n+2-r):
        a += B(p,2*n+1-r,i)
        b += B((1-p),2*n+1-r,i)
    return round(a * Fraction(repr(p)) + b * Fraction(repr(1-p)),7)
    
l = map(float, raw_input().split())
for i in range(1,int(l[1])+1):
    print "No.{0} : {1}".format(i,check_prob(l[0],int((l[1])/2),i-1))
