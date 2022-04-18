#!/usr/bin/env python
# coding: utf-8

# #                        # Assignment - 1
#     
#     
#   1) Import the necessary libraries
# 
# 
#     import pandas as pd
#     import numpy as np
# 

# In[ ]:


2) Import the dataset from this(https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user).
   
    Use sep= "|" while reading the data
       
   url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
   


# In[ ]:



   3) Assign it to a variable called users and use the 'user_id' as index
   
   users= pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',index_col='user_id',sep='|')
   


# In[ ]:



    user_id|age|gender|occupation|zip_code
          1|24|M|technician|85711
          2|53|F|other|94043
          3|23|M|writer|32067
          4|24|M|technician|43537
          5|33|F|other|15213
           ...
        939|26|F|student|33319
        940|32|M|administrator|02215
        941|20|M|student|97229
        942|48|F|librarian|78209
        943|22|M|student|77841
  

    users.head(25)
    
         age  gender  occupation   zip_code
user_id

   1      24    M      technician    85711
   2      53    F       mother       94043
   3      23    M       writer       32067
   4      24    M      technician    43537
   5      33    F       other        15213
   6      42    M      executive     98101
   7      57    M     administrator  91344
   8      36    M     administrator  05201
   9      29    M       student      01002
  10      53    M       lawyer       90703
  11      39    F       other        30329
  12      28    F       other        06405
  13      47    M      educator      29206
  14      45    M      scientist     55106
  15      49    F      educator      97301
  16      21    M      entertainment 10309
  17      30    M       programmer   06355
  18      35    F      other         37212
  19      40    M      librarian     02138
  20      42    F      homemaker     95660
  21      26    M      writer        30068
  22      25    M      writer        40206
  23      30    F      artist        48197
  24      21    F      artist        94533
  25      39    M     engineer       55107
    
    
    
    


# In[ ]:


4) See the first 10 and last 10 entries 
    
   users.tail(10)
  
  
          age      gender     occupation        zip_code
  user_id
   934    61         M         engineer           22902
   935    42         M          doctor            66221
   936    24         M          other             32789
   937    48         M         educator           98072
   938    38         F        technician          55038
   939    26         F        student             33319
   940    32         M       administrator        02215
   941    20         M        student             97229
   942    48         F        librarian           78209
   943    22         M        student             77841
    


# In[ ]:



     get_ipython().set_next_input('     5)  What is the number of observations in the dataset');get_ipython().run_line_magic('pinfo', 'dataset')
    
    
        
        users.shape[0]
        
       <class 'pandas.core.frame.DataFrame'>
    Int64Index: 943 entries, 1 to 943
    Data columns (total 4 columns):
    age           943 non-null int64
    gender        943 non-null object
    occupation    943 non-null object
    zip_code      943 non-null object
    dtypes: int64(1), object(3)
    memory usage: 36.8+ KB
    (943, 4)  
    


# In[ ]:



     get_ipython().set_next_input('     6) What is the number of columns in the dataset');get_ipython().run_line_magic('pinfo', 'dataset')
    
        users.shape[1]
        


# In[ ]:



     7) Print the name of all the columns.
       
        users.columns
        
        Index(['age', 'gender', 'occupation', 'zip_code'], dtype='object') 


# In[ ]:


get_ipython().set_next_input('8) How is the dataset indexed');get_ipython().run_line_magic('pinfo', 'indexed')
 
   users.index
     
 Int64Index([  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,
         ...
         934, 935, 936, 937, 938, 939, 940, 941, 942, 943],
        dtype='int64', name=u'user_id', length=943) 
     


# In[ ]:


get_ipython().set_next_input('9)  What is the data type of each column');get_ipython().run_line_magic('pinfo', 'column')

    users.dtypes
       
        
        age            int64
        gender        object
        occupation    object
        zip_code      object
        dtype: object
    


# In[ ]:



    10)  Print only the occupation column
    
   users.["occupation"]
  

    user_id
 1         technician
 2              other
 3             writer
 4         technician
 5              other
 6          executive
 7      administrator
 8      administrator
 9            student
10            lawyer
11             other
12             other
13          educator
14         scientist
15          educator
16     entertainment
17        programmer
18             other
19         librarian
20         homemaker
21            writer
22            writer
23            artist
24            artist
25          engineer
26          engineer
27         librarian
28            writer
29        programmer
30           student
      ...      
     914            other
     915    entertainment
     916         engineer
     917          student
     918        scientist
     919            other
     920           artist
     921          student
     922    administrator
     923          student
     924            other
     925         salesman
     926    entertainment
     927       programmer
     928          student
     929        scientist
     930        scientist
     931         educator
     932         educator
     933          student
     934         engineer
     935           doctor
     936            other
     937         educator
     938       technician
     939          student
     940    administrator
     941          student
     942        librarian
     943          student
Name: occupation, Length: 943, dtype: object 

 


# In[ ]:


get_ipython().set_next_input('11) How many different occupations are in this dataset');get_ipython().run_line_magic('pinfo', 'dataset')

     users["occupation"].value_counts().count()
    
    
    
            


# In[ ]:


get_ipython().set_next_input('12)  What is the most frequent occupation');get_ipython().run_line_magic('pinfo', 'occupation')
 
   
   users["occupation"].value_counts.sort_values(ascending=False).head()
                                           
   
   
   


# In[ ]:


13) DataFrame Info.
   
    users.describe()


# In[ ]:


14)  Describe all the columns
    

   users.describe(include="all")
 
       age        gender    occupation    zip_code
count     943.000000    943         943           943
unique    NaN            2           21           795
top       NaN            M         student       55414
freq      NaN           670          196           9
mean      34.051962     NaN          NaN          NaN
std       12.192740     NaN          NaN          NaN
min       7.000000      NaN          NaN          NaN
25%       25.000000     NaN          NaN          NaN
50%       31.000000     NaN          NaN          NaN
75%       43.000000     NaN          NaN          NaN
max       73.000000     NaN          NaN          NaN 
    
    


# In[ ]:


15) Summarize only the occupation column
    
    
   users.occupation.describe()
   
   count         943
   unique         21
   top       student
   freq          196
   Name: occupation, dtype: object
           
           


# In[ ]:


get_ipython().set_next_input('16) What is the mean age of users');get_ipython().run_line_magic('pinfo', 'users')
    
    
    round(users.age.mean())


# In[ ]:


get_ipython().set_next_input('17)  What is the age with least occurrence');get_ipython().run_line_magic('pinfo', 'occurrence')
    
    
   users.age.value_counts().tail()
   
       11    1
       10    1
       73    1
       66    1
        7     1
       Name: age, dtype: int64  
       
       
    


# In[ ]:




