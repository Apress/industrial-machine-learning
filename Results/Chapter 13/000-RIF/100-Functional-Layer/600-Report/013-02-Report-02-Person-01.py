#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # 13-02-Report-02-Person-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Process Step](../../../../../images/DV-Person.JPG)

# ![RIF Functional Layer - Process Step](../../../../../images/RIF-FL-RPT.JPG)

# In[2]:


import pandas as pd
import os


# In[3]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/300-Curated-Zone/'))
print(dirname)


# In[4]:


filename='13-02-Raport-Person.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# # Load Person

# In[5]:


dirDataName = os.path.abspath(os.path.join(dirbasename,'900-DL/300-Curated-Zone/'))
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[6]:


fileDataName='13-02-Organize-Person.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[7]:


personFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(personFullDF.shape)


# In[8]:


print(personFullDF.head())


# In[9]:


d=personFullDF
d['Cnt'] = 1
print(d.shape)


# In[10]:


import numpy as np
p=pd.pivot_table(d, values='Cnt', index=['LastName'], columns=['FirstName'], aggfunc=np.sum)


# In[11]:


print(p.shape)


# # Create 300-Curated-Zone

# ![Curated Zone](../../../../../images/DL-CUZ.JPG)

# In[12]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[13]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Person

# In[14]:


p.to_csv(fullRealZipName, index=True, encoding='utf-8', compression='gzip')


# In[15]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




