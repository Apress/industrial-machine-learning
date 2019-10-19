#!/usr/bin/env python
# coding: utf-8

# # 08-02-Assess-01-Time-03

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Time.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
filename='08-02-Assess-Time-Date.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Time

# In[4]:


dirDataName = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[5]:


fileDataName='08-02-Retrieve-Time-Date.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[6]:


timeFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(timeFullDF.shape)


# # Perform Data Quality Checks

# In[7]:


A=timeFullDF
print('A',A.shape)
B=timeFullDF.head(500)
print('B',B.shape)

D=pd.concat([A,B], axis=0)
print('D',D.shape)

E=D.drop_duplicates(keep='last')
print('E',E.shape)


# # Create Clean Data

# In[8]:


TimeFinalDF=E


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


# # Save Time

# In[11]:


TimeFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[12]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




