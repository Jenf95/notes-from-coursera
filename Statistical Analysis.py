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


get_recession_bottom()

        
        

