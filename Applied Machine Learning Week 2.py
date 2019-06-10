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
whereas a score of 1 corresponds to perfect prediction