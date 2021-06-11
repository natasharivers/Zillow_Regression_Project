# Zillow_Regression_Project


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
