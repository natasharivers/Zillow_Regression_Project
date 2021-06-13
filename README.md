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


## Project Deliverables:

___________________________________________________________________________________
___________________________________________________________________________________

## Data Dictionary

| Target          |       Datatype          |    Definition                      |
|-----------------|-------------------------|:----------------------------------:|
| value_assessed  | 28391 non-null: float64 | assessed value of homes in dataset | 


| Feature                 |       Datatype         |    Definition               |
|-------------------------|------------------------|:---------------------------:|
|total_sqft               |28321 non-null: float64 |total calculated square feet |
|bedrooms                 |28392 non-null: float64 |number of bedrooms           |
|bathrooms                |28392 non-null: float64 |number of bathrooms          |
|tax_amount               |28391 non-null: float64 |tax amount                   |
|year_built               |28298 non-null: float64 |year the residence was built |
|county_code              |28392 non-null: float64 |county code                  |
|parcelid                 |28392 non-null: int64   |unique property id           |
|tax_rate                 |28390 non-null: float64 |created column for taxrate   |

___________________________________________________________________________________
___________________________________________________________________________________

## county_code Dictionary

| Fips Code  |     State    |    County    |                      
|:-----------|:-------------|:-------------|
| 6037       | California   | Los Angeles  |
| 6059       | California   | Orange       |
| 6111       | California   | Ventura      |

___________________________________________________________________________________
___________________________________________________________________________________

## Hypothesis and Questions

#### Hypothesis 1:
- **Null Hypothesis**: There is a relationship between value_assessed and bedroom count
    - value_assessed == bedroom count
- **Alternate Hypothesis**: There is no relationship between value_assessed and bedroom count
    - value_assessed != bedroom count

<br>

#### Hypothesis 2:
- **Null Hypothesis**: There is a relationship between value_assessed and number of bathrooms
    - value_assessed == bathroom count
- **Alternate Hypothesis**: There is no relationship between value_assessed and number of bathrooms
    - value_assessed != bathroom count

<br>

#### Hypothesis 3:
- **Null Hypothesis**: There is no relationship between total_sqft and value_assessed
    - total_sqft != value_assessed 
- **Alternate Hypothesis**: There is a relationship between total_sqft and value_assessed
    - total_sqft == value_assessed

<br>

#### Hypothesis 4:
- **Null Hypothesis**: There is no relationship between tax_amount and value_assessed
    - tax_amount != value_assessed 
- **Alternate Hypothesis**: There is a relationship between tax_amount and value_assessed
    - tax_amount == value_assessed
    
<br>

- Hypothesis 1 and hypotheis 2 were answered by comparing the means of two subgroups through a T-Test while Hypothesis 3 and hypothesis 4 were answered using Pearson's Correlation test 

___________________________________________________________________________________
___________________________________________________________________________________


## Executive Summary- Conclusions & Next Steps


___________________________________________________________________________________
___________________________________________________________________________________

# CORRECT THIS PART!!! TO FIT ZILLOW 
## Pipeline Stages Breakdown

### --> Plan

- Create README.md with data dictionary, project and business goals, come up with initial hypotheses.
- Acquire data from the Codeup Database and create a function to automate this process. Save the function in an acquire.py file to import into the Final Report Notebook.
- Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion.
- Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- Establish a baseline accuracy and document well.
- Train three different classification models.
- Evaluate models on train and validate datasets.
- Choose the model with that performs the best and evaluate that single model on the test dataset.
- Create csv file with the measurement id, the probability of the target values, and the model's prediction for each observation in my test dataset.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.

### --> Acquire

- Store functions that are needed to acquire data from the telco database on the Codeup data science database server; make sure the acquire.py module contains the necessary imports to run my code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (.info(), .describe(), .value_counts(), ...).

### --> Prepare 

- Store functions needed to prepare the telco data; make sure the module contains the necessary imports to run the code. The final function should do the following: - Split the data into train/validate/test. - Change data types as needed. - remove any duplicates. -change dataframe name 
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.


### --> Explore

- Answer key questions, my hypotheses, and figure out the features that can be used in a classification model to best predict the target variable, churn.
- Run statistical test in data exploration. Document my hypotheses, set an alpha before running the test, and document the findings well.
- Create visualizations and run statistical test that work toward discovering variable relationships. The goal is to identify features that are related to churn (the target), identify any data integrity issues, and understand 'how the data works'. Run correlation code to identify if there is any positive correlation between churn and other variables.
- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.

### --> Model 

- Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 3 different models. Document these steps well.
- Train (fit, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate dataframe.
- Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.


### --> Deliver

- Introduce myself and my project goals at the very beginning of my notebook walkthrough.
- Summarize my findings at the beginning like I would for an Executive Summary. 
- Walk Codeup Data Science Team through the analysis I did to answer my questions and that lead to my findings. 
- Clearly call out the questions and answers I am analyzing as well as offer insights and recommendations based on my findings.
 
___________________________________________________________________________________
___________________________________________________________________________________

## Reproduce My Project

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook.

- Read this README.md
- Download the aquire.py, prepare.py, and final_report.ipynb files into your working directory
- Add your own env file to your directory. (user, password, host)
- Run the final_report.ipynb notebook



### PLAN
-important!!
    - 3 different sources of documentation
        - comment on EVERY cell in notebook
        - have a physical notebook to plan out problem statement, hypothesis, assumptions, statistical tests you want to do
        - formal planning on Trello 
        - have a good readme.md
        
- you are: data scientist with Zillow
    - predicting taxvalue:
        - single unit properties
        - sold during May, June, July, August

- tax_rate for EACH county
- DO NOT include tax_rate in X_train
- have your GOALS in mine
- Determine and document how you handled outliers


### ACQUIRE:
- sql query
- create one df
- input into new notebook to make sure it works and all data looks good
- cache and save into csv (to save time)


### PREPARE:
- look at distribution of individual columns
- check for outliers-  
    - what is the cause, 
    - what will you do about them?
    - IF dropping outliers say: "CANNOT verify that this data isnt accurate but I am choosing to leave it out of my data"
- check for nulls and drop nulls
- check for duplicates and drop duplicates
- scale where necessary 
    - MinMaxScale(must handle outliers FIRST)
    - RobustScaler (is good at handling outliers)
- look for errors in data 
    - some things don't "look right"
        - 10sqft with 10 bathrooms is not correct


### EXPLORE:
- Explore on SCALED data
- combination plots
- figure out drives
- df.sample(1000) - spit out plots to see data (not final product)
- REQUIRED: 
    - at least one T-Test and one correlation test
    - visualize all combination of varibles 
    - what independent are correlated with dependent variables
    - which independent are correlated with independent variables
- Make sure you have takeaways


### MODEL:
- create baseline
- RMSE, MSE, SSE (use one and stay consistent)
- Feature Engineering
    - what features should we include (RFS)
    - what features dont add value?
    - any new features you'd like to see?? (takeaways)
- select models to use
- which performs best??
- show vs baseline


### Deliverables:
- 5 minute presentation
- Slide deck presentation 
    - Canva, google slides, powerpoint, etc
    - presenting to Zillow Team
    - use technical language
    - do visuals (Tableau if wanted)
- highlights of analysis from pipeline
- Takeaways from visuals in explore
- Single notebook with Full pipeline
- Well documented README
- wrangle.py with scaling and feature engineering (at last)
