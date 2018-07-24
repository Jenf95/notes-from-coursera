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

 #Querying data using boolean mask
 df['Gold'] > 0 #this creats a boolean mask
 only_gold = df.where(df['Gold'] > 0) #overlayig with original
 #daraframe
 only_gold = only_gold.dropna() #dropping NaNs

 only_gold = df[df['Gold'] > 0] 
 #a more concise way to write the block above this code


 #Indexing Dataframes
df['country'] = df.index
df = df.set_index('Gold') 
#settimg index to number of gold medal won
df = df.reset_index()
#creats an actual column of index

df = pd.read_csv('census.csv')
df['SUMLEV'].unique()
#this function returns the two unique value in this column
df=df[df['SUMLEV'] == 50]
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df = df.set_index(['STNAME', 'CTYNAME'])
#you can set multiple indexes

df.head() #this gives you the first 5 rows of the data

df.loc['Michigan', 'Washtenaw County']
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne Counnty')] ]

df.loc[df['Gold'] > 0]

 new_set = df.where((df.loc[:,"Gold"] > 0) & (df.loc[:,"Gold.1"] > 0))

 #using groupby
 unique_counties = df.groupby("STNAME")['COUNTY'].nunique()


q6 = census_df
q6 = q6.set_index([ "STNAME", "CTYNAME"])
s = q6["CENSUS2010POP"]
s.groupby(level = "STNAME").nlargest(3)
#returns a series not a dataframe


#Pandas Intro
df.head()
df.tail()
copy_df = df.copy() #copying the dataframe
df.index
df.columns
df.values
df.describe() # a quick statistic summary of your data
df.T #swtiching columns and rows
df.sort_index(axis = 1, ascending=False) #sorting by an axis
df.sort_values(by="CENSUS2010POP") #ascending sort
df["STNAME"] or df."STNAME" #selects a column, which yields s Series
df[0:3] #or you can slice by lable, slices rows


def answer_six():
    copy_df = census_df.copy()
    copy_df = copy_df.groupby(['STNAME'])
    states_pop = pd.DataFrame(columns=['pop'])
    for i, c in copy_df:
        states_pop.loc[i] = [c.sort_values(by='CENSUS2010POP', ascending=False)[1:4]['CENSUS2010POP'].sum()]
    top3 = states_pop.nlargest(3,'pop')
    return list(top3.index)

answer_six()