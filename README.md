# Zillow Regression Project

_____________________________________________________________________________
___________________________________________________________________________________

## Goals:

- Predict the values of single unit properties based on sold data from May-August of 2017
- Identify the county & state where the properties are located in addition to the distribution of property tax rates

___________________________________________________________________________________
___________________________________________________________________________________

## Planning:

my TRELLO board is available at link:https://trello.com/b/m1beSkWz/zillow-regression-project


___________________________________________________________________________________
___________________________________________________________________________________


## Data Dictionary:

| Target          |       Datatype          |    Definition                      |
|-----------------|-------------------------|:----------------------------------:|
| value_assessed  | 28391 non-null: float64 | assessed value of homes in dataset | 


| Feature                 |       Datatype         |    Definition               |
|-------------------------|------------------------|:---------------------------:|
|total_sqft               |28321 non-null: float64 |total calculated square feet |
|bedrooms                 |28392 non-null: float64 |number of bedrooms           |
|bathrooms                |28392 non-null: float64 |number of bathrooms          |
|tax_amount               |28391 non-null: float64 |tax amount                   |
|year_built               |28298 non-null: float64 |year the property was built  |
|county_code              |28392 non-null: float64 |county code                  |
|parcelid                 |28392 non-null: int64   |unique property id           |
|tax_rate                 |28390 non-null: float64 |created column for taxrate   |

___________________________________________________________________________________
___________________________________________________________________________________

## county_code Dictionary:

| Fips Code  |     State    |    County    |                      
|:-----------|:-------------|:-------------|
| 6037       | California   | Los Angeles  |
| 6059       | California   | Orange       |
| 6111       | California   | Ventura      |

___________________________________________________________________________________
___________________________________________________________________________________

## Questions & Hypothesis:

### Key Questions:

- Is there a relationship between the assessed value of a single unit properties and the number of bedrooms?
- Is there a relationship between the assessed value of a single unit properties and the number of bathrooms?
- Is there a relationship between the assessed value of a single unit properties and the total square feet?
- Is there a relationship between the assessed value of a single unit properties and the tax amount?

### Hypothesis:

#### Hypothesis 1:
- **Null Hypothesis**: There is no relationship between value_assessed and bedroom count
    - value_assessed != bedroom count
- **Alternate Hypothesis**: There is a relationship between value_assessed and bedroom count
    - value_assessed == bedroom count

<br>

#### Hypothesis 2:
- **Null Hypothesis**: There is no relationship between value_assessed and number of bathrooms
    - value_assessed != bathroom count
- **Alternate Hypothesis**: There is a relationship between value_assessed and number of bathrooms
    - value_assessed == bathroom count

<br>

#### Hypothesis 3:
- **Null Hypothesis**: There is no relationship between value_assessed and total_sqft
    -  value_assessed != total_sqft 
- **Alternate Hypothesis**: There is a relationship between value_assessed and total_sqft 
    - value_assessed == total_sqft 

<br>

#### Hypothesis 4:
- **Null Hypothesis**: There is no relationship between value_assessed and tax_amount
    - value_assessed != tax_amount
- **Alternate Hypothesis**: There is a relationship between value_assed and tax_amount
    - value_assessed == tax_amount
    
<br>

- Hypothesis 1 and hypotheis 2 were answered by comparing the means of two subgroups through a T-Test while Hypothesis 3 and hypothesis 4 were answered using Pearson's Correlation test 


___________________________________________________________________________________
___________________________________________________________________________________


## Executive Summary- Conclusions: 

### My findings are:

- I will be using the **Logistic Regression** model because it is best performing( as shown in the chart below):

    
| model                    | rmse_train    |rmse_validate  | r^2_validate|   
|:-------------------------|:--------------|:--------------|:------------|
| mean_baseline            | 250181.876924 | 249144.577291 | 0.000000    | 
| LinearRegression         | 221563.069116 | 220793.764943 | 0.214647    |
| LassoLars alpha 6        | 221569.410724 | 220802.942919 | 0.214582    |
| TweedieRegressor power 1 | 221538.889933 | 220961.423080 | 0.213444    |

    
- Average Tax Rate per county is as follows:

 
| County Code|     State    |    County    | Average Tax Rate |                   
|:-----------|:-------------|:-------------|:-----------------|
| 6037       | California   | Los Angeles  | 1.4262%          |
| 6059       | California   | Orange       | 1.2173%          |
| 6111       | California   | Ventura      | 1.1821%          |



___________________________________________________________________________________
___________________________________________________________________________________

## Pipeline Stages Breakdown

### --> Plan

- Use Trello Board to organize thoughts
    - Link is available here: https://trello.com/b/m1beSkWz/zillow-regression-project

<br>

### --> Acquire

- Store functions that are needed to acquire data from the Zillow database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.

- The final function will return a pandas DataFrame.

- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.

- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

<br>

### --> Prepare 

- Store functions needed to prepare the Zillow data; make sure the module contains the necessary imports to run the code. 

- The final function should do the following: 
    - creates tax_rate column
    - change column names to make them more legible
    - remove any duplicates
    - removes outliers
    - split the data using "zillow_split" function
    - scale numeric data using "min_max_scaler" function
    
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.

<br>

### --> Explore

- Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable, value_assessed.

- Run statistical tests in data exploration: 
    - Document my hypotheses 
    - set an alpha before running the test 
    - document the findings
   
- Conduct feature engineering using SelectKBest and RFE to find most import features to model

- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

<br>

### --> Model 

- Establish a baseline accuracy to determine which model performs better than the baseline (if any) 
- Train (fit, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models I trained 
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

<br>

### --> Deliver

- 5 minute presentation that is verbally supported by slides
    - Audience: Zillow Data Science Team (use technical language)
    - highlights of analysis from pipeline
    - Takeaways from visuals in explore
- Github repository with final notebook that has full data science pipeline, acquire.py, and prepare.py (or wrangle.py)
- Readme.md file that documents all steps for project reproducibility, data dictionary, goals and key findings/takeaways

___________________________________________________________________________________
___________________________________________________________________________________

## Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook


