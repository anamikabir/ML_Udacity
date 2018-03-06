#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter(salary,bonus)
    """ 
    if bonus>maxbon:
        maxbon=bonus
        temp = point
print temp
"""
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

#temp = sorted(data,key= lambda x: x[1])
#print temp
"""
desired_Sal = raw_input("Enter salayr: ")

for k,v in data_dict.iteritems():
    if v['salary']==int(desired_Sal):
        print k

"""
temp = sorted(data_dict.iteritems(),key=lambda (k,v): (v['salary'],k))
for k,v in temp:
    if v['salary']!='NaN':
        print k, v['salary']
