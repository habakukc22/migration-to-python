import numpy as np
from parameters import modes, tfEDO
from functions import lamb

# https://mpmath.org/doc/current/calculus/optimization.html?highlight=roots

# This function was tested for findMaxRadius(14, 0, 3000, 10e-5)

def findMaxRadius(n,ti, tf, err):
    """
    Find the maximmum radius for the mode n given the interval [ti,tf] to search in
    
    Paramenters:
        n - is the mode
        
        ti - initial time
        
        tf - final time
        
        err - minimum accepted error
    """
    t0N = ti
    tfN = tf
    tm=(tf-ti)/2
    print(lamb(n, ti), lamb(n, tm), lamb(n, tf))
    
    while(err < (tfN-t0N)/2):
        for t in [t0N, tm, tfN]:
            # print(f'lambda({n}, {t}) = {lamb(n,t)}')
            if(lamb(n, t)>0):
                tfN=min(t,tfN)
                # print(f'tfN ={tfN}')            
            if(lamb(n, t)<0):
                t0N=max(t,t0N)
            tm=(tfN+t0N)/2
                
        # print(t0N,tm,tfN)
    
    return (tfN+t0N)/2

tc = findMaxRadius(modes[1], 0, tfEDO, 10e-5)

print(tc)
print(lamb(modes[1],tc))
