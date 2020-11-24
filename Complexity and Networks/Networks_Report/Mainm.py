#%%
#Prefeential Attachment
import random as rd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from Classes import Funcs
import scipy as sp
print("------------- Preferential Attachment: degree distribution ---------------")
#Parameters
Nmax = 1000
m = 2
#Initial graph
Nb=Funcs.Initial_graph(m)[0]
a=Funcs.Initial_graph(m)[1]
#Funcs.plotG(Nb)
for v in range(len(Nb),Nmax,1):
    t=[]
    for j in range(m):
        check = True
        while(check):
            i=rd.randint(0,len(a)-1)
            if a[i] not in t:
                t.append(a[i])
                check = False    
    Nb.append(t)           
    for q in t:
        Nb[q].append(v)
        a.append(v)
        a.append(q)
k = []
for i in Nb:
    k.append(len(i))
print(sum(k)/len(k))

#sizes = np.array(k)
#Funcs.plotG(Nb,sizes*70)

#Find zero values in the distribution
BINCOUNT = np.bincount(k)[m:]
kc=0
while(BINCOUNT[kc]>0):
    kc = kc + 1
print("kc = " + str(kc))
#Zipf
Zipf_deg = np.sort(k)[::-1]
Zipf_rank = np.arange(1,len(Zipf_deg)+1)
plt.figure()
Funcs.Zipf_plot(Zipf_rank,Zipf_deg)
#plot log binned and non-log binned
x = Funcs.logbin(k,1.)[0]
y = Funcs.logbin(k,1.)[1]
xbin = Funcs.logbin(k,1.2)[0]
ybin = Funcs.logbin(k,1.2)[1]
plt.figure()
Funcs.plotLOGBIN(x,y,xbin,ybin)
#CDF
pCDF=[]
for i in range(len(y)+1):
    pCDF.append(sum(y[0:i]))
pCDF=pCDF[1:]
plt.figure()
Funcs.plotCDF(x,pCDF)
plt.show()
#Adjacency matrix for random walk
#Funcs.plotG(Nb)
#
#E = []
#index = 0
#for e in Nb:
#    for ee in e:
#        E.append([index,ee])
#    index += 1
#G = nx.Graph()
#G.add_edges_from(E)
#
#A=nx.adjacency_matrix(G)
#X = np.array(A.todense())
#print(X@X)
#print(k)
#print("-------v=" + str(v) + "-------")
#print("S: " + str(S))
#print("Nb: " + str(Nb))
#print("a: " + str(a))
#Testing recursive formula
#kmax = 1000
#n = [2/3]
#k = range(1,kmax+1)
#for i in range(2,kmax+1):
#    n.append(((i-1)/(i+2))*n[-1])
#Boundary
print(y[0])
plt.figure()
k=np.arange(m,max(x))
Funcs.plot(x,y,k,(2*m*(m+1))/(k*(k+1)*(k+2)))
#%%
#Preferential Attachment: statistical analysis
import time
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
from scipy.stats import chisquare
from scipy.stats import kstest
from scipy.stats import ks_2samp
from random import choices
import statistics
print("--------------Preferential Attachment: statistical analysis ---------------")
#Parameters
m = 3
#Number of realizations
M = 10
N = 100000
K = []
BC=[]
#start timing
start_time = time.time()
perc = 1
for n in range(M):
    if perc % 2==0:
        print((perc/M)*100)
    perc+=1   
    #Initial graph
    Nb=Funcs.Initial_graph(m)[0]
    a=Funcs.Initial_graph(m)[1] 
    for v in range(len(Nb),N,1):       
        t=[]
        for j in range(m):
            check = True
            while(check):
                i=rd.randint(0,len(a)-1)
                if a[i] not in t:
                    t.append(a[i])
                    check = False       
        Nb.append(t)           
        for q in t:
            Nb[q].append(v)
            a.append(v)
            a.append(q)
    k = []
    for i in Nb:
        k.append(len(i))
    K.extend(k)
#    #Change to logbiN for chi squared!!!
#    x = Funcs.logbin(K,1.)[0]
#    y = Funcs.logbin(K,1.)[1]
#    #xbin = Funcs.logbin(K,1.1)[0]
#    #ybin = Funcs.logbin(K,1.1)[1]
#    BC.append(y[0])

#Test for Boundary values
#print(sum(BC)/len(BC))
#print(statistics.stdev(BC)/np.sqrt(M))

#CHISquared------Change to logbiN!!!
i = 0
while y[i]>=5:
    i=i+1
k=np.arange(m,x[i])
ntest = (N*2*m*(m+1))/(k*(k+1)*(k+2))
print(chisquare(y[0:i]/M, ntest, ddof=0))
#plt.figure()
Funcs.plot(x[0:i],y[0:i]/M,k,(N*2*m*(m+1))/(k*(k+1)*(k+2)),m)
#CHISquared---------
#KS------------
cutoff_degree = x[-1]
k = np.arange(m,cutoff_degree + 1)
weights = (2*m*(m+1))/(k*(k+1)*(k+2))
weights = np.append(weights, 1-sum(weights))
k = np.append(k,k[-1]+1)
Kteo = []
Nsample = N
for i in range(Nsample):
    Kteo.extend(choices(k,weights))
print(ks_2samp(K,Kteo))
#KS------------
#KSTest-----------
#def ntestKS(k):
#    CDF=0
#    for i in range(m, k+1):
#        CDF = CDF + (2*m*(m+1))/(i*(i+1)*(i+2))
#    return CDF
#
#print(kstest(pCDF,ntestKS))
print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
#Preferential Attachment: Data collapse
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
import time
print("--------------Preferential Attachment: Data collapse ---------------")
#Parameters
m = 2
#Number of realizations
M = 100
N= 100
K = []
#start timing
start_time = time.time()
perc = 1
for n in range(M):
    if perc % 2==0:
        print((perc/M)*100)
    perc+=1
    #Initial graph
    Nb=Funcs.Initial_graph(m)[0]
    a=Funcs.Initial_graph(m)[1]
    for v in range(len(Nb),N,1):       
        t=[]
        for j in range(m):
            check = True
            while(check):
                i=rd.randint(0,len(a)-1)
                if a[i] not in t:
                    t.append(a[i])
                    check = False
        Nb.append(t)           
        for q in t:
            Nb[q].append(v)
            a.append(v)
            a.append(q)
    k = []
    for i in Nb:
        k.append(len(i))
    K.extend(k)
x = Funcs.logbin(K,1.)[0]
y = Funcs.logbin(K,1.)[1]
xbin = Funcs.logbin(K,1.1)[0]
ybin = Funcs.logbin(K,1.1)[1]
#k=np.arange(m,max(xbin)+1,1)
#Funcs.plot(xbin,ybin,k,(2*m*(m+1))/(k*(k+1)*(k+2)),m)
#Funcs.plotDC(xbin,ybin,N)
#plt.figure()
#p_inf=(2*m*(m+1))/(xbin*(xbin+1)*(xbin+2))
#k1=(m*(m+1)*N)**(0.5)
#Funcs.plotDC(xbin/k1,ybin/p_inf,N)
#plt.figure()
Funcs.plotDC(xbin,ybin,N)
#%%
#Preferential Attachment: largest degree
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
print("--------------Preferential Attachment: largest degree ---------------")
#Funcs.plotG(Nb)
#Parameters
m = 2
#Average over
M = 100
#Values of N
NN = [100,1000,10000,100000,1000000]
kave = np.array([0]*len(NN))
s = np.array([0]*len(NN))
sq = np.array([0]*len(NN))
for n in range(M):    
    print(str((n/M)*100) + "%")    
    kmax = np.array([])
    for nn in NN:        
        #Initial graph
        Nb=Funcs.Initial_graph(m)[0]
        a=Funcs.Initial_graph(m)[1]        
        for v in range(len(Nb),nn,1):                        
            t=[]
            for j in range(m):
                check = True
                while(check):
                    i=rd.randint(0,len(a)-1)
                    if a[i] not in t:
                        t.append(a[i])
                        check = False            
            Nb.append(t)        
            for q in t:
                Nb[q].append(v)
                a.append(v)
                a.append(q)   
        k = []
        for i in Nb:
            k.append(len(i))       
        kmax = np.append(kmax, max(k))
    kave = kave + (kmax/M)
    s = s + kmax
    sq = sq + kmax**(2)
std = np.sqrt((sq/M) - (s/M)**(2))
c = np.polyfit(np.log10(NN),np.log10(kave), 1, cov=True)
print("Best fit coefficients: " + str(c))
print(kave)
plt.figure()
Funcs.plotLargest(NN,kave,m,std/(M**(1/2)),c)
err = std/(kave*(M**(1/2)))

print("x")
print(c[0]*np.log10(NN) + c[1])
print("y")
print(np.log10(kave))
print("errors")
print(err)

chi2 = 0
for i in range(len(kave)):
    chi2 = chi2 + ((np.log10(kave[i])-(c[0]*np.log10(NN[i]) + c[1]))**(2))/((err[i])**(2))
    print(chi2)
print(chi2)
#%%
#Preferential Attachment: single node growth
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
print("--------------Preferential Attachment: single node growth ---------------")
#Parameters
Nmax = 100000
m = 2
#Initial graph
Nb=Funcs.Initial_graph(m)[0]
a=Funcs.Initial_graph(m)[1]
#Funcs.plotG(Nb)
indexNodes = [0,9,99,999,9999]
Nodes = [[],[],[],[],[],[]]
for v in range(len(Nb),Nmax,1):    
    t=[]
    for j in range(m):
        check = True
        while(check):
            i=rd.randint(0,len(a)-1)
            if a[i] not in t:
                t.append(a[i])
                check = False    
    Nb.append(t)
    for q in t:
        Nb[q].append(v)
        a.append(v)
        a.append(q)    
    for i in range(len(indexNodes)):
        if v > indexNodes[i]:
            Nodes[i].append(len(Nb[indexNodes[i]]))
plt.figure()
Funcs.plotkTeo(len(Nodes[0]),m)
for i in range(len(indexNodes)):
    Funcs.plotk(Nodes[i],indexNodes[i]+1)
#%%
#Random attachment
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
import time
from scipy.stats import chisquare
from scipy.stats import kstest
from scipy.stats import ks_2samp
from random import choices
import statistics
print("--------------Random Attachment: degree distribution and statistical analysis---------------")
#Parameters
Nmax=100000
m=1
M=10
K=[]
BV = []
#start timing
start_time = time.time()
perc = 1
for n in range(M):
    if perc % 2==0:
        print((perc/M)*100)
    perc+=1
    #Initial graph
    Nb=Funcs.Initial_graph(m)[0]
    a = [_ for _ in range(len(Nb))]
    for v in range(len(Nb),Nmax,1):
        t=[]
        for j in range(m):
            check = True
            while(check):
                i=rd.randint(0,len(a)-1)
                if a[i] not in t:
                    t.append(a[i])
                    check = False
        Nb.append(t)
        for q in t:
            Nb[q].append(v)
        a.append(v)
    k = []
    for i in Nb:
        k.append(len(i))
    K.extend(k)
#    x = Funcs.logbin(K,1.)[0]
#    y = Funcs.logbin(K,1.)[1]
#    BV.append(y[0])

#print(sum(BV)/len(BV))
#print(statistics.stdev(BV)/np.sqrt(M))

#sizes = np.array(k)
#Funcs.plotG(Nb,sizes*70)

x = Funcs.logbiN(K,1.)[0]
y = Funcs.logbiN(K,1.)[1]
xbin = Funcs.logbiN(K,1.)[0]
ybin = Funcs.logbiN(K,1.)[1]
#plt.figure()
#k=np.arange(m, max(x)+1)
#Funcs.plotRandom(xbin, ybin, k, (Nmax*M*(m/(1+m))**(k-m))*(1/(1+m)), m)
#Funcs.plotRandomDC(xbin,ybin,Nmax)

#chisquared-test
i = 0
while y[i]>=5:
    i=i+1
k=np.arange(m,x[i])
ntest = (Nmax*(m/(1+m))**(k-m))*(1/(1+m))
print(chisquare(y[0:i]/M, ntest, ddof=0))
#plt.figure()
Funcs.plot(x[0:i],y[0:i]/M,k,(Nmax*(m/(1+m))**(k-m))*(1/(1+m)),m)
#chisquared-test

#KS------------
cutoff_degree = x[-1]
k = np.arange(m,cutoff_degree + 1)
weights = ((m/(1+m))**(k-m))*(1/(1+m))
weights = np.append(weights, 1-sum(weights))
k = np.append(k,k[-1]+1)
Kteo = []
Nsample = N
for i in range(Nsample):
    Kteo.extend(choices(k,weights))
print(ks_2samp(K,Kteo))
#KS------------

print("\n")
print("The time of execution is %s seconds" % (time.time() - start_time))
#%%
#Random Attachment: largest degree
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
print("--------------Random Attachment: largest degree ---------------")
#Funcs.plotG(Nb)
#Parameters
m = 2
#Average over
M = 100
#Values of N
NN = [100, 1000, 10000, 100000, 1000000]
kave = np.array([0]*len(NN))
s = np.array([0]*len(NN))
sq = np.array([0]*len(NN))
for n in range(M):    
    print(str((n/M)*100) + "%")    
    kmax = np.array([])
    for nn in NN:        
        #Initial graph
        Nb=Funcs.Initial_graph(m)[0]
        a = [_ for _ in range(len(Nb))]       
        for v in range(len(Nb),nn,1):            
            t=[]
            for j in range(m):
                check = True
                while(check):
                    i=rd.randint(0,len(a)-1)
                    if a[i] not in t:
                        t.append(a[i])
                        check = False            
            Nb.append(t)           
            for q in t:
                Nb[q].append(v)        
            a.append(v)        
        k = []
        for i in Nb:
            k.append(len(i))            
        kmax = np.append(kmax, max(k))
    kave = kave + (kmax/M)
    s = s + kmax
    sq = sq + kmax**(2)
std = np.sqrt((sq/M) - (s/M)**(2))
print(kave)
c,V = np.polyfit(np.log(NN),kave, 1, cov=True)
print(c)
plt.figure()
Funcs.plotLargestRA(NN,kave,m,std/(M**(1/2)),c)

err=std/(M**(1/2))
chi2 = 0
for i in range(len(kave)):
    chi2 = chi2 + ((kave[i]-(c[0]*np.log(NN[i]) + c[1]))**(2))/((err[i])**(2))
    print(chi2)
print(chi2)
#%%
#Random attachment
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
import time
from scipy.stats import chisquare
from scipy.stats import kstest
from scipy.stats import ks_2samp
from random import choices
print("--------------Random Attachment: data collapse---------------")
#Parameters
Nmax=1000000
m=3
M=10
K=[]
#start timing
start_time = time.time()
perc = 1
for n in range(M):
    if perc % 2==0:
        print((perc/M)*100)
    perc+=1
    #Initial graph
    Nb=Funcs.Initial_graph(m)[0]
    a = [_ for _ in range(len(Nb))]
    for v in range(len(Nb),Nmax,1):    
        t=[]
        for j in range(m):
            check = True
            while(check):
                i=rd.randint(0,len(a)-1)
                if a[i] not in t:
                    t.append(a[i])
                    check = False
        Nb.append(t)
        for q in t:
            Nb[q].append(v)
        a.append(v)
    k = []
    for i in Nb:
        k.append(len(i))
    K.extend(k)
x = Funcs.logbin(K,1.)[0]
y = Funcs.logbin(K,1.)[1]
xbin = Funcs.logbin(K,1.)[0]
ybin = Funcs.logbin(K,1.)[1]

p_inf = ((m/(1+m))**(xbin-m))*(1/(1+m))
k1= (np.log(Nmax)/np.log((m+1)/(m))) + m
#plt.figure()
Funcs.plotDC(xbin/k1,ybin/p_inf,Nmax)


#%%
#Random Walk and Preferential Attachment
import random as rd
import matplotlib.pyplot as plt
import numpy as np
from Classes import Funcs
print("--------------Random Walk and Preferential Attachment---------------")
#Funcs.plotG(Nb)
#Parameters
Nmax = 100000
m = 3
q = 0.9695
M=1
K=[]
#Initial graph
Nb=Funcs.Initial_graph(m)[0]
for _ in range(M):
    print(_)
    for s in range(len(Nb),Nmax,1):
        t=[]
        while(len(t)<m):    
            #Random walk
            v = rd.randint(0,len(Nb)-1)
            while(rd.random()<q):
                ii = rd.randint(0,len(Nb[v])-1)
                v = Nb[v][ii]
            if v not in t:
                t.append(v)
        Nb.append(t)
        for vL in t:
            Nb[vL].append(s)
    k = []
    for i in Nb:
        k.append(len(i))
K.extend(k)
#print(Nb)
#Funcs.plotG(Nb)
x = Funcs.logbin(k,1.)[0]
y = Funcs.logbin(k,1.)[1]
xbin = Funcs.logbin(K,1.2)[0]
ybin = Funcs.logbin(K,1.2)[1]
plt.figure()
k=np.arange(m,max(x)+1)
#Funcs.plotRandom(xbin,ybin,k,((m/(1+m))**(k-m))*(1/(1+m)),q)
Funcs.plotRandom(xbin,ybin,k,(2*m*(m+1))/(k*(k+1)*(k+2)),q)
#KS------------
cutoff_degree = x[-1]
k = np.arange(m,cutoff_degree + 1)
weights = (2*m*(m+1))/(k*(k+1)*(k+2))
weights = np.append(weights, 1-sum(weights))
k = np.append(k,k[-1]+1)
Kteo = []
Nsample = Nmax*M
for i in range(Nsample):
    Kteo.extend(choices(k,weights))
print(ks_2samp(K,Kteo))
#KS------------