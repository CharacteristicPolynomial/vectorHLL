import numpy as np
import matplotlib.pyplot as plt

m = 128
experi_n = 5000
step_n = 30
period_n = 2
total_step = step_n*period_n
q = 2
loglamb = np.linspace(0,period_n, total_step)
lamb = np.power(q, loglamb)
result = np.zeros((total_step, experi_n))

for n,scale in enumerate(lamb):
    for i in range(experi_n):
        sketch = np.random.exponential(1/scale, size=(m))
        logsketch = np.ceil(-np.log(sketch)/np.log(q))
        esti = m/np.sum(np.power(q,-logsketch))
        result[n,i] = esti/scale

# avg = np.mean(result,axis=1)
# result = result/avg[:,None]
avg = np.mean(result)
result = result/avg


plt.figure()
plt.rcParams.update({'font.size': 15})
for n,scale in enumerate(loglamb):
    plt.scatter(np.ones(experi_n)*scale, result[n], color='black', s=0.1)

plt.title('q='+str(q)+' without offsets')
plt.xlabel(r'$\log_q\lambda$')
plt.ylabel('relative error')
plt.ylim([0,2.5])

plt.tight_layout()
plt.savefig('q_'+str(q)+'.jpg')