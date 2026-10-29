from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.model_selection import KFold, cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import LeaveOneOut, LeavePOut, ShuffleSplit


# data = datasets.load_wine(as_frame = True)
# print(data)

# X = data.data
# y = data.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 22)

# dtree = DecisionTreeClassifier(random_state = 22)
# dtree.fit(X_train,y_train)

# y_pred = dtree.predict(X_test)

# print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred = dtree.predict(X_train)))
# print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred = y_pred))

# estimator_range = [2,4,6,8,10,12,14,16]

# models = []
# scores = []

# for n_estimators in estimator_range:
#     clf = BaggingClassifier(n_estimators = n_estimators, random_state = 22)
#     clf.fit(X_train, y_train)
#     models.append(clf)
#     scores.append(accuracy_score(y_true = y_test, y_pred = clf.predict(X_test)))


# plt.figure(figsize=(9,6))
# plt.plot(estimator_range, scores)

# plt.xlabel("n_estimators", fontsize = 18)
# plt.ylabel("score", fontsize = 18)
# plt.tick_params(labelsize = 16)

# plt.show()

# oob_model = BaggingClassifier(n_estimators = 12, oob_score = True,random_state = 22)
# oob_model.fit(X_train, y_train)
# print("the result: ",oob_model.oob_score_)

# plt.figure(figsize=(30, 20))
# plot_tree(oob_model.estimators_[0], feature_names = X.columns)
# plt.show()

# X, y = datasets.load_iris(return_X_y=True)
# clf = DecisionTreeClassifier(random_state=42)

# k_folds = KFold(n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = k_folds)

# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

### K-Stratified fold
# sk_folds = StratifiedKFold(n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = sk_folds)

# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

### LeaveOneOut
# loo = LeaveOneOut()
# scores = cross_val_score(clf, X, y, cv = loo)

# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

### LeavePOut

# lpo = LeavePOut(p=2)
# scores = cross_val_score(clf, X, y, cv = lpo)

# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

### Shuffle Split

# ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits = 5)
# scores = cross_val_score(clf, X, y, cv = ss)

# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve

# n = 10000
# ratio = .95
# n_0 = int((1-ratio) * n)
# n_1 = int(ratio * n)
# y = np.array([0] * n_0 + [1] * n_1)

# # below are the probabilities obtained from a hypothetical model that always predicts the majority class
# # probability of predicting class 1 is going to be 100%
# y_proba = np.array([1]*n)
# y_pred = y_proba > .5

# print(f'accuracy score: {accuracy_score(y, y_pred)}')
# cf_mat = confusion_matrix(y, y_pred)
# print('Confusion matrix')
# print(cf_mat)
# print(f'class 0 accuracy: {cf_mat[0][0]/n_0}')
# print(f'class 1 accuracy: {cf_mat[1][1]/n_1}')

# y_proba_2 = np.array(
#     np.random.uniform(0, .7, n_0).tolist() +
#     np.random.uniform(.3, 1, n_1).tolist()
# )
# y_pred_2 = y_proba_2 > .5

# print(f'accuracy score: {accuracy_score(y, y_pred_2)}')
# cf_mat = confusion_matrix(y, y_pred_2)
# print('Confusion matrix')
# print(cf_mat)
# print(f'class 0 accuracy: {cf_mat[0][0]/n_0}')
# print(f'class 1 accuracy: {cf_mat[1][1]/n_1}')

n = 10000
y = np.array([0] * n + [1] * n)

y_prob_1 = np.array(
    np.random.uniform(.25, .5, n//2).tolist() +
    np.random.uniform(.3, .7, n).tolist() +
    np.random.uniform(.5, .75, n//2).tolist()
)

y_prob_2 = np.array(
    np.random.uniform(0, .4, n//2).tolist() +
    np.random.uniform(.3, .7, n).tolist() +
    np.random.uniform(.6, 1, n//2).tolist()
)

print(f'model 1 accuracy score: {accuracy_score(y, y_prob_1>.5)}')
print(f'model 2 accuracy score: {accuracy_score(y, y_prob_2>.5)}')

print(f'model 1 AUC score: {roc_auc_score(y, y_prob_1)}')
print(f'model 2 AUC score: {roc_auc_score(y, y_prob_2)}')