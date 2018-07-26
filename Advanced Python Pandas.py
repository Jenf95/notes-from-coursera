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
