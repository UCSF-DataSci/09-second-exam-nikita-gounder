
import pandas as pd
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
ms_data.to_csv('ms_data.csv', index=False)
print(ms_data.head())


#Calculate summary statistics:
#Mean walking speed by education level
ms_data.groupby(['walking_speed', 'education_level']).mean
#Mean costs by insurance type
ms_data.groupby(['walking_speed', 'insurance_type']).mean
#Age effects on walking speed
ms_data.groupby(['age', 'walking_speed']).mean


#python3 analyze_visits.py