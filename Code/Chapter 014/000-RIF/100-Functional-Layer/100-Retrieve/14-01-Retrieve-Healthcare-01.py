#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # 14-01-Retrieve-Healthcare-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Location.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 14/990-DL/100-Raw-Zone/'
filename='14-01-Retrieve-Healthcare.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import zipfile as zp
import os


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[4]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[5]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Create Healthcare

# In[6]:


dirDataName = '../../../../../Data/Chapter 14/000-ExternalData/01-Healthcare/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# ## Get Healthcare

# In[7]:


fileDataName='Hospital-General-Information.csv'
fileFullName= os.path.join(pathRealDataName, fileDataName)
print(fileFullName)


# In[8]:


healthDF = pd.read_csv(fileFullName, header=0, delimiter=',')
print(healthDF.shape)


# In[9]:


healthDF.index.name='IDKey'
print(healthDF.shape)
print(healthDF.head())


# In[10]:


print(fullRealZipName)


# In[11]:


healthDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[12]:


nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




