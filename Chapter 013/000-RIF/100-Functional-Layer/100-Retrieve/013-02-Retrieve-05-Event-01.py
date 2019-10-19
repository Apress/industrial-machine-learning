#!/usr/bin/env python
# coding: utf-8

# # 08-02-Retrieve-Event-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Event.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
filename='08-02-Retrieve-Event.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Events

# In[4]:


dirDataName = '../../../../../Data/Chapter 08/000-ExternalData/05-Event/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[5]:


fileDataName='Event.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[6]:


objectFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(objectFullDF.shape)


# # Create 100-Raw-Zone

# ![Raw Zone](../../../../../images/DL-RZ.JPG)

# In[7]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[8]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Events

# In[9]:


objectFullDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[10]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

