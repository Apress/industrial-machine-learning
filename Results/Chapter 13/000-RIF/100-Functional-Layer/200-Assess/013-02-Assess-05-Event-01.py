#!/usr/bin/env python
# coding: utf-8

# ## Apress - Industrialized Machine Learning Examples
# 
# Andreas Francois Vermeulen
# 2019
# 
# ### This is an example add-on to a book and needs to be accepted as part of that copyright.

# # 13-02-Assess-01-Event-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Event.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[2]:


import pandas as pd
import os


# In[3]:


dirbasename=os.path.abspath(os.path.join(*[os.path.dirname(os.path.dirname(os.getcwd()))], os.pardir))
print(dirbasename)
dirname = os.path.abspath(os.path.join(dirbasename,'900-DL/200-Structured-Zone/'))
print(dirname)


# In[4]:


filename='13-02-Assess-Event.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# # Load Event

# In[5]:


dirDataName = os.path.abspath(os.path.join(dirbasename,'900-DL/100-Raw-Zone/200-Load-Data/05-Event'))
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[6]:


fileDataName='13-02-Retrieve-Event-000001.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[7]:


eventFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(eventFullDF.shape)


# # Perform Data Quality Checks

# In[8]:


A=eventFullDF
print('A',A.shape)

E=A.drop_duplicates(keep='last')
print('E',E.shape)


# # Create Clean Data

# In[9]:


EventFinalDF=E


# # Create 200-Structured-Zone

# ![Structured Zone](../../../../../images/DL-SZ.JPG)

# In[10]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[11]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Event

# In[12]:


fullRealZipName


# In[13]:


EventFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[14]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




