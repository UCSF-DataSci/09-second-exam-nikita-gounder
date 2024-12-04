import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from patsy import dmatrices
from scipy import stats

ms_data = pd.read_csv('ms_data.csv')
#ms_data = pd.get_dummies(ms_data, columns=['education_level'], drop_first=True) #make levels

#Analyze walking speed:
#y = ms_data['walking_speed']  #walking speed dependent variable
#X = ms_data[['age', 'education_level']] 
y, X = dmatrices('walking_speed ~ age + education_level', data=ms_data, return_type='dataframe')
X = sm.add_constant(X)  

model = sm.OLS(y, X) #OLS model
results = model.fit(cov_type='HC3') #fit model

print(results.summary()) #print summary stats
 

#-----------------

#Boxplot
sns.boxplot(x='insurance_type', y='visit_cost', data=ms_data)
plt.title("Costs by Insurance Type")
plt.show()

#Summary Statistics
summary_stats = ms_data.groupby('insurance_type')['visit_cost'].describe()
print(summary_stats)

#Effect Size
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
#y, X = dmatrices('visit_cost ~ insurance_type', data=ms_data, return_type='dataframe')
#X = sm.add_constant(X)  
#ano_model = sm.OLS(y,X).fit()
#print(anova_lm(ano_model, typ=2))
anova_model = ols('visit_cost ~ C(insurance_type)', data=ms_data).fit()
print(anova_lm(anova_model, typ=2)) 


#-----------------

print(results.params) # Coefficients
print(results.rsquared) # R-squared
print(results.pvalues) # P-values
# T-test
t_stat_age, p_val_age = stats.ttest_ind(ms_data['walking_speed'], ms_data['age'])


# python3 stats_analysis.py