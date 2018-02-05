#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
"""
#Training smaller dataset
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
C_val = float(raw_input("Enter value for C: "))
print C_val
"""

from sklearn import svm
clf = svm.SVC(kernel='rbf',C=10000.0)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

#print str(pred[10])+ "\t" + str(pred[26]) + "\t" + str(pred[50])
count =0
for p in pred:
    if p == 1:
        count +=1

print count 

from sklearn.metrics import accuracy_score

print accuracy_score(pred,labels_test)

#########################################################


