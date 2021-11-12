import pandas as pd
import os


ethnicity_df = pd.read_csv('output/inputs/input_ethnicity.csv')


for file in os.listdir('output/inputs'):
    if file.startswith('input'):
        #exclude ethnicity
        if file.split('_')[1] not in ['ethnicity.csv']:
            file_path = os.path.join('output/inputs', file)
            print(file_path)
            df = pd.read_csv(file_path)
            merged_df = df.merge(ethnicity_df, how='left', on='patient_id')
            
            merged_df.to_csv(file_path)  