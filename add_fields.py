#!/usr/bin/env python
# coding: utf-8

# In[366]:


path = "/Users/daniel-new2/sites/daniel_py/data/"


# In[367]:


import pandas as pd
import os


# In[368]:


pd.set_option('display.max_rows', 10)


# In[369]:


def get_files_in_directory():
    dir_list = os.listdir(path)
    if '.DS_Store' in dir_list: dir_list.remove('.DS_Store')
    return dir_list
 
def create_data_frame(file):
    df = pd.read_csv(path + file)
    return df

def add_to_big_data_frame(new_data):
    big_data_length = len(df)
    big_data.loc[big_data_length] = new_data
    


# In[370]:


test_data = [['cash', 'us-chone']]
 
# Create the pandas DataFrame
big_data = pd.DataFrame(data, columns = ['field', 'fact_type'])
 
# print dataframe.
display(big_data)

bd = []


# In[381]:


files = get_files_in_directory() 
print("Files Found:" , len(files), "\n")
for file in files:
    fields = pd.read_csv(path + file) # read CSV
    fields_df = pd.DataFrame(fields)  # make a Data Frame
    relevant_fields = fields_df.loc[:, ["field", "fact_type"]]  #include columns
    print( "Fields Found", len(relevant_fields) )
    
    unique_fields = relevant_fields.groupby(['field', 'fact_type'], as_index=False).first()  #remove duplicates
    #display(unique_fields)
    
    print( "Unique Fields Found", len(unique_fields), "\n" )
    big_data = pd.concat([big_data, unique_fields])
    
print("Total Fields Found:" , len(big_data))
#print(type(big_data))
big_unique_fields = big_data.groupby(['field', 'fact_type'], as_index=False).first()  #remove duplicates
print("Total Unique Fields Found:" , len(big_unique_fields))


# In[382]:


#import sqlalchemy
#engine = create_engine("mysql:///?User=myUser&;Password=myPassword&Database=NorthWind&Server=myServer&Port=3306")


# In[ ]:


#engine = create_engine("mysql+pymysql://root:solaR3625@some_mariadb/finfresh?charset=utf8mb4")
#my_conn = create_engine("mysql+mysqldb://root:solaR3625@localhost/finfresh")

