#!/usr/bin/env python
# coding: utf-8

# # 08-02-Assess-04-Location-01

# In[18]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Location.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[19]:


dirname = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
filename='08-02-Assess-Location.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[20]:


import pandas as pd
import os


# # Load Location

# In[21]:


dirDataName = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[22]:


fileDataName='08-02-Retrieve-Location.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[23]:


locationFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(locationFullDF.shape)


# # Perform Data Quality Checks

# In[24]:


A=locationFullDF
print('A',A.shape)

E=A.drop_duplicates(keep='last')
print('E',E.shape)


# # Create Clean Data

# In[25]:


locationFinalDF=E


# # Create 200-Structured-Zone

# ![Structured Zone](../../../../../images/DL-SZ.JPG)

# In[26]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[27]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Location

# In[28]:


fullRealZipName


# In[30]:


locationFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[31]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




