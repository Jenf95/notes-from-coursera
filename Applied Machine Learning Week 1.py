%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table('food_data_with_colors.txt')

'''create a mapping from fruit label value to fruit name to make 
results easier to interpret'''
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(),fruits.fruit_name.unique()))

#CREATE TRAIN TEST SPLIT
X = fruits[['mass','width', 'height']]
y = fruits['fruit_label']
X_train,X_test, y_train, y_test = train_test_split(X,y,random_state = 0)
'''default is 75% / 25% train_test_split, x is features, y is labels