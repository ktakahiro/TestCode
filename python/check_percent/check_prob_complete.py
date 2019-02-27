import itertools
import scipy.misc as scm
from fractions import Fraction
import random

def fail(p,n,s,k,c,r):
    print "fail : {0}C{1}*{2}C{3}*{4}C{5}*{6}^{7}*{8}^{9}/{10}C{11})".format(n-s,k-s,c,n-k,r-1,k,p,k-s,1-p,s,c+r-1,n)
    return scm.comb(n-s,k-s,1)*scm.comb(c,n-k,1)*scm.comb(r-1,k,1)*pow(Fraction(repr(p)),k-s)*pow(Fraction(repr(1-p)),s)

def success(p,n,f,k,c,r):
    print "success : {0}C{1}*{2}C{3}*{4}C{5}*{6}^{7}*{8}^{9}/{10}C{11})".format(n-f,k-f,c,n-k,r-1,k,p,f,1-p,k-f,c+r-1,n)
    return scm.comb(n-f,k-f,1)*scm.comb(c,n-k,1)*scm.comb(r-1,k,1)*pow(Fraction(repr(p)),f)*pow(Fraction(repr(1-p)),k-f)

def check_prob(p,f,s,c,r):
    n = s+f
    suc = 0
    fai = 0
    for j in range(s,n+1):
        fe = fail(p,n,s,j,c,r)
        print("s",j,s)
        print("fail {0} : {1}".format(j,float(fe)))
	fai += fe
    for i in range(f,n+1):
        sa = success(p,n,f,i,c,r)
        print("success {0} : {1}".format(i,float(sa)))
        suc += sa
    print(float(fai),float(suc))
    return float(max([suc,fai]))/float(suc+fai)

l = map(float, raw_input().split())
p = l[0]
c = int(l[1])
r = int(l[2])
add = 0
result = check_prob(p,0,0,c,r)
print "No.{0} : {1}".format(6,result)
