import csv
import pandas as pd
import os
import glob
import plotly.graph_objs as go
import plotly.express as px

# data = pd.read_csv("/outputmeasure_prescribing_rate_all")


# type_counts = data['ageband_narrow'].value_counts()
# df2 = pd.DataFrame({'age_band': type_counts}, 
                     # index = ['65-74', '75-79', '80-84','85-89','90+']
                   # )
# fig=df2.plot.pie(y='age_band', figsize=(10,10), autopct='%1.1f%%').get_figure()

# fig.savefig("output/descriptive_*.png")

file_list=[]
file_dict = {}

for file in os.listdir('output'):    
    if file.startswith('input_a'):
        file_path = os.path.join('output/', file)
        file_list.append(file_path)
        
for file in file_list:        
        key = file
        df_input = pd.read_csv(file)
        file_dict[key] = df_input

for key in file_dict.keys():
    file_dict[key].describe().to_csv('output/Descriptive_Statistics_'+str(key.split('/')[1])+'.csv')

#df_input.describe().to_csv('output/Descriptive_Statistics.csv')


df_all_ap = pd.read_csv("output/measure_ap_prescribing_rate_all.csv").dropna()
df_all_ad = pd.read_csv("output/measure_ad_prescribing_rate_all.csv").dropna()
df_region_ap = pd.read_csv("output/measure_ap_prescribing_rate_region.csv").dropna()
df_region_ad = pd.read_csv("output/measure_ad_prescribing_rate_region.csv").dropna()
df_age_ap = pd.read_csv("output/measure_ap_prescribing_rate_age.csv").dropna()
df_age_ad = pd.read_csv("output/measure_ad_prescribing_rate_age.csv").dropna()


df_all_ap['date'] = pd.to_datetime(df_all_ap['date'])
df_region_ap['date'] = pd.to_datetime(df_region_ap['date'])
df_age_ap['date'] = pd.to_datetime(df_age_ap['date'])


df_all_ad['date'] = pd.to_datetime(df_all_ad['date'])
df_region_ad['date'] = pd.to_datetime(df_region_ad['date'])
df_age_ad['date'] = pd.to_datetime(df_age_ad['date'])


# Plotly figure 1
fig = px.line(df_region_ad, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig.update_layout(title='Antidepressent Prescribing, Region' , showlegend=True)
fig.update_yaxes(tickformat = ',.0%')
fig.write_html("output/region_ad.html")

# Plotly figure 2
fig2 = px.line(df_age_ad, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig2.update_layout(title='Antidepressent Prescribing, Age' , showlegend=True)
fig2.update_yaxes(tickformat = ',.0%')
fig2.write_html("output/age_ad.html")

# Plotly figure 3
fig3 = px.line(df_all_ad, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig3.update_layout(title='Antidepressent Prescribing, Care Home Type' , showlegend=True)
fig3.update_yaxes(tickformat = ',.0%')
fig3.write_html("output/carehome_ad.html")


# Plotly figure 4
fig4 = px.line(df_region_ap, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig4.update_layout(title='Antipsychotic Prescribing, Region' , showlegend=True)
fig4.update_yaxes(tickformat = ',.0%')
fig4.write_html("output/region_ap.html")

# Plotly figure 5
fig5 = px.line(df_age_ap, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig5.update_layout(title='Antipsychotic Prescribing, Age' , showlegend=True)
fig5.update_yaxes(tickformat = ',.0%')
fig5.write_html("output/age_ap.html")

# Plotly figure 6
fig6 = px.line(df_all_ap, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig6.update_layout(title='Antipsychotic Prescribing, Care Home Type' , showlegend=True)
fig6.update_yaxes(tickformat = ',.0%')
fig6.write_html("output/carehome_ap.html")