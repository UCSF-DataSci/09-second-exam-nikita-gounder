# DS-217 Final Exam: Multiple Sclerosis Analysis ReadME


## Question 1: Data Preparation with Command-Line Tools 

Using the shell script prepare.sh that first runs the script `generate_dirty_data.py` to create `ms_data_dirty.csv` and then performs data cleaning using command line tools.
Cleaning involved: Remove comment lines, Remove empty lines, Remove extra commas, Extract essential columns: patient_id, visit_date, age, education_level, walking_speed.

Next the `insurance.lst` file lists unique labels for a new variable, `insurance_type` containing Basic, Better, Best categories.
The summary of the processed data is stored in ms_data.csv.


## Question 2: Data Analysis with Python 
Using the cleaned data and insurance category file from Question 1, I converted and sorted necessary columns.

Then I added random insurance information and vist costs from .lst file to each unique patient ID. There was random variation in the visit_cost by setting a range for each insurance type and picking a random value rounded to 2 digits for accurat cost representation.

Lastly, presented a summary statistics showing mean walking speed by education level, mean costs by insurance type, and age effects on walking speed.


## Question 3: Statistical Analysis
In this section, statistical analysis on both walking speed and costs outcomes.

To analyze walking speed, I made multiple regression with education and age using sn.OLS modeling. And looked at significant trends, key stats, and advanced analysis through p-values.

 OLS Regression Results                            
==============================================================================
Dep. Variable:          walking_speed   R-squared:                       0.800
Model:                            OLS   Adj. R-squared:                  0.800
Method:                 Least Squares   F-statistic:                 1.544e+04
Date:                Wed, 04 Dec 2024   Prob (F-statistic):               0.00
Time:                        07:49:36   Log-Likelihood:                -5254.1
No. Observations:               15384   AIC:                         1.052e+04
Df Residuals:                   15379   BIC:                         1.056e+04
Df Model:                           4                                         
Covariance Type:                  HC3                                         

To analyze costs, made Box plots and basic statistics to see the insurance efect and looked at ANOVA to see effect sizes in insurance groups. 

Key Statistics: Costs based on Insurance Type
==============================================================================
                 count        mean        std     min      25%      50%       75%     max
insurance_type                                                                           
Basic           5045.0   99.774789  29.057243   50.02   74.650   99.190  124.5300  149.93
Best            5392.0  424.404062  43.177420  350.03  386.985  423.635  462.0125  499.96
Better          4947.0  239.992151  34.840248  180.02  209.745  240.480  270.2200  299.99


## Question 4: Data Visualization
Created visualizations for both walking speed and cost analyses in a Jupyter notebook.

First we look at the Walking speed analysis scatter plot of age vs walking speed with regression line. We can see that as age increases, walking speed steadily decreases. There is low outliers and a strong association.
The Box plots by education level shows that it is hard to predict walking speed based on education. There is varation with highschool and some college showing lower walking speed compared to Bachelors/Graduate education.
The Line plot showing education~age interaction shows the same relationship as the scatter plot with variation by education. The trend is still similar with increasing age, decreasing walking speed. The education levels are all pretty similar. 

Looking at Cost analysis through a Bar plot of mean costs by insurance type, we can see that the highest costs come from the Better insurance type. This might be due to the associated range of cost values. Better is more expensive than Basic.
The Box plots showing cost distributions with Confidence Intervals show a similar trend as the bar plot. The confidence intervals are similar in all 3 insurance types.

Next we Combined visualizations, first using a  Pair plot looking at key variables. Here we can see the same strong correlation between age and walking speeds. While the other variables don't show strong trends but show the relationship between ages and costs based on insurance.
The Faceted plots foces on education/insurance and shows that education effects which insurance policy someone takes. For example, higher education chooses the Best or Better policy the most comapred to Basic.
The relevant Time trends looked at walking speeds show the same negative trends with walking speeds and age.

In summary, there is a strong trend between age and walking speeds seen in the stistical reasoning and visualization plots. There is also variation by Insurance type, with education determining which plan. However, age and visit costs generally didn't effect insurance type. But ther values are very close to each other based on education and insurance (no outliers).