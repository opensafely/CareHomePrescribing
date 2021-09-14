import csv
import pandas as pd
import os
import plotly.graph_objs as go
import plotly.express as px

# data = pd.read_csv("/outputmeasure_prescribing_rate_all")


# type_counts = data['ageband_narrow'].value_counts()
# df2 = pd.DataFrame({'age_band': type_counts}, 
                     # index = ['65-74', '75-79', '80-84','85-89','90+']
                   # )
# fig=df2.plot.pie(y='age_band', figsize=(10,10), autopct='%1.1f%%').get_figure()

# fig.savefig("output/descriptive_*.png")



for file in os.listdir('output'):    
    if file.startswith('input_2019-11'):
        file_path = os.path.join('output/', file)
        df_input = pd.read_csv(file_path)



df_input.describe().to_csv('output/Descriptive_Statistics.csv')

"""
df_all = pd.read_csv("output/measure_prescribing_rate_all.csv")
df_region = pd.read_csv("output/measure_prescribing_rate_region.csv")
df_age = pd.read_csv("output/measure_prescribing_rate_age.csv")



df_all['date'] = pd.to_datetime(df_all['date'])
df_region['date'] = pd.to_datetime(df_region['date'])
df_age['date'] = pd.to_datetime(df_age['date'])


df_all_nonCH = df_all[df_all['care_home_type']=='PR']
df_all_CH = df_all[df_all['care_home_type']=='PN']

df_region_nonCH = df_region[df_region['care_home_type']=='PR']
df_region_CH = df_region[df_region['care_home_type']=='PN']

df_age_nonCH = df_age[df_age['care_home_type']=='PR']
df_age_CH = df_age[df_age['care_home_type']=='PN']


# Plotly figure 1
fig = px.line(df_region_CH, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig.update_layout(title='Antidepressent Prescribing, Region' , showlegend=True)
fig.write_html("output/region.html")

# Plotly figure 2
fig2 = px.line(df_age_CH, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig2.update_layout(title='Antidepressent Prescribing, Age' , showlegend=True)
fig2.write_html("output/age.html")

# Plotly figure 3
fig3 = px.line(df_all, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig3.update_layout(title='Antidepressent Prescribing, Care Home Type' , showlegend=True)
fig3.write_html("output/carehome.html")
"""