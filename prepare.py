import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler


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

def zillow_split(df, target):
    '''
    This function take in get_zillow  from aquire.py and performs a train, validate, test split
    Returns train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test
    and prints out the shape of train, validate, test
    '''
    #create train_validate and test datasets
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)
    #create train and validate datasets
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)

    #Split into X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]

    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]

    X_test = test.drop(columns=[target])
    y_test = test[target]

    # Have function print datasets shape
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
   
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test

############################## Plot Univariate ##############################


def explore_univariate(train, cat_vars, quant_vars):
    for var in cat_vars:
        explore_univariate_categorical(train, var)
        print('_________________________________________________________________')
    for col in quant_vars:
        p, descriptive_stats = explore_univariate_quant(train, col)
        plt.show(p)
        print(descriptive_stats)

############################## Plot Bivariate ##############################

def explore_bivariate(train, target, cat_vars, quant_vars):
    for cat in cat_vars:
        explore_bivariate_categorical(train, target, cat)
    for quant in quant_vars:
        explore_bivariate_quant(train, target, quant)

############################## PREP ZILLOW  ##############################

def final_prep_zillow(df):
    '''
    This function takes in the zillow df acquired by get_zillow_file,
    then the function removed outliers from bedrooms, bathrooms, value_assessed, and total_sqft
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
    
    q1_bed = df['bedrooms'].quantile(0.25)
    q3_bed = df['bedrooms'].quantile(0.75)
    iqr_bed = q3_bed - q1_bed
    lowerbound_bed = q1_bed - (1.5 * iqr_bed)
    upperbound_bed = q3_bed + (1.5 * iqr_bed)
    df= df[df.bedrooms > lowerbound_bed]
    df= df[df.bedrooms < upperbound_bed]

    q1_bath = df['bathrooms'].quantile(0.25)
    q3_bath = df['bathrooms'].quantile(0.75)
    iqr_bath = q3_bath - q1_bath
    lowerbound_bath = q1_bath - (1.5 * iqr_bath)
    upperbound_bath = q3_bath + (1.5 * iqr_bath)
    df= df[df.bathrooms > lowerbound_bath]
    df= df[df.bathrooms < upperbound_bath]

    q1_tax = df['value_assessed'].quantile(0.25)
    q3_tax = df['value_assessed'].quantile(0.75)
    iqr_tax = q3_tax- q1_tax
    lowerbound_tax = q1_tax - (1.5 * iqr_tax)
    upperbound_tax = q3_tax + (1.5 * iqr_tax)
    df= df[df.value_assessed > lowerbound_tax]
    df= df[df.value_assessed < upperbound_tax]

    q1_sqft = df['total_sqft'].quantile(0.25)
    q3_sqft = df['total_sqft'].quantile(0.75)
    iqr_sqft = q3_sqft - q1_sqft
    lowerbound_sqft = q1_sqft - (1.5 * iqr_sqft)
    upperbound_sqft = q3_sqft + (1.5 * iqr_sqft)
    df= df[df.total_sqft > lowerbound_sqft]
    df= df[df.total_sqft < upperbound_sqft]

    #drop duplicates
    df.drop_duplicates(inplace=True)
    
    return df

############################## Select K Best Function  ##############################

#X- features, y- target, k-#of features
def select_kbest(X,y,k): 
    f_selector = SelectKBest(f_regression, k)
    f_selector.fit(X, y)
    k_features = X.columns[f_selector.get_support()]

    return k_features

############################## RFE Function ##############################

def rfe(X, y, n):
    lm = LinearRegression()
    rfe = RFE(lm, n)
    rfe.fit(X, y)
    
    n_features = X.columns[rfe.support_]
    
    return n_features

############################## MinMaxScaler Function ##############################


def min_max_scaler(X_train, X_validate, X_test, numeric_cols):
    """
    this function takes in 3 dataframes with the same columns,
    a list of numeric column names (because the scaler can only work with numeric columns),
    and fits a min-max scaler to the first dataframe and transforms all
    3 dataframes using that scaler.
    it returns 3 dataframes with the same column names and scaled values.
    """
    # create the scaler object and fit it to X_train (i.e. identify min and max)
    # if copy = false, inplace row normalization happens and avoids a copy (if the input is already a numpy array).
    scaler = MinMaxScaler(copy=True).fit(X_train[numeric_cols])
    # scale X_train, X_validate, X_test using the mins and maxes stored in the scaler derived from X_train.
    #
    X_train_scaled_array = scaler.transform(X_train[numeric_cols])
    X_validate_scaled_array = scaler.transform(X_validate[numeric_cols])
    X_test_scaled_array = scaler.transform(X_test[numeric_cols])
    # convert arrays to dataframes
    X_train_scaled = pd.DataFrame(X_train_scaled_array, columns=numeric_cols).set_index(
        [X_train.index.values]
    )
    X_validate_scaled = pd.DataFrame(
        X_validate_scaled_array, columns=numeric_cols
    ).set_index([X_validate.index.values])
    X_test_scaled = pd.DataFrame(X_test_scaled_array, columns=numeric_cols).set_index(
        [X_test.index.values]
    )
    # Overwriting columns in our input dataframes for simplicity
    for i in numeric_cols:
        X_train[i] = X_train_scaled[i]
        X_validate[i] = X_validate_scaled[i]
        X_test[i] = X_test_scaled[i]
    return X_train, X_validate, X_test