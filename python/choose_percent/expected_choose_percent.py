import itertools
import scipy.misc as scm
from fractions import Fraction
import random

def B(k,w,p):
    return float(scm.comb(w,k,1)*pow(Fraction(repr(p)),k)*pow(Fraction(repr(1-p)),w-k))

def S_B(r,w,p):
    p_total = 0
    for i in range(r+1):
        p_total += Fraction(repr(B(i,w,p)))
    e = 0
    for i in range(r+1):
        e += float(i*Fraction(repr(B(i,w,p)))/p_total)
    return int(round(e))

l = map(float, raw_input().split())
print ""
e = S_B(int(l[1])/2,int(l[1]),l[0])
print(e)
