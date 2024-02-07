#!/usr/bin/env python
# coding: utf-8

# # DAY 04 OF 75 DAYS CHALLENGE 

# # MATPLOTLIB 

# In[20]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import PIL


# In[4]:


x = [ 2,4,56,6,7]
y= [7,8,9,6,78]
plt.plot(x,y)
plt.show()


# In[14]:


a = [1,3,6,9,19]
b = [2,3,4,5,6]
c =['r','b','g','b']
plt.bar(a,b,color=c)
plt.show()


# In[54]:


a = [8,6,4,3,2]


plt.pie(a)
plt.show()


# # bar plot 

# In[35]:


x=['python','c','c++',"java"]
y =[88,45,67,34]   
c= ['r','b','g','y']
plt.xlabel("language", fontsize= 12)
plt.ylabel('NO.', fontsize= 12)
plt.title("language uses", fontsize = 20)
plt.bar(x,y, color = c,width =0.8,edgecolor="b",alpha= 0.9,linestyle = ':',linewidth = 1,label = 'sumit singh')
plt.legend()
plt.show()


# In[4]:


df= pd.read_csv("train.csv")


# In[12]:


x=['python','c','c++',"java"]
y =[88,45,67,34]   
c= ['r','b','g','y']
plt.xlabel("language", fontsize= 12)
plt.ylabel('NO.', fontsize= 12)
plt.title("language uses", fontsize = 20)
plt.scatter(x,y, color = c,edgecolor="b",alpha= 0.9,linestyle = ':',linewidth = 1,label = 'sumit singh')
plt.legend()
plt.show()


# In[34]:


from PIL import Image 
import matplotlib.pyplot as plt
fname =r'ss.jpg'
image =Image.open(fname).convert("L")
plt.imshow(image ,cmap = 'gray')
plt.show()


# In[44]:


import matplotlib.pyplot as plt
from PIL import Image 
fname = r'jgjtj.jpg'
image = Image.open(fname).convert('L')
plt.imshow(image,cmap ='gray')
plt.grid()
plt.show()


# In[43]:


from  PIL import Image
fname = r'jgjtj.jpg'
image = Image.open(fname).convert('L')
plt.imshow(image,cmap = 'RdPu_r')
plt.show()                                  


# In[ ]:




