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

def answer_two():
    cancerdf = answer_one()
    target_code = {0:'malignant',1:'benign'}
    target = cancerdf['target'].value_counts().rename(index=target_code)
    return target
#find the class distribution (This function should return a Series named target of length 2 with integer \
#values and index = ['malignant', 'benign'])

def answer_three():
    cancerdf = answer_one()
    X = cancerdf[cancerdf.columns[:-1]]
    y = cancerdf['target']   
    return X, y
#splits the dataframe into data and labels

from sklearn.model_selection import train_test_split
def answer_four():
    X, y = answer_three()
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)  
    return X_train, X_test, y_train, y_test

from sklearn.neighbors import KNeighborsClassifier
def answer_five():
    X_train, X_test, y_train, y_test = answer_four()
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)    
    return knn

def answer_six():
    cancerdf = answer_one()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    #above gets the mean value for each feature, ignores the target column, and reshapes the data from
    # one-dimensional to two, necessary for the predict methods of knn
    X_train, X_test, y_train, y_test = answer_four()
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    prediction = knn.predict(means)    
    return prediction
#predicts the class label using the mean value for each feature

def answer_seven():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    prediction = knn.predict(X_test)
    return prediction

def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    score = knn.score(X_test, y_test)   
    return score

#visualize the differet predicition scores between training and test sets, as well as malignant and benign cells
def accuracy_plot():
    import matplotlib.pyplot as plt

    %matplotlib notebook

    X_train, X_test, y_train, y_test = answer_four()

    # Find the training and testing accuracies by target value (i.e. malignant, benign)
    mal_train_X = X_train[y_train==0]
    mal_train_y = y_train[y_train==0]
    ben_train_X = X_train[y_train==1]
    ben_train_y = y_train[y_train==1]

    mal_test_X = X_test[y_test==0]
    mal_test_y = y_test[y_test==0]
    ben_test_X = X_test[y_test==1]
    ben_test_y = y_test[y_test==1]

    knn = answer_five()

    scores = [knn.score(mal_train_X, mal_train_y), knn.score(ben_train_X, ben_train_y), 
              knn.score(mal_test_X, mal_test_y), knn.score(ben_test_X, ben_test_y)]


    plt.figure()

    # Plot the scores as a bar chart
    bars = plt.bar(np.arange(4), scores, color=['#4c72b0','#4c72b0','#55a868','#55a868'])

    # directly label the score onto the bars
    for bar in bars:
        height = bar.get_height()
        plt.gca().text(bar.get_x() + bar.get_width()/2, height*.90, '{0:.{1}f}'.format(height, 2), 
                     ha='center', color='w', fontsize=11)

    # remove all the ticks (both axes), and tick labels on the Y axis
    plt.tick_params(top='off', bottom='off', left='off', right='off', labelleft='off', labelbottom='on')

    # remove the frame of the chart
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    plt.xticks([0,1,2,3], ['Malignant\nTraining', 'Benign\nTraining', 'Malignant\nTest', 'Benign\nTest'], alpha=0.8);
    plt.title('Training and Test Accuracies for Malignant and Benign Cells', alpha=0.8)