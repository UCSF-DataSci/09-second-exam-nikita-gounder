


import statsmodels.api as sm

X = sm.add_constant(X)  # Add intercept column to X
model = sm.OLS(y, X)
results = model.fit()

# Key outputs
print(results.params) # Coefficients
print(results.rsquared) # R-squared
print(results.pvalues) # P-values
 



# T-test
from scipy import stats
t_stat, p_val = stats.ttest_ind(group1, group2)
# ANOVA
from statsmodels.stats.anova import anova_lm
anova_table = anova_lm(fitted_model, typ=2)
# Chi-square
chi2, p_val = stats.chi2_contingency(contingency_table)