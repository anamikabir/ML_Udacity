#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for i in xrange(len(ages)):
        cleaned_data.append((ages[i],net_worths[i],abs(net_worths[i]-predictions[i])))
    cleaned_data = sorted(cleaned_data,key = lambda x:x[2])
    size_of_new_dataset = int(round(0.9*len(cleaned_data)))
    cleaned_data = cleaned_data[:size_of_new_dataset]
    return cleaned_data

