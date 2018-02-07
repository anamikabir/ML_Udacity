#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#number_of_people
print len(enron_data)

#number of features
#print len(enron_data[enron_data.keys()[0]])
print str(enron_data.itervalues().next())


"""
#number of people of interest
count = 0
for psn,attr in enron_data.iteritems():
    if attr["poi"]==1:
        count +=1
print count
"""

name = raw_input("Enter name: ")
namestr = name.split()
finalname = namestr[-1]+" "+" ".join(namestr[:-1])
finalname = finalname.upper()
feature = raw_input("Enter feature: ")

try:
    #print enron_data["PRENTICE JAMES"]["total_stock_value"]
    print enron_data[finalname][feature]

except:
    print "Error"

