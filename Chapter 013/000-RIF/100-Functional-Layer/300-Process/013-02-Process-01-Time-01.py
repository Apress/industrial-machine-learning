#!/usr/bin/env python
# coding: utf-8

# # 08-02-Process-01-Time-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Process Step](../../../../../images/DV-Time.JPG)

# ![RIF Functional Layer - Process Step](../../../../../images/RIF-FL-PRC.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/300-Curated-Zone/'
filename='08-02-Process-Time.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Time

# In[4]:


dirDataName = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[5]:


fileDataName='08-02-Assess-Time.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[6]:


time1DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time1DF.shape)


# In[7]:


fileDataName='08-02-Assess-Time-Date.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[8]:


time2DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time2DF.shape)


# In[9]:


fileDataName='08-02-Assess-Time-Time.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[10]:


time3DF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(time3DF.shape)


# In[11]:


time4DF=pd.merge(time1DF,time2DF)
timeFullDF=pd.merge(time4DF,time3DF)
print(timeFullDF.shape)


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


# # Save Time

# In[14]:


timeFullDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[15]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




