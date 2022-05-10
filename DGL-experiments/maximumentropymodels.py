import numpy as np
import networkx as nx
from tqdm import tqdm
from scipy.spatial.distance import squareform
from matplotlib.pyplot import figure
import seaborn as sns

# traditional configuration model that fixes the expected degree sequence

def configuration_model(k, precision=10**(-5), loops=10000):
    n=len(k)
    t=np.random.uniform(size=(n,1))
    oldt=np.random.uniform(size=(n,1))

    for kk in tqdm(range(loops)):
        T=t*t.transpose()
        summat=(np.ones((n,1))*t.transpose())/(1 + T)
        summat=summat-np.diag(np.diagonal(summat))
        summat=np.sum(summat,axis=1, keepdims=True)
        t=k/(summat+(summat==0))
            
        if (max(abs((t>0)*(1-t/(oldt+(oldt==0)))))< precision):
            break

        oldt=t
            
            
    print("Loops ", kk+1)
    print('Error margin: ', max(abs((t>0)*(1-t/(oldt+(oldt==0))))))

    T=t*(t.transpose())
    Z=1+T;
    pmatrix=T/(Z+(Z==0))
    pmatrix=pmatrix-np.diag(np.diagonal(pmatrix))
    kcal=np.sum(pmatrix,axis=1,keepdims=True);  

    return (pmatrix, kcal) 


# unipartite positive and negative layers ...k01, k10 are column vectors
def multidegree_entropy_pos_neg(k01, k10, precision=10**(-5), loops=10000):
    n=len(k01)
    t01=np.random.uniform(size=(n,1))
    t10=np.random.uniform(size=(n,1))
    oldt01=np.random.uniform(size=(n,1))
    oldt10=np.random.uniform(size=(n,1))    
    
    for kk in tqdm(range(loops)):
            T01=t01*(t01.transpose())
            T10=t10*(t10.transpose())
            Z=1+ T01 + T10
            
            #p01
            summat=(np.ones((n,1))*t01.transpose())/(Z+(Z==0))
            summat=summat-np.diag(np.diagonal(summat))
            summat=np.sum(summat,axis=1, keepdims=True);
            t01=k01/(summat+(summat==0))
            T01=t01*(t01.transpose())
            
            Z=1+ T01 + T10
    
            #p10
            summat=(np.ones((n,1))*t10.transpose())/(Z+(Z==0))
            summat=summat-np.diag(np.diagonal(summat))
            summat=np.sum(summat,axis=1,keepdims=True)
            t10=k10/(summat+(summat==0))
            
            if np.logical_and((max(abs((t01>0)*(1-t01/(oldt01+(oldt01==0)))))< precision),(max(abs((t10>0)*(1-t10/(oldt10+(oldt10==0)))))<precision)):
                break

            oldt01=t01
            oldt10=t10
            
            
    print("Loops ", kk+1)
    print('Error margin: ', max((max(abs((t01>0)*(1-t01/(oldt01+(oldt01==0)))))),max(abs((t10>0)*(1-t10/(oldt10+(oldt10==0)))))))
    T01=t01*(t01.transpose());
    T10=t10*(t10.transpose());

    Z=1+ T01 + T10;
    
    
    summat01=T01/(Z+(Z==0))
    summat01=summat01-np.diag(np.diagonal(summat01))
    k01cal=np.sum(summat01,axis=1,keepdims=True);  
    
    summat10=T10/(Z+(Z==0))
    summat10=summat10-np.diag(np.diagonal(summat10))
    k10cal=np.sum(summat10,axis=1,keepdims=True)
                    
    pconditional=summat10/(summat10+summat01+(summat10==0))
    
    return (summat01, k01cal, summat10, k10cal, pconditional)   



if __name__ == "__main__":
    print("testing standard configuration model")
    ba=nx.barabasi_albert_graph(500,2)

    print("500 nodes, barabasi-albert")
    degree_sequence=np.array([[ba.degree(idn) for idn in ba.nodes]]).T # degree sequence
    (pm, degree_sequence_cal)=configuration_model(degree_sequence)

    figure(figsize=(8, 8))
    ax = sns.distplot(squareform(pm), hist_kws=dict(alpha=0.1))
    ax.set(xlim = [0,1], xlabel='$p^{ij}$', ylabel='PDF')

