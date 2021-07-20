#suicide prediction program
'''
suicide prediction program is working 
            but 
will take time so dont quit in middle
'''
#ignore warnings
import warnings
warnings.filterwarnings("ignore")
# import modules

#importing src moduls
import src.dataCleaningEncoding as dt
import src.dataSplit as spl 
import src.correlationMatrix as cm
import src.dataFeaturing as ft
import src.tuningGrid as gcv
import src.modelEvaluator as ev
import src.tuningRand as rcv
import src.accuracyPlot as ap

#importing basic python libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
import json

# data loading
#enter the location of your input file

input_location = input("Enter your input file location: ")

# check if the file exists
while not os.path.isfile(input_location):
    print("File does not exist")
    exit()

# Check input and read file
if(input_location.endswith(".csv")):
    data = pd.read_csv(input_location)
elif(input_location.endswith(".xlsx")):
    data = pd.read_excel(input_location)
else:
    print("ERROR: File format not supported!")
    exit()

#calling dataMagic function from src.data_cleaning_encoding to clean and encode the data
data = dt.dataMagic(data)

cm.corrMat(data)
#calling the datasplit function from src.data_split to split our data into training and testing sets
#returning the independent and dpendent variables and storing the below
X, y, X_train, X_test, y_train, y_test = spl.datasplit(data)
ft.findFeature(X, y)

#Creating a dictionary to store accuracy score of different algorithms
accuracyDict = {}

#Calling prediction algorithms from src.tuned_algos and passing training data to train the algo and testing
#data to test and rate the accuracy of the algorithm
#calling LogisticRegression with GridSearchCV
gcv.log_reg_mod_tuning(X_train, X_test, y_train, y_test, accuracyDict)
#K nearest neighbour with GridSearchCV
gcv.tuneKNN(X_train, X_test, y_train, y_test, accuracyDict)
#Decision tree with GridSearchCV
gcv.tuneDTree(X_train, X_test, y_train, y_test, accuracyDict)
#Random Forrest with GridSearchCV
gcv.tuneRF(X_train, X_test, y_train, y_test, accuracyDict)
# Boosting with GridSearchCV
gcv.boosting(X_train, X_test, y_train, y_test, accuracyDict)
# Boosting with GridSearchCV
gcv.bagging(X_train, X_test, y_train, y_test, accuracyDict)


#calling functions from src.randomized_searchCV_algos and passing training data to train the algo and testing
#data to test and rate the accuracy of the algorithm
# LogisticRegression with randomizedCV
rcv.log_reg_mod_tuning_rand(X_train, X_test, y_train, y_test, accuracyDict)
# K Nearest neighbour with randomizedCV
rcv.tuneKNN_rand(X_train, X_test, y_train, y_test, accuracyDict)
# Decision Tree with randomizedCV
rcv.tuneDTree_rand(X_train, X_test, y_train, y_test, accuracyDict)
# Random Forest with randomizedCV
rcv.tuneRF_rand(X_train, X_test, y_train, y_test, accuracyDict)
# Boosting with randomizedCV
rcv.boosting_rand(X_train, X_test, y_train, y_test, accuracyDict)
# Bagging with randomizedCV tuning implemented
rcv.bagging_rand(X_train, X_test, y_train, y_test, accuracyDict)

#printing the accuracyDict containing accuracy scores of different algorithms
print("accuracyDict:\n")
print(json.dumps(accuracyDict, indent=1))

#calling accuracy_graph function from src.accuracy_plot to plot the accuracy scores of different algorithms
ap.accuracy_graph(accuracyDict)