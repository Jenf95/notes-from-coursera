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