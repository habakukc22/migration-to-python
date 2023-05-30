import numpy as np
from scipy.integrate import odeint
from parameters import modesTotal
from functions import BO, W0, lamb

def SecOrderA(y, t):
       return sum(((1/2)*BO(y-p)*(W0(y, p, t)*a(p,t)*a(abs(y-p),t)
            -W0(y, p, t)*b(p,t)*(np.sign(y-p))*b(abs(y-p),t))
            +(1/2)*BO(y+p)*(W0(y, -p, t)*a(p,t)*a(abs(y+p),t)
            +W0(y, -p, t)*b(p,t)*b(abs(y+p),t))) for p in modesTotal)
            
result =  sum((p) for p in modesTotal)
print(modesTotal)



def odes(x,t):
    an = x[0]
    bn = x[0]
    a2n = x[1]
    b2n = x[1]
    
    dan_dt = lamb(modesTotal[0],t)*an
    dbn_dt = lamb(modesTotal[0],t)*an
    da2n_dt = lamb(modesTotal[1],t)*an
    db2n_dt = lamb(modesTotal[1],t)*an
    
    