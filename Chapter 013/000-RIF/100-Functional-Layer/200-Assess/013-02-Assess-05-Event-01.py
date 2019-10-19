#!/usr/bin/env python
# coding: utf-8

# # 08-02-Assess-01-Event-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Event.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
filename='08-02-Assess-Event.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Event

# In[4]:


dirDataName = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[5]:


fileDataName='08-02-Retrieve-Time.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[6]:


eventFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(eventFullDF.shape)


# # Perform Data Quality Checks

# In[7]:


A=eventFullDF
print('A',A.shape)

E=A.drop_duplicates(keep='last')
print('E',E.shape)


# # Create Clean Data

# In[8]:


EventFinalDF=E


# # Create 200-Structured-Zone

# ![Structured Zone](../../../../../images/DL-SZ.JPG)

# In[9]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[10]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Event

# In[11]:


fullRealZipName


# In[12]:


EventFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[13]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:





# In[ ]:




