#%%
from Classes import Task1a
import time
import matplotlib.pyplot as plt

print("\n")
print("\n")
print("--------------- TASK 1: Tests for different values of p ---------------")
print("\n")
L = 0
while L == 0:
    L = int(input("Enter system size (>0): "))
Gs = 4*L*L
p = [0, 0.2, 0.5, 0.8, 1]
print("\n")
#start timing
start_time = time.time()
tests = []
for i in p:
    test = Task1a(L,Gs,i)
    tests.append(test.___Task1a___())

plt.figure(figsize=(16,10), dpi=120)
j=0
for i in tests:
    Task1a.plot(i,p[j],L)
    j+=1
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task1b
import time
import matplotlib.pyplot as plt

print("\n")
print("\n")
print("--------------- TASK 1: Test the average height for L = 16, 32 ---------------")
print("\n")
#start timing
start_time = time.time()
#Object OsloTest(size,grains,p)
test16 = Task1b(16,32*32 + 50000)
test32 = Task1b(32,32*32 + 50000)
t16 = test16.___Task1b___()
t32 = test32.___Task1b___()
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
print("\n")
print("The average heights are: " + str(t16[0]) + " " + str(t32[0]))
plt.figure(figsize=(16,10), dpi=120)
Task1b.plot(t16[1],16,2*32*32,16*16)
Task1b.plot(t32[1],32,2*32*32,32*32)
#%%
from Classes import Task3a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task1: Test <s>-------------------------")
L = [8,16,32,64,128]
T = 50000
print("\n")
#start timing
start_time = time.time()
for i in L:
    o = Task3a(i,int(((i*i)/2)+T))
    s = o.___Task3a___()
    print("L=" + str(i) + ":  " + str(sum(s)/len(s)) )
    print(i)
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import TaskExtra
import time

print("\n")
print("\n")
print("--------------- TASK 1: Tests ---------------")
print("\n")
L = 0
while L == 0:
    L = int(input("Enter system size (>0): "))
Gs = 200
print("\n")
#start timing
start_time = time.time()
test = TaskExtra(L,Gs,0.5)
print("The number of different configurations visited is " + str(test.___TaskExtra___()))

print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task1a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2a: Height of the pile vs. time for different sizes ------------")
print("\n")
L = [2,4,8,16,32,64,128,256]
p=0.5
#start timing
start_time = time.time()
heights = []
for i in L:
    h = Task1a(i,L[-1]*L[-1] + 10000,p)
    heights.append(h.___Task1a___())

plt.figure(figsize=(16,14), dpi=120)
#x = np.arange(1.,L[-1]*L[-1],0.1)
#plt.plot(x,1.8*np.sqrt(x))
for i in range(len(heights)):
    Task1a.ploth(heights[i],L[i],L[i],False)
#x = np.arange(0.,64*64, 0.01)
#plt.plot(x,1.84*x**(0.5))
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2b
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2b: Cross-over time ------------")
print("\n")
M = int(input("Enter M (= number of different realizations): "))
#p = float(input("Enter p: "))
print("\n")
#start timing
start_time = time.time()
CT = []
L = [2,4,8,16,32,64,128,256]
for i in L:
    o = Task2b(i)
    Sum = 0
    for j in range(M):
        Sum = Sum + o.__Task2b__()
    CT.append(Sum/M)
CT = np.array(CT)
L = np.array(L)
x = np.arange(0.,L[-1], 0.1)
c = np.polyfit(L[2:], CT[2:], 2)
print("Best fit : " + str(c))
print("Points: " + str(CT))
Task2b.plot(L,CT)
plt.plot(x, c[0]*x**2 + c[1]*x + c[2], color='r')
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2b
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2b: Cross-over time (Linear)------------")
print("\n")
M = int(input("Enter M (= number of different realizations): "))
#p = float(input("Enter p: "))
print("\n")
#start timing
start_time = time.time()
CT = []
L = [16,32,64,128,256]
for i in L:
    o = Task2b(i)
    Sum = 0
    for j in range(M):
        Sum = Sum + o.__Task2b__()
    CT.append(Sum/M)
CT = np.array(CT)
L = np.array(L)
x = np.arange(0.,L[-1]**2, 0.1)
c = np.polyfit(L**2, CT, 1)
print("Best fit coefficients: " + str(c))
print("Points: " + str(CT))
Task2b.plot(L**2,CT)
plt.plot(x, c[0]*x + c[1], color='r')
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2c
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2c: Average height <h(L)> fit ------------")
print("\n")
L = [2,4,8,16,32,64,128,256]
T = 50000
#p = float(input("Enter p: "))
print("\n")
#start timing
start_time = time.time()
h = []
for k in L:
    print(k)
    o = Task2c(k,k*k + T)
    h.append(o.___Task2c___())
x = np.arange(0.,L[-1], 0.1)
c = np.polyfit(L[4:], h[4:], 1)
plt.figure(figsize=(16,10), dpi=120)
Task2c.plot(L,h)
plt.plot(x, c[0]*x + c[1], color='r')
print("Best fit coefficients: " + str(c))
print("\n")
print(h)
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2d
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2d: Data collapse of h(t;L) ------------")
print("\n")
L = [4,8,16,32,64,128,256]
M = int(input("Enter M (= number of different realizations): "))
#p = float(input("Enter p: "))
#steps = int(input("Enter time steps: "))
print("\n")
T=20000
#start timing
start_time = time.time()
plt.figure(figsize=(16,10), dpi=120)
#average slopes for different system sizes in steady state
#c = [1.53157445, 1.57834862, 1.62152393, 1.65986925, 1.68305689, 1.70482295]
for k in range(len(L)):
    o = Task2d(L[k],L[k]*L[k]+T)
    havas= np.array([o.___Task2d___()])
    for j in range(M-1):
        print(L[k])
        print(j)
        havas = havas + o.___Task2d___()
    Task2d.plot(havas[0]/M,L[k]*L[k]+T,L[k],1)
    havas = np.array([0])

#x = np.arange(0.,1.5, 0.01)
#plt.plot(x,1.6*x**(0.5))
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2c
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2e: Correction to scaling for <h(L)> FIT------------")
print("\n")
L = [4,8,16,32,64,128,256]
T = 50000
#p = float(input("Enter p: "))
print("\n")
#start timing
start_time = time.time()
h = np.array([])
for k in L:
    o = Task2c(k,k*k + T)
    h=np.append(h,np.log(-o.___Task2c___()/(1.73*k)+1))

x = np.arange(0.,L[-1], 0.1)
c = np.polyfit(np.log(L), h, 1)
plt.figure(figsize=(16,10), dpi=120)
Task2c.plot(np.log(L),h)
plt.plot(x, c[0]*x + c[1], color='r')
print("Best fit coefficients: " + str(c))
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2c
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

print("\n")
print("\n")
print("------------ TASK 2e: Correction to scaling for <h(L)> FIT1------------")
print("\n")
L = [16,32,64,128,256]
T = 10000
#p = float(input("Enter p: "))
print("\n")
#start timing
start_time = time.time()
h = np.array([])
for k in L:
    o = Task2c(k,k*k + T)
    h=np.append(h,o.___Task2c___())

def func(x, a, b, c):
    return a*(1-b*x**(-c))


xdata = np.linspace(2, 130, 1000)
c1,c2 = curve_fit(func, L, h/L, [1.6, 0.1, 0.5])

print(c1)
print("\n")

plt.figure(figsize=(16,10), dpi=120)
#Task2c.plot(np.log(L),h)
#print(c)
Task2c.plot(L,h/L)
plt.plot(xdata, func(xdata, *c1), color='r')

#print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2f
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2f: sigma ------------")
print("\n")
L =[2,4,8,16,32,64]
T = 50000
sigma = []
#start timing
start_time = time.time()
for i in L:
    o = Task2f(i,int((i*i)/2) + T)
    sigma.append(o.___Task2f___())
plt.figure(figsize=(16,10), dpi=120)
Task2f.plot(L,sigma)
print(sigma)
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task2f
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("------------ TASK 2f: sigma FIT------------")
print("\n")
L =[2,4,8,16,32,64,128,256]
T = 50000
sigma = []
#start timing
start_time = time.time()
for i in L:
    o = Task2f(i,int((i*i)/2) + T)
    sigma.append(o.___Task2f___())

sigma = np.array(sigma)
x = np.arange(0.,L[-1], 0.1)
c = np.polyfit(np.log(L), np.log(sigma), 1)
plt.figure(figsize=(16,10), dpi=120)
Task2c.plot(np.log(L),np.log(sigma))
plt.plot(x, c[0]*x + c[1], color='r')
print("Best fit coefficients: " + str(c))
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
print("\n")
print("\n")
print("--------------- TASK 2g: P(h;L), theoretically ---------------")
print("\n")

from Classes import Task3a
from Classes import Task2g
import matplotlib.pyplot as plt
import numpy as np
import random as rd

L=40

def Ph(h,L):
    allk = [(i,j) for i in range(L+1) for j in range(L+1)]
    res = [item for item in allk if (item[0] + 2*item[1]) == h]
    res1 = [item for item in res if (item[0] + item[1])<41]
    
    Sum=0
    for i in res1:
        Sum = Sum + Task2g.Pkk(i[0],i[1],L) 
    return Sum

i = range((2*L)+1)
ph = []
for j in i:
    ph.append(Ph(j,L))

plt.figure(figsize=(16,10), dpi=120)
#plt.plot(i,ph, label="Expected")

M=50000
L=40
h = []
for k in range(M):
    z = 0
    for i in range(L):
        z=z+np.random.choice([2,1,0], p=[1/2,1/3,1/6])
    h.append(z)

p = Task3a.logbin(h,1.)
#plt.figure(figsize=(16,10), dpi=120)
Task3a.plot(p[0],p[1],L)
print(p[0])
#%%
from Classes import Task2g
from Classes import Task3a
import matplotlib.pyplot as plt
import numpy as np
print("\n")
print("\n")
print("--------------- TASK 2g: P(h;L), Data collapse ---------------")
print("\n")
L=[8,16,32,64,128,256]
T=50000
#Measured data
h = [3.0592611852237046, 6.307066141322826, 12.979519590391808, 26.52637052741055, 53.95781915638313, 108.91893837876758, 219.1730234604692, 440.484929698594]
sigma = [0.6570759610425904, 0.8020202089718995, 0.9587437079909461, 1.1311309247717418, 1.3404669370579914, 1.5727998229214804, 1.8431191259833608, 2.1878004024383597]
plt.figure(figsize=(16,10), dpi=120)
for i in range(len(L)):
    print(L[i])
    o = Task2g(L[i],L[i]*L[i] + T)
    p = Task3a.logbin(o.___Task2g___(),1.)
    #Task3a.plot(p[0],p[1],L[i],h[i],sigma[i])
    Task3a.plot(p[0],p[1],L[i])
#%%
from Classes import TaskX
import time
import matplotlib.pyplot as plt
import numpy as np
print("\n")
print("\n")
print("------------ TASK X: average slope ------------")
print("\n")
L = [1]
T = 50000
z = np.array([])
z2 = np.array([])
#start timing
start_time = time.time()
for k in L:
    o = TaskX(k,int((k*k)/2) + T)
    a = o.___TaskX___()
    z = np.append(z, np.mean(a[0]))
    z2 = np.append(z2, np.mean(a[1]))
    print(k)

sigma = np.array(np.sqrt(z2-z**2))

TaskX.plot(L,sigma)
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task3a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task3a: P(s;L)-------------------------")
L = [4,8,16,32,64,128,256,512]
T = 100000
print("\n")
#start timing
start_time = time.time()
s = []
for i in L:
    o = Task3a(i,int(((i*i)/2)+T))
    s.append(Task3a.logbin(o.___Task3a___(),1.2,False))
    print(i)
plt.figure(figsize=(16,10), dpi=120)
for j in s:    
    Task3a.plot(j[0],j[1],L[s.index(j)])
#[s.index(j)]
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task3a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task3b: data collapse-------------------------")
L = [4,8,16,32,64,128,256,512]
T = 100000

print("\n")
#start timing
start_time = time.time()
s = []
for i in L:
    o = Task3a(i,int((i*i)/2+T))
    s.append(Task3a.logbin(o.___Task3a___(),1.2,False))
    print(i)

tau = 1.3
D = 2.25
plt.figure(figsize=(16,10), dpi=120)
for j in s:    
    Task3a.plotc(j[0],j[1],L[s.index(j)],tau,D)

tau = 1.55
D = 2.25
plt.figure(figsize=(16,10), dpi=120)
for j in s:    
    Task3a.plotc(j[0],j[1],L[s.index(j)],tau,D)

tau = 1.55
D = 2.5
plt.figure(figsize=(16,10), dpi=120)  
for j in s:    
    Task3a.plotc(j[0],j[1],L[s.index(j)],tau,D)


print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task3a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task3c: kth moment-------------------------")
L = [2,4,8,16,32,64,128]
T = 10000
print("\n")
#start timing
start_time = time.time()
s = []
for i in L:
    o = Task3a(i,(i*i)+T)
    s.append(o.___Task3a___())

mom = []
for k in range(1,10):
    a = []
    for i in range(len(L)):
        a.append(Task3a.momentum(s[i],k))
    mom.append(a)
plt.figure(figsize=(16,10), dpi=120)
for i in mom:
    Task3a.plotk(L,i)
    x = np.arange(0.,L[-1], 0.1)
    c = np.polyfit(np.log(L[3:]), np.log(i[3:]), 1)
    print("Best fit k=" + str(mom.index(i)+1) + " " + str(c))
    plt.plot(x, c[0]*x + c[1])
    c = np.array([])

print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
from Classes import Task3a
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task3c: D and Tau -------------------------")
c = [0.1, 3.17, 5.37, 7.56, 9.74, 11.92, 14.01, 16.24, 18.39]
k = [1,2,3,4,5,6,7,8,9]
plt.figure(figsize=(16,10), dpi=120)
x = np.arange(0.,10., 0.1)
fit = np.polyfit(k,c,1)
print("Best fit " + str(fit))
Task3a.plotk(k,c)
plt.plot(x, fit[0]*x + fit[1], color ='r')
#%%
from Classes import Task3a
import time
import matplotlib.pyplot as plt
import numpy as np

print("\n")
print("\n")
print("-------------------------Task3c: kth moment correction to scaling-------------------------")
L = [2,4,8,16,32,64,128,256,512]
T = 10000
print("\n")
#start timing
start_time = time.time()
s = []

for i in L:
    o = Task3a(i,(i*i)+T)
    s.append(o.___Task3a___())

mom = []
for k in range(1,6):
    a = []
    for i in range(len(L)):
        a.append(Task3a.momentum(s[i],k))
    mom.append(a)
    

plt.figure(figsize=(16,10), dpi=120)
for i in mom:
    Task3a.plotkCorrections(L,i,mom.index(i))
#    x = np.arange(0.,L[-1], 0.1)
#    c = np.polyfit(np.log(L[3:]), np.log(i[3:]), 1)
#    print("Best fit k=" + str(mom.index(i)+1) + " " + str(c))
#    plt.plot(x, c[0]*x + c[1])
#    c = np.array([])

print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
print("\n")
print("\n")
print("--------------- Average z ---------------")
print("\n")

from Classes import Zave
import matplotlib.pyplot as plt
import numpy as np

L = [8,16,32,64]

plt.figure(figsize=(16,10), dpi=120)
for j in L:
    o = Zave(j,20000)
    i = range(1,j+1)
    Zave.plot(i,o.___Zave___()**(2),j)
    plt.show()
