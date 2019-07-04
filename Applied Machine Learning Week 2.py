#KNearestNeighbors
#classification
from adspy_shared_utilities import plot_two_class_knn

X_train, X_test, y_train, y_test = train_test_split(X_C2, y_C2,random_state=0)

plot_two_class_knn(X_train, y_train, 1, 'uniform', X_test, y_test)
plot_two_class_knn(X_train, y_train, 3, 'uniform', X_test, y_test)
plot_two_class_knn(X_train, y_train, 11, 'uniform', X_test, y_test)

#regression
from sklearn.neighbors import KNeighborsRegressor
X_train, y_train, X_test, y_test = train_test_split(X_R1, y_R1, random_state=0)
knnreg = KNeighbrosRegressor (n_neighbors = 5).fit(X_train, y_train)
knnreg.predict(X_test)
print('R-squared test score:{:.3f}'.format(knnreg.score(X_test, y_test)))
''' the R-squared regression score, also known as 'coefficient of determination', measures
how well a prediction model for regression fits the given data; a score of 0 corresponds to a constant model,
whereas a score of 1 corresponds to perfect prediction'''

#Ridge Regression
from sklearn.linear_model import Ridge
X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state = 0)
linridge=Ridge(alpha=20.0).fit(X_train, y_train) 
'''
The influence of the regularization term is controled by alpha; higher alpha means more regularization
and simpler models
L2 penalty is the sum of squares for all the coefficients
Feature normalization technique: MinMax scaling(transform all the values to between 0 and 1)
'''
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
'''alternatively, we can use fit_transform()'''
X_train_scaled = scalter.fit_transform(X_train)
clf = Ridge().fit(X_train_scaled, y_train)
r2_score = clf.score(X_test_scaled, y_test)
'''the test set must use identical scaling to the training set'''

#Lasso Regression
'''
L1 penalty is to minimize the sum of the absolute values of the coefficients
This has the effect of setting parameter weights to zero for the least influential variables. It's called 
sparse solution: a kind of feature selection.
Parameter alpha in the function controls L1 penalty (default = 1.0)
Ridge vs. Lasso:
- Many small to medium sized effects: use Ridge
- Only a few variables with medium/large effect: Use Lasso
