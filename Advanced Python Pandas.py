import pandas as pd
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

answer = pd.merge(products_df, invoices_df, how="left", left_index="True", right_on="Product ID")


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



def answer_one():
    import pandas as pd
    import numpy as np

    energy = pd.read_excel("Energy Indicators.xls")
    energy = energy[16:243]
    energy = energy.drop(energy.columns[:2], axis=1)
    energy = energy.rename(columns = {"Environmental Indicators: Energy" : "Country", "Unnamed: 3" : "Energy Supply", "Unnamed: 4" : 
                                 "Energy Supply per Capita", "Unnamed: 5" : "% Renewable"})
    energy = energy.replace("...", np.nan)
    energy["Energy Supply"] = energy["Energy Supply"] * 1000000

    for country in energy["Country"]:
        if country[-1].isdigit() & country[-2].isdigit():
            energy = energy.replace(country, (country[:-2]))
        elif country [-1].isdigit():
            energy = energy.replace(country, (country[:-1]))
        else:
            False
    energy = energy.replace({"Republic of Korea" : "South Korea", "United States of America" : "United States", "United Kingdom of Great Britain and Northern Ireland" : "United Kingdom", "China, Hong Kong Special Administrative Region" : "Hong Kong" , 
                        "Bolivia (Plurinational State of)" : "Bolivia" , "Iran (Islamic Republic of)" : "Iran"})

    GDP = pd.read_csv("world_bank.csv")
    GDP =GDP[4:]
    GDP = GDP.replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep." : "Iran", "Hong Kong SAR, China":"Hong Kong"})

    ScimEn = pd.read_excel("scimagojr-3.xlsx")

    GDP = GDP.rename(columns = {"Unnamed: 48" : "2006" , "Unnamed: 49" : "2007" , "Unnamed: 50" : "2008" , "Unnamed: 51" : "2009" , 
                            "Unnamed: 52" : "2010" , "Unnamed: 53" : "2011" , "Unnamed: 54" : "2012"  ,"Unnamed: 55" : "2013",
                            "Unnamed: 56" : "2014","Unnamed: 57" : "2015"})
    GDP = GDP.drop(GDP.columns[58:], axis = 1)
    GDP = GDP.drop(GDP.columns[1:48], axis = 1)
    GDP = GDP.rename(columns = {"Data Source" : "Country"})

    df = pd.merge(energy, GDP, how="outer", left_on="Country", right_on = "Country")
    ANSWER = pd.merge(df, ScimEn, how = "outer", left_on="Country", right_on = "Country")
    ANSWER = ANSWER.sort_values(by="Rank")
    ANSWER = ANSWER[:15]
    ANSWER = ANSWER.set_index("Country")
    return ANSWER

answer_one()

#String Manipulation see notebook

def answer_three():
    def avg(row):
        data = row[["2006", "2007", "2008", "2009", "2010","2011","2012","2013","2014","2015"]]
        row["avgGDP"] = np.average(data)
        return row
    Top15 = ANSWER.apply(avg, axis = 1)
    Top15.sort_values(by="avgGDP", ascending = False)
    return Top15["avgGDP"]
answer_three()


import pandas as pd
import numpy as np

top15 = answer_one()
years = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]
average = (top15[years].mean(axis=1)).sort_values(ascending=False).rename('avgGDP')

def answer_three():
    return average



def answer_four():
    def max_minus_min(row):
        data = row[["2006", "2007", "2008", "2009", "2010","2011","2012","2013","2014","2015"]]
        row["delta_GDP"] = np.max(data) - np.min(data)
        return row
    Top15_1 = Top15.apply(max_minus_min, axis = 1)
     return top15_1.iloc[5]["delta_GDP"]
answer_four()


def answer_five():
    Top15 = answer_one()
    ans5 = Top15["Energy Supply per Capita"].mean()
    return ans5



def answer_six():
    Top15 = answer_one()
    x = (Top15["% Renewable"].idxmax(), Top15["% Renewable"].max())
    return x


def answer_seven():
    Top15 = answer_one()
    Top15["ratio"] = Top15["Self-citations"] / Top15["Citations"]
    y = (Top15["ratio"].idxmax(), Top15["ratio"].max())
    return y

 def answer_eight():
    Top15 = answer_one()
    Top15["Population"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"] 
    Top15 = Top15["Population"].sort_values(ascending=False)
    return Top15.index[2]


def answer_nine():
    Top15 = answer_one()
    Top15["Population"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    Top15["Citable docs per Capita"] = Top15["Citable documents"] / Top15["Population"]
    return Top15[["Energy Supply per Capita", "Citable docs per Capita"]].corr().ix["Energy Supply per Capita", "Citable docs per Capita"] 



def plot9():
    import matplotlib as plt
    %matplotlib inline
    
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


import pandas as pd
import numpy as np

def answer_ten():
    Top15 = answer_one()
    med = Top15["% Renewable"].median()
    Top15["HighRenew"] = Top15["% Renewable"] >= med
    Top15["HighRenew"] = Top15["HighRenew"].apply(lambda x:1 if x else 0)
    Top15.sort_values(by = "% Renewable", inplace=True)
    return Top15["HighRenew"]

def answer_eleven():
    Top15 = answer_one()
    ContinentDict = {'China':'Asia','United States':'North America','Japan':'Asia','United Kingdom':'Europe','Canada':'North America',
                    'Germany':'Europe','India':'Asia','France':'Europe','South Korea':'Asia','Italy':'Europe','Iran':'Asia','Spain':
                    'Europe','Australia':'Australia','Brazil':'South America'}
    eleven = pd.DataFrame(columns = ['size','sum','mean','std'])
    Top15["Population"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"] 
    for group, frame in Top15.groupby(ContinentDict):
        eleven.loc[group] = [len(frame), frame['Population'].sum(), frame['Population'].mean(),frame['Population'].std()]
    return eleven
#returns a dataframe with continent as index, and size(number of countries in the continent), pop sum, pop mean, pop standard deviation

def answer_twelve():
    Top15 = answer_one()
    Top15['bins']=pd.cut(Top15["% Renewable"], 5)
    ContinentDict = {'China':'Asia','United States':'North America','Japan':'Asia','United Kingdom':'Europe','Canada':'North America',
                    'Germany':'Europe','India':'Asia','France':'Europe','South Korea':'Asia','Italy':'Europe','Iran':'Asia','Spain':
                    'Europe','Australia':'Australia','Brazil':'South America','Russian Federation':'Europe'}
    Top15['Continent'] = [ContinentDict[country] for country in Top15.index]
    return Top15.groupby(['Continent','bins']).size()

answer_twelve()

def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst']=(Top15['Energy Supply']/Top15['Energy Supply per Capita']).astype(float)
    return Top15['PopEst'].apply(lambda x: '{0:,}'.format(x))
answer_thirteen()
#this put population numbers into numbers seperated by thousands seperator



#wrong stuff
def digit_sum(n):
  string = str(n)
  total = 0
  for digit in string:
    total = total + int(string(digit))
  return total
