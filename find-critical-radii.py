import scipy as sp
from parameters import modes, tfEDO
from functions import lamb

def findCriticalTime(x, tf):
    tcArr = []
    for mode in x:
        if(lamb(mode, 0) >= 0):
            tcArr.append(0)
        else:
            def lamb_n(t):
                return lamb(mode, t)
            tc = sp.optimize.root_scalar(lamb_n,x0=0,bracket=[0,tf/2], method="bisect")
            tcArr.append(tc.root)
    return tcArr

# print(lamb(7, 0))
print(findCriticalTime(modes, tfEDO))

# t=np.arange(tc.root-tc.root/2,tc.root+tc.root/2,tc.root/50)

# fig, ax = plt.subplots()
# ax.plot(t, lamb_n(t))

# ax.set(xlabel='t', ylabel='Growth Rate',
#         title=f'Growth rate for mode {modes[1]}')
# ax.grid()

# fig.savefig(f'./{modes[1]}/test_growthrate_{modes[1]}.png')
# plt.show()