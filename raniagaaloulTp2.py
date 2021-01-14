#!/usr/bin/env python
# coding: utf-8

# # Simulation du jeux de LIDO simplifié

# ## Principe
# On considére un jeux de Lido simple:
# on dispose d'un un seul pion.
# 
# - Etape 0 :
# Le pion doit sort de sa prison lorsqu'on obtient un 6.
# 
# - Etape 1 :
# Le pion doit atteindre exactement une position cible situé à N pas de distance de sa prison 
# 
# Soit $X_n$ la variable aléatoire qui represente le nombre de coup nécéssaire pour atteindre la positions cible.
# 
# **Objectif 1** : Simuler le jeux 
# 
# **Objectif 2** : Calculer une estimation de l'éspérance mathématique de $X_n$ en utilisant `python`
# 
# **Objéctif 3** : Observer la variation de $\mathbb{E}(X_n)$ en fonction de $n$
# 
# <img src="LIDO.png">
# 

# In[8]:


import numpy as np


# ### Simulation du lancé de dé

# In[12]:


def Roll():
    return int(np.random.choice(_____,____))


# In[13]:


Roll()


# ### Compléter le code et commenter

# In[14]:


A=0  # position
NA=0 # la valeur de dé aprés le lancement
N=10  # position de la cible
c=0 # compteur
while (A<N) :
    NA=Roll() 
    if NA==6 and A==0:
        A=1 
        c=c+1 
        print(NA,A,c) 
    elif A>0 and NA+A<N: 
        A=A+NA 
        c=c+1
        print (NA,A,c)   
    elif  NA+A==N: 
        A=A+NA 
        c=c+1
        print (NA,A,c) 
        break  
    else: 
        c=c+1
        print (NA,A,c)
    pass


# ### Simulation
# Ecrire une foction `sim` qui simule le jeux et qui prend comme variable le nombre de pas $n$ nécessazire pour atteindre la cible

# In[6]:



def sim(N):
    A=0
    NA=0
    c=0
    while (A<N) :
        NA=Roll() 
        if NA==6 and A==0:
            A=1 
            c=c+1  
        elif A>0 and NA+A<N: 
            A=A+NA 
            c=c+1   
        elif  NA+A==N:  
            c=c+1
            A=A+NA 
            print (NA,A,c) 
            break  
        else: 
            c=c+1
    return c


# In[7]:


sim(20)


# ### Simulation de $10^5$  scénario 

# In[ ]:


Freq=np.fromiter((sim(20) for i in range(10**5)),dtype=int)


# In[148]:


ESP=Freq.sum()/10**5


# In[11]:


x=list(range(10,20))


# In[14]:


y=[np.fromiter((sim(u) for i in range(5*10**4)),dtype=int).sum()/50000 for u in x]


# In[15]:


import matplotlib.pyplot as plt


# In[16]:


plt.plot(x,y)


# In[17]:


from scipy import stats
import numpy as np
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)


# In[18]:


slope


# In[19]:


intercept


# In[ ]:




