import panda as pd
df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
                  
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})


#inner join and outer join
#you have a student df and staff df both with names as indeces
pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
#above is performing a union
pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
#above is performing an intersection
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
#above gets a list of all staff, regardless if they are students
#above is called a left join
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
#above is a right join to get a list of all students
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
#above is doing join by column
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])

answer = pd.merge(products_df, invoices_df, how="left", Left_index="True", Right_on="Product ID")


#Pandas Idioms
(df.where(df['SUMLEV']==50)
    .dropna()
    .set_index(['STNAME','CTYNAME'])
    .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})
df.apply(min_max, axis=1)
#be careful axis =1 here because it's applying new data to index
import numpy as np
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row
df.apply(min_max, axis=1)
#above cleans data and add new column to the dataframe
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']
df.apply(lambda x: np.max(x[rows]), axis=1)
#more reader-friendly code using lambda


#Group Functions
for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))
#or you can use groupby, which is faster
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))
#provide a function to groupby
df = df.set_index('STNAME')

def fun(item):
    if item[0]<'M':
        return 0
    if item[0]<'Q':
        return 1
    return 2

for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')

df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
#above built a summary datafram fro the average pop for state
#we gave agg a dictionary with census2010pop key and avrg function
def totalweight(df, w, q):
    return sum(df[w] * df[q])
print(df.groupby('Category').apply(totalweight, 'Weight (oz.)', 'Quantity'))
#this function renders weight by category

(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
    .agg({'avg': np.average, 'sum': np.sum}))
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'avg': np.average, 'sum': np.sum}))
#above creates a heirarchical dataframe


#Scales
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
#above turns it into nominal then ordinal data that we can perform boolean mask on
grades > 'C'

s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype("category", categories = ["Low", "Medium", "High"],ordered=True)

#reducing ratio scale to ordinal scale
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10)
#putting a series into 3 bins and label then
pd.cut(s, 3)
pd.cut(s, 3, labels = ["small", "medium", "large"])


#pivot table
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
#to compare the makes of electric viehcles versus the years in terms of batttery capacity

#Create a pivot table that shows the price and rating for every 
#'Manufacturer' / 'Bike Type' combination.
Bikes.pivot_table(values=["Price","Rating"], index=["Manufacturer","Bike Type"], columns="mean", aggfunc=np.mean)
#above is invalid code, find out why
print(pd.pivot_table(Bikes, index=['Manufacturer','Bike Type']))

df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)





pd.Timestamp('9/1/2016 10:05AM')
pd.Period('1/2016') #return Period('2016-01', 'M')
pd.Period('3/5/2016') #return Period('2016-03-05', 'D')
#datetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
#will return a, b, and c next to the timestamps

#periodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
# will return Freq: M, dtype: object

ts3.index = pd.to_datetime(ts3.index) #put time in a standard format (ts3 is a df)
pd.to_datetime('4.7.12', dayfirst=True) #will return Timestamp('2012-07-04 00:00:00'
#timedeltas
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016') #return Timedelta('2 days 00:00:00')
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H')

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN') #occur 9 times, bi-weekly every sunday

df.diff() #the difference between each value across index

df.asfreq('W', method='ffill') #change frequency to weekly from bi-weekly, forward fill missing values


