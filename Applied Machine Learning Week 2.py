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
'''
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train, X_test, y_train, y_test = train_test_split(X_crime, y_crime, random_state = 0)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
linlasso = Lasso(alpha = 2.0, max_iter=10000).fit(X_train_scaled,y_train)
#increasing the max_iter value will increase the computation time accordingly; typically at least 20000
linear_model_intercept = linlasso.intercept_
linear_model_coefficient = linlasso.coef_
non_zero_features = np.sum(linlasso.coef_ != 0)
score_training = linlasso.score(X_train_scaled,y_train)
score_test = linlasso.score(X_test_scaled,y_test)

#Polynomial Features with Linear Regression
'''
- Generate new features consisting of all polynomial combinations of the original two features (x0, x1)
- the degree of the polynomial specifies how many variables participate at a time in each new feature
  (above example the degree would be 2)
- still a linear model, and can use the same least-squares estimation method for w and b
- why? to capture interactions between the original features by adding them as features to the linear model
- In practice, polynomial feature expansion is often combined with a regularized learning method like
  ridge regression
'''
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
X_train,y_train,X_test,y_test = train_test_split(X_F1, y_F1, random_state=0)
linreg = LinearRegression.fit(X_train, y_train)
poly = PolynomialFeatures(degree=2)
X_F1_poly = poly.fit_transform(X_F1)
X_train, y_train, X_test, y_test = train_test_split(X_F1_poly, y_F1, random_state=0)
linreg=LinearRegression.fit(X_train, y_train)

