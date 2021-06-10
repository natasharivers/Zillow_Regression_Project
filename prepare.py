import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

############################## PREP ZILLOW  ##############################

def prep_zillow(df):
    '''
    This function takes in the zillow df acquired by get_zillow
    Returns a cleaned zillow df.
    '''
    #create new column for tax_rate
    df['tax_rate'] =df['taxamount']/  df['taxvaluedollarcnt']
    
    #replace blank spaces and special characters
    df = zillow_df.replace(r'^\s*$', np.nan, regex=True)

    #drop null values- at most there were 9000 nulls (this is only 0.5% of 2.1M)
    df = df.dropna()
 
    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df


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

############################ Wrangle Zillow Function ##############################

def wrangle_zillow():
    '''
    This function checks to see if zillow.csv already exists, 
    if it does not, one is created
    then the data is cleaned and the dataframe is returned
    '''
    #check to see if telco_churn.csv already exist
    if os.path.isfile('zillow.csv'):
        zillow_df = pd.read_csv('zillow.csv', index_col=0)
    
    else:

        #creates new csv if one does not already exist
        zillow_df = get_zillow_data()
        zillow_df.to_csv('zillow.csv')

    #replace blank spaces and special characters
    zillow_df = zillow_df.replace(r'^\s*$', np.nan, regex=True)

    #drop null values- at most there were 9000 nulls (this is only 0.5% of 2.1M)
    zillow_df = zillow_df.dropna()

    return zillow_df