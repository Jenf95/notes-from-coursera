%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits = pd.read_table('food_data_with_colors.txt')

'''create a mapping from fruit label value to fruit name to make 
results easier to interpret'''
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(),fruits.fruit_name.unique()))


#PLOTTING A SCATTER MATRIX
from matplotlib import cm
X = fruits[['height','width','mass','color_score']]
y = fruits['fruit_label']
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)
cmap = cm.getcmap('gnuplot')
scatter = pd.scatter_matrix(X_train,c=y_train,marker = 'o', s=40, hist_kwds = {'bins':15},figsize=(9,9), cmap=cmap)

#PLOTTIING A 3D SCATTER PLOT
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(X_train['width'],X_train['height'], X_train['color_score'],c=y_train,marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()

#CREATE TRAIN TEST SPLIT
X = fruits[['mass','width', 'height']]
y = fruits['fruit_label']
X_train,X_test, y_train, y_test = train_test_split(X,y,random_state = 0)
'''default is 75% / 25% train_test_split, x is features, y is labels'''

#CREATE CLASSIFIER OBJECT
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
#TRAIN THE CLASSIFIER (FIT THE ESTIMATOR) USING THE TRAINING DATA
knn.fit(X_train, y_train)
#ESTIMATE THE ACCURACY OF THE CLASSIFIER ON FUTURE DATA, USING THE TEST DATA
knn.score(X_test, y_test)

#PREDICT UNSEEN OBJECTS
fruit_prediction - knn.predict([[20,4.3,5.5]])
lookup_fruit_name[fruit_prediction[0]]



#------------------------------------------#
#HOMEWORK
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer.DESCR)

def answer_one():
    columns_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
               'mean smoothness', 'mean compactness', 'mean concavity',
               'mean concave points', 'mean symmetry', 'mean fractal dimension',
               'radius error', 'texture error', 'perimeter error', 'area error',
               'smoothness error', 'compactness error', 'concavity error',
               'concave points error', 'symmetry error', 'fractal dimension error',
               'worst radius', 'worst texture', 'worst perimeter', 'worst area',
               'worst smoothness', 'worst compactness', 'worst concavity',
               'worst concave points', 'worst symmetry', 'worst fractal dimension']
    df_cancer = pd.DataFrame(cancer['data'],index=pd.RangeIndex(start=0, stop=569, step=1), columns = columns_names)
    df_cancer['target']=pd.DataFrame(cancer['target'])
    return df_cancer
#convert the sklearn.dataset cancer to a dataframe
#you don't need to convert to a pd dataframe to train a sklearn model, but it is easier for data munging



