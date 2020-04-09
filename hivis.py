import numpy as np
import matplotlib.pyplot as plt

q = 2.0
size = 100
x = np.linspace(0,2,num=size)
result = np.zeros(size)
e = 1e-10
for i, typ in enumerate(x):
    out = 0
    k = 0
    while True:
        temp = np.exp(-np.power(q, typ-k)) - np.exp(-np.power(q, typ-k+1))
        if temp < e:
            break
        out += -temp*np.log(temp)
        k += 1
    k = -1
    while True:
        temp = np.exp(-np.power(q, typ-k)) - np.exp(-np.power(q, typ-k+1))
        if temp < e:
            break
        out += -temp*np.log(temp)
        k -= 1
    out1 = out
    out = 0
    k = 0
    while True:
        temp = np.exp(-np.power(q, typ-k)) - np.exp(-np.power(q, typ-k+1))
        temp1 = -np.power(q, typ-k) * np.exp(-np.power(q, typ-k)) +np.power(q, typ-k+1) * np.exp(-np.power(q, typ-k+1))
        if temp < e:
            break
        out += temp1*temp1/temp
        k += 1
    k = -1
    while True:
        temp = np.exp(-np.power(q, typ-k)) - np.exp(-np.power(q, typ-k+1))
        temp1 = -np.power(q, typ-k) * np.exp(-np.power(q, typ-k)) +np.power(q, typ-k+1) * np.exp(-np.power(q, typ-k+1))
        if temp < e:
            break
        out += temp1*temp1/temp
        k -= 1
    result[i] = out1/out

plt.figure()
plt.title('q=2')
plt.plot(x,result)
plt.xlabel(r'$\log_q\lambda$')
plt.ylabel('H/I')
plt.tight_layout()
plt.savefig('hi_q_'+str(q)+'.pdf')



q = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
size = 100
x = np.linspace(0,2,num=size)
result = np.zeros((len(q),size))
e = 1e-15
for j, myq in enumerate(q):
    for i, typ in enumerate(x):
        out = 0
        k = np.floor(typ)
        while True:
            temp = np.exp(-np.power(myq, typ-k)) - np.exp(-np.power(myq, typ-k+1))
            if temp < e:
                break
            out += -temp*np.log(temp)
            k += 1
        k = np.floor(typ)-1
        while True:
            temp = np.exp(-np.power(myq, typ-k)) - np.exp(-np.power(myq, typ-k+1))
            if temp < e:
                break
            out += -temp*np.log(temp)
            k -= 1
        out1 = out
        out = 0
        k = np.floor(typ)
        while True:
            temp = np.exp(-np.power(myq, typ-k)) - np.exp(-np.power(myq, typ-k+1))
            temp1 = -np.power(myq, typ-k) * np.exp(-np.power(myq, typ-k)) +np.power(myq, typ-k+1) * np.exp(-np.power(myq, typ-k+1))
            temp = temp1*temp1/temp
            print(temp)
            if temp < e:
                break
            out += temp
            k += 1
        k = np.floor(typ)-1
        while True:
            temp = np.exp(-np.power(myq, typ-k)) - np.exp(-np.power(myq, typ-k+1))
            temp1 = -np.power(myq, typ-k) * np.exp(-np.power(myq, typ-k)) +np.power(myq, typ-k+1) * np.exp(-np.power(myq, typ-k+1))
            temp = temp1*temp1/temp
            print(temp)
            if temp < e:
                break
            out += temp
            k -= 1
        result[j,i] = out1/out

plt.figure()
plt.title('q=2,4,16')
for j, myq in enumerate(q):
    plt.plot(x,result[j],label='q='+str(q[j]))
plt.xlabel(r'$\log_q\lambda$')
plt.ylabel('H/I')
plt.legend()
plt.tight_layout()
plt.savefig('hi_q_2_4_16.pdf')