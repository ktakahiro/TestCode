import itertools
import scipy.misc as scm
from fractions import Fraction
import random

def B(p,w,k):
    return scm.comb(w,k,1)*pow(Fraction(repr(p)),k)*pow(Fraction(repr(1-p)),w-k)

def check_prob(p,alpha,r,f):
    a = 0
    b = 0
    for i in range(alpha+1-(f+1),2*alpha+2-r):
        a += B(p,2*alpha+1-r,i)
    for i in range(alpha+1-r+f,2*alpha+2-r):
	b += B((1-p),2*alpha+1-r,i)
    # print(a,b)
    return float(max(a,b))
    
l = map(float, raw_input().split())
alpha = int(l[1])
n = 2 * alpha + 1
for i in range(0,n+1):
    print "No.{0} : {1}".format(i,check_prob(l[0],alpha,i,0))
