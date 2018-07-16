<<<<<<< HEAD
import pandas as pd
pd.Series? 

#gives you an explanation of series data structure

animals = ["tiger", "bear", "moose"]
pd.Sereis(animals)


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], \
	index=['Store 1', 'Store 1', 'Store 2'])
df.head()
#this creates a table/dataframe

df = pd.read_csv()
#python is built to read datafiles and convert them into dataframes
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
#this skips the first numerical row and column that woudld
#have been authomatically added when python does read_csv

df.columns
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 
 #this renames the columns to someting more reader-friendly
=======
import pandas as pd
pd.Series? 

#gives you an explanation of series data structure

animals = ["tiger", "bear", "moose"]
pd.Sereis(animals)


>>>>>>> b2198fc90cc9c6430d13b14119bb247fa7e4fdb4
