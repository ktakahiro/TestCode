import itertools
import scipy.misc as scm
from decimal import Decimal
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def binomial(k,N,p):
    return Decimal(repr(scm.comb(N,k,1)))*(Decimal(repr(p))**k)*(Decimal(repr(1-p))**(N-k))

def model_percent(N,p):
    a = 0
    b = 0

    s1 = int(float(N)/2)
    s2 = math.ceil(float(N)/2)
    for i in range(0,s1+1):
        a += binomial(i,N,p)
    res1 = 1 - (a * Decimal(repr(p)))

    for i in range(s2,N+1):
        b += binomial(i,N,p)
    res2 = b * Decimal(repr(p))
    return (res2/res1)

x = []
y = []
for i in range(1,51,2):
    y_temp = 1 - model_percent(i,0.33)
    x.append(i)
    y.append(y_temp)
    x.append(i+1.999)
    y.append(y_temp)

plt.plot(np.asarray(x), np.asarray(y))
plt.show()
