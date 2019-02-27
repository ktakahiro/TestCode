import itertools
import scipy.misc as scm
from decimal import Decimal
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def b(k,N,p):
    return Decimal(repr(scm.comb(N,k,1)))*(Decimal(repr(p))**k)*(Decimal(repr(1-p))**(N-k))

def model_percent(N,p):
    a = Decimal('0')
    s = math.ceil(float(N)/2)
    for i in range(s,N+1):
        a = a + b(i,N,p)
    return a * Decimal(repr(p))

x = []
y = []
for i in range(1,51,2):
    y_temp = float(model_percent(i,0.33))
    x.append(i)
    y.append(y_temp)
    x.append(i+1.999)
    y.append(y_temp)

plt.plot(np.asarray(x), np.asarray(y))
plt.show()
