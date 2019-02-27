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
    print("************************************")
    print(float(p_total))
    print("************************************") 
    print
    print
    biggest = 0
    mode = 0
    for i in range(r+1):
	res = float(Fraction(repr(B(i,w,p)))/p_total)
        # print("when {0} of {1} rational: {2}".format(i,w,res))
	if(biggest < res):
	    biggest = res
	    mode = i
    return mode	

l = map(float, raw_input().split())
print ""
mode = S_B(int(l[1])/2,int(l[1]),l[0])
print("mode : {0}".format(mode))
