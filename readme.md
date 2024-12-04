# DS-217 Final Exam: Multiple Sclerosis Analysis ReadME


## Question 1: Data Preparation with Command-Line Tools 

Using the shell script prepare.sh that first runs the script `generate_dirty_data.py` to create `ms_data_dirty.csv` and then performs data cleaning using command line tools.
Cleaning involved: Remove comment lines, Remove empty lines, Remove extra commas, Extract essential columns: patient_id, visit_date, age, education_level, walking_speed.

Next the `insurance.lst` file lists unique labels for a new variable, `insurance_type` containing Basic, Better, Best categories.
The summary of the processed data is stored in ms_data.csv. The head looks like this:

15418 ms_data.csv
patient_id,visit_date,age,education_level,walking_speed
P0001,2020-01-11,36.05,Graduate,5.11
P0001,2020-04-02,36.27,Graduate,4.66
P0001,2020-06-17,36.48,Graduate,4.78
P0001,2020-09-14,36.73,Graduate,4.98
P0001,2020-12-16,36.98,Graduate,5.47
P0001,2021-03-01,37.19,Graduate,4.85
P0001,2021-05-29,37.43,Graduate,5.08
P0001,2021-08-19,37.65,Graduate,5.3
P0001,2021-11-21,37.91,Graduate,4.78


## Question 2: Data Analysis with Python 
Using the cleaned data and insurance category file from Question 1, I converted and sorted necessary columns.

Then I added random insurance information and vist costs from .lst file to each unique patient ID. There was random variation in the visit_cost by setting a range for each insurance type and picking a random value rounded to 2 digits for accurat cost representation.

Lastly, presented a summary statistics showing mean walking speed by education level, mean costs by insurance type, and age effects on walking speed.


## Question 3: Statistical Analysis
In this section, statistical analysis on both walking speed and costs outcomes.

To analyze walking speed, I made multiple regression with education and age using sn.OLS modeling. And looked at significant trends, key stats, and advanced analysis through p-values.

### OLS Regression Results

#### Model Summary:
- **Dependent Variable**: Walking Speed
- **Model**: Ordinary Least Squares (OLS)
- **Method**: Least Squares
- **Covariance Type**: HC3 (robust standard errors)
- **Date**: Wed, 04 Dec 2024
- **Time**: 07:49:36          

#### Fit Statistics:
| Statistic              | Value        |
|-------------------------|--------------|
| **R-squared**          | 0.800        |
| **Adj. R-squared**     | 0.800        |
| **F-statistic**        | 1.544e+04    |
| **Prob (F-statistic)** | 0.00         |
| **Log-Likelihood**     | -5254.1      |
| **AIC**                | 1.052e+04    |
| **BIC**                | 1.056e+04    |

Interpretation:
- The model explains 80% of the variance in walking speed, as indicated by the R-squared value.
- The F-statistic suggests the overall significance of the model, with a p-value of 0.00.
- The use of HC3 standard errors means reliability 


To analyze costs, made Box plots and basic statistics to see the insurance efect and looked at ANOVA to see effect sizes in insurance groups. The summary is seen below.

### Key Statistics: Costs based on Insurance Type
==============================================================================
| Insurance Type | Count   | Mean      | Std Dev   | Min    | 25%      | 50%      | 75%      | Max    |
|----------------|---------|-----------|-----------|--------|----------|----------|----------|--------|
| **Basic**      | 5045.0  | 99.77     | 29.06     | 50.02  | 74.65    | 99.19    | 124.53   | 149.93 |
| **Best**       | 5392.0  | 424.40    | 43.18     | 350.03 | 386.99   | 423.64   | 462.01   | 499.96 |
| **Better**     | 4947.0  | 239.99    | 34.84     | 180.02 | 209.75   | 240.48   | 270.22   | 299.99 |

### Summary:
- **Basic**: The mean cost is approximately $99.77, with costs ranging from $50.02 to $149.93.
- **Better**: The mean cost is approximately $239.99, with costs ranging from $180.02 to $299.99.
- **Best**: The mean cost is approximately $424.40, with costs ranging from $350.03 to $499.96.


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