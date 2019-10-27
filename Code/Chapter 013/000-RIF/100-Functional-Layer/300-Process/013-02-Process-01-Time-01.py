#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # 13-02-Process-01-Time-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Process Step](../../../../../images/DV-Time.JPG)

# ![RIF Functional Layer - Process Step](../../../../../images/RIF-FL-PRC.JPG)

# In[2]:


import pandas as pd
import os


# In[3]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/300-Curated-Zone/'))
print(dirname)


# In[4]:


filename='13-02-Process-Time.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# # Load Time

# In[5]:


dirDataName = os.path.abspath(os.path.join(dirbasename,'900-DL/200-Structured-Zone/'))
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[6]:


fileDataName='13-02-Assess-Time.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[7]:


time1DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time1DF.shape)


# In[8]:


fileDataName='13-02-Assess-Time-Date.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[9]:


time2DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time2DF.shape)


# In[10]:


fileDataName='13-02-Assess-Time-Time.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[11]:


time3DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time3DF.shape)


# In[12]:


time4DF=pd.merge(time1DF,time2DF)
timeFullDF=pd.merge(time4DF,time3DF)
print(timeFullDF.shape)


# # Create 300-Curated-Zone

# ![Curated Zone](../../../../../images/DL-CUZ.JPG)

# In[13]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[14]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Time

# In[15]:


timeFullDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[16]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




