#!/usr/bin/env python
# coding: utf-8

# # 08-02-Retrieve-Time-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Retrieve Step](../../../../../images/RIF-FL-RET.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
filename='08-02-Retrieve-Time-Date.csv'
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


# # Create Dates Satellite

# In[6]:


dates = pd.date_range(start='2017-1-1', end='2018-12-31', freq='D')


# In[7]:


datesNameDF = pd.DataFrame(dates.strftime('%Y-%m-%d'))
datesNameDF.index.name='DateID'
datesNameDF.columns=['Date']


# In[8]:


datesKey=dates.strftime('D%Y%m%d')
datesKeyDF=pd.DataFrame(datesKey)
datesKeyDF.index.name='DateID'
datesKeyDF.columns=['DateKey']


# In[9]:


datesDF=datesKeyDF
datesDF=datesDF.merge(datesNameDF, how='inner', left_on='DateID', right_on='DateID')


# In[10]:


datesDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[11]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)

