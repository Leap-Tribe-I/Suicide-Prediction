# importing from src
from src.ModelEvaluation import evalModel

# sklearn module for tuning
from sklearn.model_selection import RandomizedSearchCV

# sklearn modules for model creation
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import StackingClassifier

# importing module
from scipy.stats import randint as sp_randint

# Run all model in one shot
def RandomizedSearch(X_train, X_test, y_train, y_test, accuracyDict):
    log_reg_mod_tuning(X_train, X_test, y_train, y_test, accuracyDict)
    tuneKNN(X_train, X_test, y_train, y_test, accuracyDict)
    tuneDT(X_train, X_test, y_train, y_test, accuracyDict)
    tuneRF(X_train, X_test, y_train, y_test, accuracyDict)
    tuneBoosting(X_train, X_test, y_train, y_test, accuracyDict)
    tuneBagging(X_train, X_test, y_train, y_test, accuracyDict)
    # tuneStacking(X_train, X_test, y_train, y_test, accuracyDict)

# tuning the logistic regression model with RandomizedSearchCV
def log_reg_mod_tuning(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning the Logistic Regression Model with RandomizedSearchCV\n")
    param_distributions = {"C": sp_randint(1,100),
                  "solver": ["newton-cg", "lbfgs", "sag"],
                  "multi_class": ["ovr", "multinomial"],
                  "max_iter": sp_randint(100,500)}
    random_search = RandomizedSearchCV(LogisticRegression(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    lr = random_search.best_estimator_
    y_pred_class = lr.predict(X_test)
    accuracy = evalModel(lr, X_test, y_test, y_pred_class)
    accuracyDict['Log_Reg_mod_tuning_RandomSearchCV'] = accuracy * 100

# tuning the KNN model with RandomizedSearchCV
def tuneKNN(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning KNN model with RandomizedSearchCV\n")
    param_distributions = {"n_neighbors": sp_randint(1,100),
                  "weights": ["uniform", "distance"],
                  "algorithm": ["auto", "ball_tree", "kd_tree", "brute"],
                  "leaf_size": sp_randint(10,100)}
    random_search = RandomizedSearchCV(KNeighborsClassifier(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    knn = random_search.best_estimator_
    y_pred_class = knn.predict(X_test)
    accuracy = evalModel(knn, X_test, y_test, y_pred_class)
    accuracyDict['KNN_tuning_RandomSearchCV'] = accuracy * 100

# tuning the Decision Tree model with RandomizedSearchCV
def tuneDT(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning Decision Tree model with RandomizedSearchCV\n")
    param_distributions = {"criterion": ["gini", "entropy"],
                  "max_depth": sp_randint(1,100),
                  "min_samples_split": sp_randint(2,10),
                  "random_state": [0]}
    random_search = RandomizedSearchCV(DecisionTreeClassifier(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    dt = random_search.best_estimator_
    y_pred_class = dt.predict(X_test)
    accuracy = evalModel(dt, X_test, y_test, y_pred_class)
    accuracyDict['Decision_Tree_tuning_RandomSearchCV'] = accuracy * 100

# tuning the Random Forest model with RandomizedSearchCV
def tuneRF(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning Random Forest model with RandomizedSearchCV\n")
    param_distributions = {"n_estimators": sp_randint(10,100),
                  "max_depth": sp_randint(1,100),
                  "min_samples_split": sp_randint(2,10),
                  "criterion": ["gini", "entropy"],
                  "random_state": [0]}
    random_search = RandomizedSearchCV(RandomForestClassifier(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    rf = random_search.best_estimator_
    y_pred_class = rf.predict(X_test)
    accuracy = evalModel(rf, X_test, y_test, y_pred_class)
    accuracyDict['Random_Forest_tuning_RandomSearchCV'] = accuracy * 100

# tuning boosting model with RandomizedSearchCV
def tuneBoosting(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning Boosting model with RandomizedSearchCV\n")
    param_distributions = {"n_estimators": sp_randint(10,100),
                  "learning_rate": [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                  "random_state": [0]}
    random_search = RandomizedSearchCV(AdaBoostClassifier(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    ada = random_search.best_estimator_
    y_pred_class = ada.predict(X_test)
    accuracy = evalModel(ada, X_test, y_test, y_pred_class)
    accuracyDict['AdaBoost_tuning_RandomSearchCV'] = accuracy * 100

# tuning bagging model with RandomizedSearchCV
def tuneBagging(X_train, X_test, y_train, y_test, accuracyDict):
    print("\nTuning Bagging model with RandomizedSearchCV\n")
    param_distributions = {"n_estimators": sp_randint(10,100),
                  "max_samples": [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                  "bootstrap": [True,False],
                  "bootstrap_features": [True,False],
                  "random_state": [0]}
    random_search = RandomizedSearchCV(BaggingClassifier(), param_distributions, n_jobs=-1, cv=5)
    random_search.fit(X_train,y_train)
    print("Best param_distributionss: ", random_search.best_params_)
    print("Best cross-validation score: ", random_search.best_score_*100, "%")
    print("Best estimator: ", random_search.best_estimator_)
    bag = random_search.best_estimator_
    y_pred_class = bag.predict(X_test)
    accuracy = evalModel(bag, X_test, y_test, y_pred_class)
    accuracyDict['Bagging_tuning_RandomSearchCV'] = accuracy * 100

# # tuning stacking model with RandomizedSearchCV
# def tuneStacking(X_train, y_train, X_test, y_test, accuracyDict):
#     # rf = RandomForestClassifier(n_estimators=20, random_state=1)
#     # ada = AdaBoostClassifier(n_estimators=20, learning_rate=0.1, random_state=1)
#     # bag = BaggingClassifier(n_estimators=20, max_samples=0.1, random_state=1)
#     # classifiers=[rf,ada,bag]
#     print("\nTuning Stacking model with RandomizedSearchCV\n")
#     param_distributions = {"n_estimators": sp_randint(10,100),
#                   "max_samples": [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
#                   "bootstrap": [True,False],
#                   "bootstrap_features": [True,False],
#                   "random_state": [0]}
#     random_search = RandomizedSearchCV(StackingClassifier(), param_distributions, n_jobs=-1, cv=5)
#     random_search.fit(X_train,y_train)
#     print("Best param_distributionss: ", random_search.best_params_)
#     print("Best cross-validation score: ", random_search.best_score_*100, "%")
#     print("Best estimator: ", random_search.best_estimator_)
#     stack = random_search.best_estimator_
#     y_pred_class = stack.predict(X_test)
#     accuracy = evalModel(stack, X_test, y_test, y_pred_class)
#     accuracyDict['Stacking_tuning_RandomSearchCV'] = accuracy * 100