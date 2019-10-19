#!/usr/bin/env python
# coding: utf-8

# # 08-02-Retrieve-Location-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/DV-Location.JPG)

# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
filename='08-02-Retrieve-Location.csv'
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


# # Create Location

# In[6]:


dirDataName = '../../../../../Data/Chapter 08/000-ExternalData/04-Location/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# ## Get Location

# In[7]:


fileZipName='ukpostcodes.zip'
fileDataName='ukpostcodes.csv'
fileFullZipName= os.path.join(pathRealDataName, fileZipName)
print(fileFullZipName)


# In[8]:


with zp.ZipFile(fileFullZipName) as z:
    with z.open(fileDataName) as f:
        locationDF = pd.read_csv(f, header=0, delimiter=',')


# In[9]:


locationDF.index.name='IDKey'
print(locationDF.shape)
print(locationDF.head())


# In[10]:


locationDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[11]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

