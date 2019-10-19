#!/usr/bin/env python
# coding: utf-8

# # 08-02-Assess-03-Object-01

# In[1]:


import datetime
nowStart = datetime.datetime.now()


# ![RIF Functional Layer - Assess Step](../../../../../images/DV-Object.JPG)

# ![RIF Functional Layer - Assess Step](../../../../../images/RIF-FL-ASS.JPG)

# In[2]:


dirname = '../../../../Chapter 08/990-DL/200-Structured-Zone/'
filename='08-02-Assess-Object.csv'
fileZipname=filename + '.gz'
print(fileZipname)


# In[3]:


import pandas as pd
import os


# # Load Object

# In[4]:


dirDataName = '../../../../Chapter 08/990-DL/100-Raw-Zone/'
pathRealDataName=os.path.realpath(dirDataName)
print(pathRealDataName)


# In[ ]:


fileDataName='08-02-Retrieve-Object.csv.gz'
fileFullDataName= os.path.join(pathRealDataName, fileDataName)
print(fileFullDataName)


# In[ ]:


objectFullDF= pd.read_csv(fileFullDataName, encoding='utf-8', compression='gzip')
print(objectFullDF.shape)


# # Perform Data Quality Checks

# In[ ]:


A=objectFullDF
print('A',A.shape)

E=A.drop_duplicates(keep='last')
print('A',E.shape)


# # Create Clean Data

# In[ ]:


objectFinalDF=E


# # Create 200-Structured-Zone

# ![Structured Zone](../../../../../images/DL-SZ.JPG)

# In[ ]:


pathRealName=os.path.realpath(dirname)
print(pathRealName)
fullRealZipName = os.path.join(pathRealName, fileZipname)


# In[ ]:


if not os.path.exists(pathRealName):
    print('Make:', pathRealName)
    os.makedirs(pathRealName)


# # Save Object

# In[ ]:


fullRealZipName


# In[ ]:


objectFinalDF.to_csv(fullRealZipName, index=False, encoding='utf-8', compression='gzip')


# In[ ]:


print(fullRealZipName)
nowStop = datetime.datetime.now()
runTime=nowStop-nowStart
print('Start:', nowStart.strftime('%Y-%m-%d %H:%M:%S'))
print('Stop: ', nowStop.strftime('%Y-%m-%d %H:%M:%S'))
print('Time: ', runTime)


# In[ ]:




