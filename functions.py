import numpy as np
from parameters import A, delta, R, epsilon, Bq, Ca, modesTotal

def s(y, t):
    return 1 + delta/(6*R(t)**2)*abs(y)*(abs(y) + A) + epsilon*Bq*abs(y)*(A + 1)/(24*R(t)**3)

# tested with print(s(1,0))

def lamb(y,t): #Growth Rate
    return (1. / s(y,t)) * (((1 / (2 * np.pi * R(t)**2)) * (A * abs(y) - 1)) - (((A + 1) / (2 * Ca * R(t)**3)) * abs(y) * (y ** 2 - 1)) - (delta * (1 / (12 * np.pi * R(t)**4)) * abs(y) * (abs(y) - A)) - (epsilon * ((Bq * (A + 1)) / (48 * np.pi * R(t) ** 5)) * abs(y) * (y ** 2 - 2)))

#tested with print(lamb(2, 1))

def F(y,p,t):
    return (abs(y) / (s(y,t) * R(t))) * (A * (1 / (2 * np.pi * R(t) ** 2)) * (1 / 2 - np.sign(y * p)) - ((A + 1) / (2 * Ca * (R(t)) ** 3)) * (1 - (p / 2) * (3 * p + y))) + delta * (abs(y) / (12 * np.pi * (R(t)) ** 5 * s(y, t))) * (abs(p) + y * np.sign(p) - A * (y * abs(y) * np.sign(p) - p ** 2 + 1)) - epsilon * ((Bq * (A + 1)) / (48 * np.pi * (R(t)) ** 6 * s(y, t))) * abs(y) * (3 + y ** 2 * (1 + np.sign(y * p)) - 7 / 2 * p ** 2 - 5 / 2 * y * p)

# tested with print(F(2,3,1))

def G(y, p, t):
    return (abs(y) * (1 - np.sign(p * y)) - 1) / (s(y, t) * R(t)) + delta * (abs(y) / (6 * (R(t)) ** 3 * s(y, t))) * (abs(p) - abs(y) + y * np.sign(p) - A * (y * abs(y) * np.sign(p) - 2 * y * p + p ** 2 - 1)) - epsilon * ((Bq * (A + 1)) / (24 * (R(t)) ** 4 * s(y, t))) * abs(y) * (y ** 2 * (1 + np.sign(y * p)) - 2 + 2 * p ** 2 - 4 * y * p)

# Tested with print. We Expect the value G(2,3,1) = -0.264094 and that's we got by using print(G(2,3,1))

def W0(i,j,t):
    return F(i,j,t)+lamb(j, t)*G(i, j, t)

# tested with print(W0(7, 7, 3))

def BO(x):
    return int(any(x == item for item in modesTotal))
