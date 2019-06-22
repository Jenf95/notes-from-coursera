import pandas as pd
import os
import numpy as np
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

purchase_4 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df1 = pd.DataFrame([purchase_4], \
	index=['Store 4'])

#print(df.loc[1:2,['Name','Item purchased']])
#print(df.loc[df.Name=='Kevyn'])
#print(df[df["Name"].apply(lambda x: x[:2] =='Ke')])
dictionary=df.to_dict()
dictionary1=dictionary['Name']
#print(dictionary1)
dictionary1['store 3']='Jack'
#print(dictionary1)

#path = "/mnt/document/haircare"
#os.chdir(path)

df['Name'].replace('Chris','Jack',inplace=True)
#print(df)
new = df[df['Name']=='Vinod']
#print(new)

name,counts = np.unique(df['Name'],return_counts=True)
#s=pd.DataFrame(t)
s = np.asarray((name,counts)).T
#print(s)

t=df.groupby('Name').agg({'Cost':np.sum})
#print(t)

#df.set_index('group').groupby(level=0)['pv'].agg({'sum':np.sum})

df=df.sort_values(by='Cost',ascending=False)
#rint(df)


merge=pd.concat([df,df1])
print(merge)

rows=merge.head(2)
print(rows)