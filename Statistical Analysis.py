np.random.binomial(1,0.5)


#sampling the distribution
chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)    
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1
print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))

#calculate standard deviation
np.std(distribution)

import scipy.stats as stats
distribution = np.random.normal(0.75,size=1000)
stats.kurtosis(distribution)
#a negative means slightly more flat than a normal distribution
#a positive values means the curve is slightly more peaky than a normal distribution

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)

from scipy import stats
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
#compare two independent samples to see if they have different means


#Assignment: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean 
      #price of the houses in university towns the quarter before the recession starts compared to the receccion bottom 
      #(price_ratio = quarter_before_recession/recession_bottom
        
def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    university_towns = []
    state = None
    towns = [] 
    file = open('university_towns.txt',"r")
    for line in file:
        new_line = line[:-1]
        if new_line[-6:] == '[edit]':
            state = new_line[:-6]
            continue
        if '(' in line:
            town = new_Line[:thisLine.index('(')-1]
            towns.append([state,town])
        else:
            town = new_line
            towns.append([state,town])
    university_towns = pd.DataFrame(towns, columns = ['State','RegionName'])
    return university_towns

get_list_of_university_towns()

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    #use chained value in 2009 dollars, only look from 2000q1
    #A recession is defined as starting with two consecutive quarters of GDP decline, 
    #and ending with two consecutive quarters of GDP growth.
    gdp = pd.read_excel("gdplev.xls")
    gdp = gdp[219:]
    gdp = gdp.drop(gdp.columns[:4], axis = 1 )
    gdp = gdp.drop(gdp.columns[1], axis = 1)
    gdp = gdp.drop(gdp.columns[2], axis = 1)
    gdp = gdp.rename(columns = {"Unnamed: 4":"Year/Quarter", "Unnamed: 6" : "GDP in chained 2009 values"})
    recession_start = []   
    for i in range(2,len(gdp)):
        if gdp.iloc[i-2][1] > gdp.iloc[i-1][1] and gdp.iloc[i-1][1] > gdp.iloc[i][1]:
            recession_start.append(gdp.iloc[i-2]["Year/Quarter"])      
    return recession_start[0]
get_recession_start()

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    gdp = pd.read_excel("gdplev.xls")
    gdp = gdp[219:]
    gdp = gdp.drop(gdp.columns[:4], axis = 1 )
    gdp = gdp.drop(gdp.columns[1], axis = 1)
    gdp = gdp.drop(gdp.columns[2], axis = 1)
    gdp = gdp.rename(columns = {"Unnamed: 4":"Year/Quarter", "Unnamed: 6" : "GDP in chained 2009 values"})
    recession_end = []   
    for i in range(len(gdp)-2):
        if gdp.iloc[i][1] < gdp.iloc[i+1][1] and gdp.iloc[i+1][1] < gdp.iloc[i+2][1]:
            recession_start.append(gdp.iloc[i+2]["Year/Quarter"])      
    return recession_end[2]
get_recession_end()


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    #A recession bottom is the quarter within a recession which had the lowest GDP
    gdp = pd.read_excel("gdplev.xls")
    gdp = gdp[219:]
    gdp = gdp.drop(gdp.columns[:4], axis = 1 )
    gdp = gdp.drop(gdp.columns[1], axis = 1)
    gdp = gdp.drop(gdp.columns[2], axis = 1)
    gdp = gdp.rename(columns = {"Unnamed: 4":"Year/Quarter", "Unnamed: 6" : "GDP in chained 2009 values"})
    gdp = gdp[33:40]
    bottom = gdp.iloc[4][0]
    return bottom


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    housing_price = pd.read_csv("City_Zhvi_AllHomes.csv")
    housing_price = housing_price.drop(["RegionID", 'Metro', 'CountyName','SizeRank'], axis = 1)
    housing_price['State'] = housing_price['State'].map(states)
    housing_price.set_index(['State','RegionName'],inplace = True)
    housing_price = housing_price.drop(housing_price.columns[0:45], axis = 1)
    housing_price.columns = pd.to_datetime(housing_price.columns).to_period(freq="M")
    housing_price = housing_price.groupby(housing_price.columns.asfreq("Q"),axis=1).mean() #group months by quarter and get average
    housing_price.columns=housing_price.columns.to_series().astype(str) #change column name from period index to string
    housing_price.columns = housing_price.columns.str.lower()
    return housing_price

convert_housing_data_to_quarters()


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    recession_price = convert_housing_data_to_quarters().loc[:,["2008q3","2009q4"]]
    recession_price.columns = ["Start","Bottom"]
    recession_price["Ratio"] = recession_price.Start / recession_price.Bottom 
    recession_price = recession_price.dropna(axis=0,how="any")
    college = get_list_of_university_towns().set_index(["State","RegionName"])
    college["isUnv"] = "Yes"
    result = pd.merge(recession_price,college,how="left",left_index=True,right_index=True)
    result.isUnv = result.isUnv.fillna("No")

    result_u = result[result.isUnv == "Yes"].Ratio
    result_n = result[result.isUnv == "No"].Ratio
    #print(res_n)
    _,p = stats.ttest_ind(result_u,result_n)
    different = (True if p < 0.01 else False)
    better = ("university town" if np.nanmean(result_u) < np.nanmean(result_n) else "non-university town")
    return different, p, better

run_ttest()