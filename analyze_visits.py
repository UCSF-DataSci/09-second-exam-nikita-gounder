
import pandas as pd
import numpy as np
import random

#Load and structure the data:
ms_data = pd.read_csv('ms_data.csv')
ms_data['visit_date'] = pd.to_datetime(ms_data['visit_date'], format='%Y-%m-%d')
ms_data.groupby(['patient_id', 'visit_date'])
#print(ms_data.head())


#Add insurance information
with open('insurance.lst', 'r') as file:
    insurance = [line.strip() for line in file]

insurance_map = {}
for patient_id in ms_data['patient_id'].unique():
    insurance_map[patient_id]=random.choice(insurance)

ms_data['insurance_type'] = ms_data['patient_id'].map(insurance_map)


# Cost ranges for each insurance type
insur_ranges = {
    'Basic': (50, 150),
    'Better': (180, 300),
    'Best': (350, 500)
}

def calculate_visit_cost(row):
    cost_range = insur_ranges[row['insurance_type']] 
    rand_num = np.random.uniform(cost_range[0], cost_range[1])
    return np.round(rand_num, 2)

ms_data['visit_cost'] = ms_data.apply(calculate_visit_cost, axis=1)
ms_data.to_csv('ms_data.csv', index=False)
print(ms_data.head())


#Calculate summary statistics:
#Mean walking speed by education level
print(ms_data.groupby('education_level').agg({'walking_speed': 'mean'}))
#Mean costs by insurance type
print(ms_data.groupby('insurance_type').agg({'visit_cost': 'mean'}))
#Age effects on walking speed
#ms_data.groupby('age').agg({'walking_speed': 'mean'})
ms_data.plot('age', 'walking_speed')



#python3 analyze_visits.py