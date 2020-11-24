import numpy as np
import math
import random as rn
import matplotlib.pyplot as plt
import scipy.special

class Task1a:
    
    def __init__(self, size, grains, prob):
        self.size = size
        self.grains = grains    
        self.prob = prob

    def ___Task1a___(self):
    
        #slopes
        z = [0]*self.size
        #heights
        h = 0
        #threshold slopes
        zt = []
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1)

        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 200:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1
            
            #at t=0 we have h[1]=0
            height.append(h)

            #adding grain
            z[0] = z[0]+1
            h = h + 1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1
                        h=h-1

                    else:
                        self.relaxj(z,j)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1
        
        return height

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1
    
    
    #plots
    
    def plot(h,p,L):
        plt.plot(h, label = p)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("t", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("h(t; %s)" %L, fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.annotate(p, xy=(len(h),h[-1]), xytext=(6,0), color=plt.gca().lines[-1].get_color() , textcoords="offset points", size=20, va="center")
        plt.show()

    def ploth(h,l,L,log):
        plt.plot(h)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("t", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("h(t;L)", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        if log:
            plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.annotate(l, xy=(len(h),h[-1]), xytext=(6,0), color=plt.gca().lines[-1].get_color() , textcoords="offset points", size=20, va="center")
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class Task1b:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains    

    def ___Task1b___(self):
    
        #slopes
        z = [0]*self.size
        #heights
        h = [0]*self.size
        #threshold slopes
        zt = []
        #Number of grains
        n = [0]*self.grains
        n[0] = 1
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        heightave = []
        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 100:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1
            
            #at t=0 we have h[1]=0
            height.append(h[0])
            
            if i>(self.size)*(self.size):
                heightave.append(h[0])
            
            if i>0:
                n[i]=n[i-1]+1

            #adding grain
            z[0] = z[0]+1
            h[0] = h[0]+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,h,j)
                        zt[j] = rn.randint(1,2)
                        n[i]=n[i]-1
                        
                    elif j==0:
                        self.relax0(z,h)
                        zt[j] = rn.randint(1,2)

                    else:
                        self.relaxj(z,h,j)
                        zt[j] = rn.randint(1,2)


        if self.grains < (self.size)*(self.size):
            print("the number of grains to be added is too small to calculate the (steady state) average height")
            return 0
        sum = 0
        for i in heightave:
            sum = sum + i
        return sum/len(heightave), n

    #functions to be called when relaxing sites
        
    def relax0(self,z,h):
        h[0] = h[0]-1
        h[1] = h[1]+1
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,h,m):
        h[m] = h[m]-1
        h[m+1] = h[m+1]+1
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,h,m):
        h[self.size-1] = h[self.size-1]-1
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1


    def plot(n,L,Gs,vl):
        plt.plot(n[:Gs], label=L)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("t", fontname="Times New Roman", fontsize=35, labelpad=10)
        plt.ylabel("n(t)", fontname="Times New Roman", fontsize=35, labelpad=15)
        plt.xticks(fontsize=20,fontname="Times New Roman")
        plt.yticks(fontsize=20, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.annotate(L, xy=(Gs,n[-1]), xytext=(6,0), color=plt.gca().lines[-1].get_color() , textcoords="offset points", size=14, va="center")
        plt.axvline(x=vl, linewidth=1, color=plt.gca().lines[-1].get_color(), linestyle='--')
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class Task2b:
    def __init__(self, size):
        self.size = size
        
    def __Task2b__(self):
        
        #slopes
        z = [0]*self.size
        #threshold slopes
        zt = []
             
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))
        
        end = True
        i=0
        
        while end:
            
            #adding grain
            z[0] = z[0]+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        end = False
                        
                    elif j==0:
                        self.relax0(z,)
                        zt[j] = rn.randint(1,2)

                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)

            i=i+1
            

        return i-1
    
        #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,i):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1
            
    def plot(L,CT):
        plt.figure(figsize=(16,10), dpi=120)
        plt.scatter(L,CT)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("L", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("<tc(t)>", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
    

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
        
class Task2c:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    

    def ___Task2c___(self):
    
        #slopes
        z = [0]*self.size
        #heights
        h = 0
        #threshold slopes
        zt = []
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 5000:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1
            
            if i > self.size*self.size:
                height.append(h)
            
    

            #adding grain
            z[0] = z[0]+1
            h = h + 1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        h = h - 1
                        zt[j] = rn.randint(1,2)

                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
        
        return sum(height)/len(height)

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1

    def plot(L,h):
        plt.figure(figsize=(16,10), dpi=120)
        plt.scatter(L,h)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("L", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("<h(t)>", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
        
class Task2d:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    

    def ___Task2d___(self):
    
        #slopes
        z = [0]*self.size
        #heights
        h = 0
        #threshold slopes
        zt = []
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 500:
                print(str(round((i/self.grains)*100)) + "%")
                q=0
            q=q+1
            
            #at t=0 we have h[1]=0
            height.append(h)

            #adding grain
            z[0] = z[0]+1
            h = h+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                        h=h-1

                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
        
        return height

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1

    def plot(h,Gs,L,c):
        i = np.arange(0,Gs)
        plt.plot(i/(0.87*L**(2)), h, label="L="+str(L))
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 20)
        plt.xlabel("t/tc", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("h(t;L)/L", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
        
class Task2f:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    

    def ___Task2f___(self):
    
        #slopes
        z = [1]*self.size
        #heights
        h = 0
        #threshold slopes
        zt = []
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 500:
                print(str(round((i/self.grains)*100)) + "%")
                q=0
            q=q+1
            
            if i > (self.size*self.size)/2:
                height.append(h)

            #adding grain
            z[0] = z[0]+1
            h = h+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                        h=h-1

                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
        
        sigma = np.array(height)
        return np.std(sigma)

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1

    def plot(L,sigma):
        plt.plot(L,sigma)
        plt.scatter(L,sigma)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("t/tc", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("h(t;L)/L", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class TaskX:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    
    def ___TaskX___(self):
    
        #slopes
        z = [1]*self.size
        #thhreshold slopes
        zt = []
        #average tresholds
        zave = []
        zave2 = []
        #start counting slopes from
        ts = (self.size)*(self.size)/2
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        q = 0

        for i in range(self.grains):
            
            if q == 2000:
                print(str(round((i/self.grains)*100)) + "%")
                q=0
            q=q+1
            
            #adding grain
            z[0] = z[0]+1
            
            #do not enter the while loop if not necessary???
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
                        
            if i>ts:
                Sum = 0
                Sum2 = 0
                for k in z:
                    Sum = Sum + k
                    Sum2 = Sum2 + k**2
                zave.append(Sum/len(z))
                zave2.append(Sum2/len(z))
                
        return zave,zave2

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1
    
    def plot(L,z):
        plt.plot(L,z, marker='o')
        plt.grid(axis='both', alpha=.3)
        plt.xlabel("<z>", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("L", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=20,fontname="Times New Roman")
        plt.yticks(fontsize=20, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
            
#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class Task3a:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    
    def ___Task3a___(self):
    
        #slopes: we are interested in avalalanches of systems in steady state, we can initialize the system in the staircase configuration
        z = [1]*self.size
        #z = [0]*self.size
        #threshold slopes
        zt = []
        #Avalanche sizes
        s = []
        
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))
        
        q=0
        
        for i in range(self.grains):

            if q == 5000:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1
            
            #initializing counter for avalanche size
            c=0

            #adding grain
            z[0] = z[0]+1

            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        c+=1
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                        c+=1
                        
                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
                        c+=1

            if i>((self.size)*(self.size))/2:
                s.append(c)

        return s

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1
    

    def logbin(data, scale = 1., zeros = False):

        if scale < 1:
            raise ValueError('Function requires scale >= 1.')
        count = np.bincount(data)
        tot = np.sum(count)
        smax = np.max(data)
        if scale > 1:
            jmax = np.ceil(np.log(smax)/np.log(scale))
            if zeros:
                binedges = scale ** np.arange(jmax + 1)
                binedges[0] = 0
            else:
                binedges = scale ** np.arange(1,jmax + 1)
                # count = count[1:]
            binedges = np.unique(binedges.astype('uint64'))
            x = (binedges[:-1] * (binedges[1:]-1)) ** 0.5
            y = np.zeros_like(x)
            count = count.astype('float')
            for i in range(len(y)):
                y[i] = np.sum(count[binedges[i]:binedges[i+1]]/(binedges[i+1] - binedges[i]))
                # print(binedges[i],binedges[i+1])
            # print(smax,jmax,binedges,x)
            # print(x,y)
        else:
            x = np.nonzero(count)[0]
            y = count[count != 0].astype('float')
            if zeros != True and x[0] == 0:
                x = x[1:]
                y = y[1:]
        y /= tot
        x = x[y!=0]
        y = y[y!=0]
        return x,y
    
    def plot(p1,p2,L):
        plt.plot(p1,p2, label="L=" + str(L))
        #plt.plot(p1,p2, label="Measured")
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 20)
        plt.xlabel("s", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("P(s;L)", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()

        

    def plotc(p1,p2,L,tau,D):
        plt.plot(p1/L**(D),p2*(p1**(tau)), label="L=" + str(L))
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 'x-large')
        plt.xlabel("s/L^D", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("s^tau P(s;L)", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=20,fontname="Times New Roman")
        plt.yticks(fontsize=20, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        plt.yscale("log")
        plt.xscale("log")
    
    def plotk(L,i):
        #L=np.array([np.log(L)])
        #i=np.array([np.log(i)])
        plt.scatter(L,i)
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        #plt.legend(fontsize = 'x-large')
        plt.xlabel("L", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("<s^k>", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()
    
    
    def plotkCorrections(L,i,k):
        L=np.array(L)
        i=np.array(i/(L**(2.2335*(1+(k+1)-1.6968))))
        plt.scatter(L,i)
        plt.plot(L,i, label = "k=" + str(k+1))
        #plt.title("", fontname="Times New Roman", fontsize=22)
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 'x-large')
        plt.xlabel("L", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("<s^k>", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()
    
    
    
    def momentum(s,k):
        sum = 0
        for i in s:
            sum = sum + i**(k)
        return sum/len(s)


    def plotCollapse(p1,p2,L,h,sigma):
        
        p1=np.array(p1)
        p2=np.array(p2)
        
        plt.plot(((p1-h)/sigma),p2*sigma, label="L=" + str(L))
        #plt.plot(p1,p2, label="Measured")
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 'x-large')
        plt.xlabel("s", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("P(s;L)", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class TaskExtra:
    
    def __init__(self, size, grains, prob):
        self.size = size
        self.grains = grains
        self.prob = prob
    

    def ___TaskExtra___(self):
    
        #slopes
        z = [0]*self.size
        #threshold slopes
        zt = []
        #configurations
        configs = []
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1)
        
        q=0
        
        for i in range(self.grains):
            
            if q == 100:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1
            
            if i>(self.size)*(self.size):
                configs.append([z[0],z[1],z[2],z[3]])
                

            #adding grain
            z[0] = z[0]+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1

                    else:
                        self.relaxj(z,j)
                        zt[j] = np.random.choice(2,1,p=[self.prob,1-self.prob])[0] + 1

        confdiv = []     
        for i in configs:
            if not(i in confdiv):
                confdiv.append(i)
        return len(confdiv)
    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1


#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------
class Task2g:
    
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains    

    def ___Task2g___(self):
    
        #slopes
        z = [0]*self.size
        #heights
        h = 0
        #threshold slopes
        zt = []
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))

        height = []
        
        q=0
        
        for i in range(self.grains):
            
            if q == 500:
                print(str(round((i/self.grains)*100)) + "%")
                q=0
            q=q+1
            
            #at t=0 we have h[1]=0
            if i> (self.size)*(self.size):
                height.append(h)

            #adding grain
            z[0] = z[0]+1
            h = h+1
            
            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                        h=h-1

                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)
        
        return height

    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1

    
    
    def Pkk(k1,k2,L):
        f1 = scipy.special.binom(L, k1)*((1/3)**(k1))*(1-1/3)**(L-k1)
        f2 = scipy.special.binom(L-k1, k2)*((1/2)**(k2))*(1/2)**(L-k1-k2)
        
        return f1*f2

#-----------------------------------------------------------
#-----------------------------------------------------------
#-----------------------------------------------------------

class Zave:
    def __init__(self, size, grains):
        self.size = size
        self.grains = grains
    
    def ___Zave___(self):
    
        #slopes: we are interested in avalalanches of systems in steady state, we can initialize the system in the staircase configuration
        z = [1]*self.size
        #z = [0]*self.size
        #threshold slopes
        zt = []
        
        zave = np.array([0]*self.size)
        
        #sysytem inizialization
        for _ in range(self.size):
            zt.append(rn.randint(1,2))
        
        q=0
        c=0
        
        for i in range(self.grains):

            if q == 5000:
                print(str((i/self.grains)*100) + "%")
                q=0
            q=q+1

            #adding grain
            z[0] = z[0]+1

            #do not enter the while loop if not necessary
            if z[0]<=zt[0]:
                relaxSites = np.array([], dtype=int)
            else:
                relaxSites = np.arange(self.size, dtype=int)

            while len(relaxSites)>0:
                
                relaxSites = np.array([], dtype=int)
                for k in range(self.size):
                    if z[k]>zt[k]:
                        relaxSites = np.append(relaxSites, int(k))
                
                for j in relaxSites:
                    if j==self.size-1:
                        self.relaxL(z,j)
                        zt[j] = rn.randint(1,2)
                        
                    elif j==0:
                        self.relax0(z)
                        zt[j] = rn.randint(1,2)
                        
                    else:
                        self.relaxj(z,j)
                        zt[j] = rn.randint(1,2)

            if i>((self.size)*(self.size))/2:
                zave = zave + z
                c=c+1
        return zave/c



    #functions to be called when relaxing sites
        
    def relax0(self,z):
        z[0] = z[0]-2
        z[1] = z[1]+1
        
    def relaxj(self,z,m):
        z[m] = z[m]-2
        z[m-1] = z[m-1]+1
        z[m+1] = z[m+1]+1
        
    def relaxL(self,z,m):
        z[self.size-1] = z[self.size-1]-1
        if self.size>1:
            z[self.size-2] = z[self.size-2]+1    
        
    def plot(p1,p2,L):
        plt.plot(p1,p2, label="L=" + str(L))
        plt.scatter(p1,p2)
        #plt.plot(p1,p2, label="Measured")
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 20)
        plt.xlabel("<zi>", fontname="Times New Roman", fontsize=25, labelpad=10)
        plt.ylabel("i", fontname="Times New Roman", fontsize=25, labelpad=15)
        plt.xticks(fontsize=28,fontname="Times New Roman")
        plt.yticks(fontsize=28, fontname="Times New Roman")
        #plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)
        plt.gca().spines["left"].set_alpha(0.3)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()