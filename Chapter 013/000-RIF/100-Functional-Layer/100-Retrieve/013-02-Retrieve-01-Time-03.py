#!/usr/bin/env python
# coding: utf-8

# # 08-02-Retrieve-Time-03

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
filename='08-02-Retrieve-Time.csv'
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


# # Create Date and Time Hub

# In[6]:


dates = pd.date_range(start='2017-1-1', end='2018-12-31', freq='D')


# In[7]:


datesKey=dates.strftime('D%Y%m%d')
datesKeyDF=pd.DataFrame(datesKey)
datesKeyDF.index.name='DateID'

datesKeyDF.columns=['DateKey']
datesKeyDF['Key1']='1'


# In[8]:


times = pd.date_range(start='2018/01/01 00:00', end='2018/01/01 23:59', freq='1min')


# In[9]:


timesKeyDF = pd.DataFrame(times.strftime('T%H%M'))
timesKeyDF.index.name='TimeID'
timesKeyDF.columns=['TimeKey']
timesKeyDF['Key1']='1'


# In[10]:


datetimesDF=datesKeyDF


# In[11]:


datetimesDF=datetimesDF.merge(timesKeyDF, how='inner', left_on='Key1', right_on='Key1')


# In[12]:


datetimesDF.drop('Key1', axis=1, inplace=True)


# In[13]:


datetimesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[14]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

