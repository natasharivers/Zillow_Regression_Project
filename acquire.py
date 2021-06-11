
#import libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# acquire
from env import host, user, password

######################### URL Connection Function ###########################

def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

############################ Acquire Zillow Function ##############################

def get_zillow():
    '''
    This function reads in the Zillow data from the Codeup db
    with properties_2017, predictions_2017 and propertylandusetype tables joined
    returns: a pandas DataFrame 
    '''
    
    zp_query = '''
    SELECT calculatedfinishedsquarefeet, bedroomcnt, bathroomcnt, taxvaluedollarcnt, taxamount, yearbuilt, fips
    FROM properties_2017
    JOIN predictions_2017 ON properties_2017.parcelid = predictions_2017.parcelid
    JOIN propertylandusetype ON properties_2017.propertylandusetypeid= propertylandusetype.propertylandusetypeid
    WHERE predictions_2017.transactiondate BETWEEN '2017-05-01' AND '2017-08-31' AND properties_2017.propertylandusetypeid IN (31, 46, 47, 260, 261, 262, 263, 264, 265, 268, 273, 274, 275, 276, 279);
    '''
    return pd.read_sql(zp_query, get_connection('zillow'))