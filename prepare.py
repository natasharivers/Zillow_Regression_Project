import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

############################## PREP ZILLOW  ##############################

def prep_zillow(df):
    '''
    This function takes in the zillow df acquired by get_zillow_file
    Returns a cleaned zillow df.
    '''
    #create new column for tax_rate
    df['tax_rate'] =(df['taxamount']/  df['taxvaluedollarcnt']) *100

    #change column names to be more legible
    df = df.rename(columns={"calculatedfinishedsquarefeet": "total_sqft", "bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", "taxvaluedollarcnt": "value_assessed", "taxamount": "tax_amount", "yearbuilt": "year_built", "fips": "county_code" })
    #replace blank spaces and special characters
    df = df.replace(r'^\s*$', np.nan, regex=True)

    #drop null values- at most there were 9000 nulls (this is only 0.5% of 2.1M)
    df = df.dropna()
 
    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df

############################## DROP OUTLIERS FUNCTION ##############################

def outlier_bound_calculation(df, variable):
    '''
    calcualtes the lower and upper bound to locate outliers in variables
    '''
    quartile1, quartile3 = np.percentile(df[variable], [25,75])
    IQR_value = quartile3 - quartile1
    lower_bound = quartile1 - (1.5 * IQR_value)
    upper_bound = quartile3 + (1.5 * IQR_value)
    '''
    returns the lowerbound and upperbound values
    '''
    return print(f'For {variable} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
    

############################## ZILLOW SPLIT ##############################

def zillow_split(df):
    '''
    This function take in get_zillow  from aquire.py and performs a train, validate, test split
    Returns train, validate, test dfs and prints out the shape of all three datasets
    '''
    #create train_validate and test datasets
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)
    #create train and validate datasets
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)

    # Have function print datasets shape
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
   
    return train, validate, test
