#chatgpt example
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from functions import lamb, W0
from parameters import R0, R

tfEDO = 3000

# Função que define o sistema de EDOs
def system(amp, t):
    da7_dt = lamb(7,t)*amp[0] +(1/2)*W0(7, 14, t)*amp[0]*amp[1] 
    da14_dt =  lamb(14,t)*amp[1] +(1/2)*W0(14, 7, t)*amp[0]**2
    return [da7_dt, da14_dt]

# Condições iniciais
amp0 = [R0/2500, 0]

# Intervalo de tempo
t_span = np.linspace(0, tfEDO,tfEDO)

# Resolvendo o sistema de EDOs
sol = odeint(system, amp0, t_span)# solve_ivp(system, t_span, amp0)

An = sol[:,0]
A2n = sol[:,1]

print(An)
print(R(tfEDO))

# Plotando os resultados


plt.plot(t_span, An, label='a_{n}')
plt.plot(t_span, A2n, label='a_{2n}')
plt.xlabel('Tempo')
plt.ylabel('Amplitudes')
plt.legend()
plt.grid(True)
plt.show()


