# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import datetime 
from pandas import Series, DataFrame

def calculate_ret(df, col, log_r = False):
    """Takes in specified column of dataframe and calculates daily return

Parameters:
    
    df: dataframe
    
    col: column of dataframe that contains input to be calculated
    
    log_r: boolean, default False
        if False, returns daily return
        if True, returns log of daily return 
        """    
    
    if log_r == False:
        df['prevday']= df[col].shift(1)
        df['ret']= (df[col]-df['prevday'])
    else:
        df['prevday'] = df[col].shift(1)
        df['log_ret'] = np.log((df[col]-df['prevday']))
    
    df = df[1:]
    return df

#data = {'index':[0,1,2,3,4], 'py': [1.1, 1.3, 1.5, 1.6, 1.8]}
#frame = DataFrame(data)

#output =return_cal(frame, 'py', log_r = True)

#print (output)
#print(frame)

def dt_convert(dates, output = 'all'):
    """Takes in a list or series of date,
returns year or month or day of specified list or series. 
list or series must contain dates.
    
Parameters:
    
    dates: a list or series of dates
    
    output:  {'year', 'month', 'day'}, default = 'all'
            if 'year' is chosen, return year of each date in dates
            if 'month' is chosen, return month of each date in dates
            if 'day' is chosen, return month of each date in dates
            default returns a dict of year, month and day
        """
    dates = pd.to_datetime(dates, infer_datetime_format = True)
    if output == 'year':
        year = (dates).map(lambda x: int(x.strftime('%Y')))
        return year
    elif output == 'month':
        month = (dates).map(lambda x: int(x.strftime('%m')))
        return month 
    elif output == 'day': 
        day = (dates).map(lambda x: int(x.strftime('%d')))
        return day
    elif output == 'all':
        year = (dates).map(lambda x: int(x.strftime('%Y')))
        month = (dates).map(lambda x: int(x.strftime('%m')))
        day = (dates).map(lambda x: int(x.strftime('%d')))
        return {'year':year, 'month':month, 'day': day}


#data = {'date':['14 Sep 2019', '15 Sep 2019','16 Sep 2019','17 Sep 2019'],
#        'value': [1,2,3,4]}

#frame = DataFrame(data)

#data1 = ('14 Sep 2019', '15 Sep 2019','16 Sep 2019','17 Sep 2019')

#output = dt_convert(data1)
#print(output)

def count(list1, lower_limit, upper_limit):
    """"takes in a list or series, count and return the number of occurence
    where int or float elements fall between lower_limit and upper_limit.
    
Parameters:
    
    list1: list of series, elements must be int or float type
    
    lower limit: an int or float that represents the lower limit of the range
    
    upper_limit: an int or float that represents the upper limit of the range"""
        
    return len(list(x for x in list1 if lower_limit < x <= upper_limit))

#data = [0,1,2,3,4]
#print(count(data,1,3))

def prob(list1, lower_limit, upper_limit):
    """calculates the probability of an event falls between 
    the lower_limit and upper_limit given a statistical data, list1

Parameters:
    
    list1: list of series, elements must be int or float type
    
    lower limit: an int or float that represents the lower limit of the range
    
    upper_limit: an int or float that represents the upper limit of the range"""

    return count(list1, lower_limit, upper_limit)/ len(list1)

data = [0,1,2,3,4]
print(prob(data,1,3))


