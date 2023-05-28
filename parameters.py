import numpy as np

fund = 7;
modes = [fund*1, fund*2] # Modos de Fourier a serem usados    
R0 = 3 # Raio Inicial
amp1 = R0/2500 # Amplitude dos modos
amp2 = 0
A = 1 #(* Contraste de viscosidade \
Ca = 150. # Número de Capilaridade 12\[Eta]2Q/(\[Sigma]b)
order = 2 # Ordem da simulação [1,2,3] *)
delta = 1 # \[Delta]=1: Com estresses normais; \[Delta]=0: Sem estresses \
epsilon =   1. # epsilon = 1 então inclui reologia, se epsilon = 0 exclui
Bq = 0. # Subscript[\[Eta], s]/(Subscript[\[Eta], 2]b)*)
tTipico = 2600
tfEDO = 3000

def R(t):
  return np.sqrt(R0**2. + t/(np.pi)) # Raio não pertubado

# print(R(0))