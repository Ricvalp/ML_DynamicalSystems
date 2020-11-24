import random as rd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

class Funcs:
    
    def Initial_graph(m):
        N = 2*m + 1
        
        Nb = []
        a = []
        for _ in range(N):
            Nb.append([])
        
        
        for i in range(N):
            for j in range(N):
                if j != i:
                    Nb[i].append(j)
                    a.append(i)
            
        return Nb,a
    
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
    
    def logbiN(data, scale = 1., zeros = False):

        if scale < 1:
            raise ValueError('Function requires scale >= 1.')
        count = np.bincount(data)
#        tot = np.sum(count)
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

        x = x[y!=0]
        y = y[y!=0]
        return x,y

    def plotG(Nb,size):
        E = []
        index = 0
        for e in Nb:
            for ee in e:
                E.append([index,ee])
            index += 1
        plt.figure()
        G = nx.Graph()
        G.add_edges_from(E)
        nx.draw(G, with_labels=True, font_weight='bold', linewidths=0.5, node_size=size)

    def plot(k,p,k1,p1,m):
        plt.scatter(k,p, label="m = " + str(m), s=60, marker='o')
        plt.plot(k1,p1, color = 'r', linestyle='--')
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$k$", fontsize=28, labelpad=8)
        plt.ylabel("$n(k)$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotLOGBIN(k,p,k1,p1):
        plt.scatter(k,p, label="Raw Data", s=70, marker='x')
        plt.scatter(k1,p1, label="Log-Binned Data", s=40, marker='d')
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$k$", fontsize=28, labelpad=8)
        plt.ylabel("$p(k)$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotDC(k,p,N):
        plt.scatter(k,p, label= "N=" + str(N), s=35, marker='o')
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$k/k_{1}$", fontsize=28, labelpad=8)
        plt.ylabel("$p(k)/p_{\infty}(k)$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

    def Zipf_plot(k,p):
        plt.scatter(k,p, s=50, marker='d')
        plt.grid(axis='both', alpha=.3)
        plt.xlabel("$k$", fontsize=28, labelpad=8)
        plt.ylabel("$rank$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

    def plotRandom(k,p,k1,p1,q):
        plt.scatter(k, p, label="q=" + str(q), s=50, marker='o')
        plt.plot(k1, p1, label = "Preferential Attachment", linestyle = '-.')
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$k$", fontsize=28, labelpad=8)
        plt.ylabel("$p(k)$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.yscale("log")
        plt.xscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotRandomDC(k,p,N):
        plt.scatter(k,p, label="N=" + str(N), s=15)
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 'x-large')
        plt.xlabel("")
        plt.ylabel("")
        plt.xticks(fontsize=35, fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()

    def plotLargest(n,kmax,m,err,c):
        N=np.arange(min(n),max(n),10)
        plt.plot(N, (m*(m+1)*N)**(0.5), label="Expected", linestyle='--')
        plt.plot(N, (10**(c[1]))*N**(c[0]), label="Best-fit", linestyle='-.')
        plt.errorbar(n,kmax, yerr=err, label="Numerical", color='r', linestyle="None", marker='x', markersize=25)
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$N$", fontsize=28, labelpad=8)
        plt.ylabel("$k_{1}$", fontsize=28, labelpad=15)
        plt.xscale("log")
        plt.yscale("log")
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotLargestRA(n,kmax,m,err,c):
        N=np.arange(min(n),max(n),10)
        plt.plot(np.log(N),   np.log(N)/(np.log((m+1)/(m)))  + m  , label="Expected", linestyle='--')
        plt.plot(np.log(N), c[0]*np.log(N) + c[1], label="Best-fit", linestyle='-.')
        plt.errorbar(np.log(n),kmax, yerr=err, label="numeric", color='r', linestyle="None", marker='x', markersize=25)
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$ln(N)$", fontsize=28, labelpad=8)
        plt.ylabel("$k_{1}$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotk(k,labell):
        t = range(labell,labell+len(k))
        plt.scatter(t,k, label="i="+ str(labell))
        plt.grid(axis='both', alpha=.3)
        plt.legend(fontsize = 25)
        plt.xlabel("$t$", fontsize=28, labelpad=8)
        plt.ylabel("$k_{i}$", fontsize=28, labelpad=15)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()
        
    def plotkTeo(maxx,m):
        t = np.arange(1,maxx)
        plt.plot(t,2*m*t**(1/2), label="Expected sublinear growth", linestyle='dashed', color='r')
        plt.legend(fontsize = 25)

    def plotCDF(k,p):
        plt.scatter(k,p, s=50, marker='d')
        plt.grid(axis='both', alpha=.3)
        plt.xlabel("$k$", fontsize=28, labelpad=8)
        plt.ylabel("$p_{<}(k)$", fontsize=28, labelpad=17)
        plt.xticks(fontsize=35,fontname="Times New Roman")
        plt.yticks(fontsize=35, fontname="Times New Roman")
        plt.xscale("log")
        plt.yscale("log")
        plt.gca().spines["top"].set_alpha(0.0)    
        plt.gca().spines["bottom"].set_alpha(0.3)
        plt.gca().spines["right"].set_alpha(0.0)    
        plt.gca().spines["left"].set_alpha(0.3)
        plt.show()