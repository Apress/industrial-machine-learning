#!/usr/bin/env python
# coding: utf-8

# # 08-02-Process-05-Event-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Process Step](../../../../../images/DV-Event.JPG)

# ![RIF Functional Layer - Process Step](../../../../../images/RIF-FL-PRC.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/300-Curated-Zone/'
filename='08-02-Process-Event.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Event

# In[4]:


dirDataName = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[5]:


fileDataName='08-02-Assess-Event.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[6]:


eventFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(eventFullDF.shape)


# # Create 300-Curated-Zone

# ![Curated Zone](../../../../../images/DL-CUZ.JPG)

# In[7]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[8]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Event

# In[9]:


eventFullDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[10]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

