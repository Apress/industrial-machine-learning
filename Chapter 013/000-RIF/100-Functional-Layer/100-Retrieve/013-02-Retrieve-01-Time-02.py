#!/usr/bin/env python
# coding: utf-8

# # 08-02-Retrieve-Time-02

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
filename='08-02-Retrieve-Time-Time.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
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


# # Create Time Satellite

# In[6]:


times = pd.date_range(start='2018/01/01 00:00', end='2018/01/01 23:59', freq='1min')
timesNameDF = pd.DataFrame(times.strftime('%H:%M'))
timesNameDF.index.name='TimeID'
timesNameDF.columns=['Time']


# In[7]:


timesKeyDF = pd.DataFrame(times.strftime('T%H%M'))
timesKeyDF.index.name='TimeID'
timesKeyDF.columns=['TimeKey']


# In[8]:


timesDF=timesKeyDF
timesDF=timesDF.merge(timesNameDF, how='inner', left_on='TimeID', right_on='TimeID')


# In[9]:


timesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[10]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

