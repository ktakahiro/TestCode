import itertools
import scipy.misc as scm
from decimal import Decimal
import random

def B(k,w,p):
    return float(scm.comb(w,k,1)*pow(Decimal(repr(p)),k)*pow(Decimal(repr(1-p)),w-k))

def S_B(k,w,p):
    a = 0
    for i in range(k):
        a = a + Decimal(repr(B(i,w,p)))
    return a

l = map(float, raw_input().split())
rand = random.uniform(0,1)
j = 0
w = l[0]
p = l[1]
#print("random : %f" % rand)
#print("start : %f, end : %f" % (S_B(j,int(l[0]),l[1]),S_B(j+1,int(l[0]),l[1])))

s_b = 0
next_s_b = B(j, int(w), p)
while not (s_b <= rand < next_s_b):
    s_b = next_s_b
    next_s_b += B(j, int(w), p)
    j += 1
    #print("start : %f, end : %f" % (S_B(j,int(l[0]),l[1]),S_B(j+1,int(l[0]),l[1])))
print j
