import csv
import pandas as pd
import os
import glob
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


if not os.path.exists('output/graphs'):
    os.makedirs('output/graphs')
    
if not os.path.exists('output/descriptives'):
    os.makedirs('output/descriptives')
    

# data = pd.read_csv("/outputmeasure_prescribing_rate_all")


# type_counts = data['ageband_narrow'].value_counts()
# df2 = pd.DataFrame({'age_band': type_counts}, 
                     # index = ['65-74', '75-79', '80-84','85-89','90+']
                   # )
# fig=df2.plot.pie(y='age_band', figsize=(10,10), autopct='%1.1f%%').get_figure()

# fig.savefig("output/inputs/descriptive_*.png")

file_list=[]
file_dict = {}

for file in os.listdir('output/inputs/'):    
    if file.startswith('input_'):
            if file.split('_')[1] not in ['ethnicity.csv']:
                file_path = os.path.join('output/inputs/', file)
                file_list.append(file_path)
        
for file in file_list:
        key = file
        df_input = pd.read_csv(file)
        file_dict[key] = df_input

for key in file_dict.keys():
    file_dict[key].describe().to_csv('output/descriptives/descriptive_statistics_'+str(key.split('/')[2])+'.csv')







df_all_ap = pd.read_csv("output/inputs/measure_ap_prescribing_rate_all.csv").dropna()
df_all_ad = pd.read_csv("output/inputs/measure_ad_prescribing_rate_all.csv").dropna()
df_region_ap = pd.read_csv("output/inputs/measure_ap_prescribing_rate_region.csv").dropna()
df_region_ad = pd.read_csv("output/inputs/measure_ad_prescribing_rate_region.csv").dropna()
df_age_ap = pd.read_csv("output/inputs/measure_ap_prescribing_rate_age.csv").dropna()
df_age_ad = pd.read_csv("output/inputs/measure_ad_prescribing_rate_age.csv").dropna()

df_all_ap_new = pd.read_csv("output/inputs/measure_ap_prescribing_new_all.csv").dropna()
df_all_ad_new = pd.read_csv("output/inputs/measure_ad_prescribing_new_all.csv").dropna()
df_region_ap_new = pd.read_csv("output/inputs/measure_ap_prescribing_new_region.csv").dropna()
df_region_ad_new = pd.read_csv("output/inputs/measure_ad_prescribing_new_region.csv").dropna()
df_age_ap_new = pd.read_csv("output/inputs/measure_ap_prescribing_new_age.csv").dropna()
df_age_ad_new = pd.read_csv("output/inputs/measure_ad_prescribing_new_age.csv").dropna()

df_all_ap_control = pd.read_csv("output/control/measure_control_ap_prescribing_rate_all.csv").dropna()
df_all_ad_control = pd.read_csv("output/control/measure_control_ad_prescribing_rate_all.csv").dropna()
df_region_ap_control = pd.read_csv("output/control/measure_control_ap_prescribing_rate_region.csv").dropna()
df_region_ad_control = pd.read_csv("output/control/measure_control_ad_prescribing_rate_region.csv").dropna()
df_age_ap_control = pd.read_csv("output/control/measure_control_ap_prescribing_rate_age.csv").dropna()
df_age_ad_control = pd.read_csv("output/control/measure_control_ad_prescribing_rate_age.csv").dropna()

df_all_ap_new_control = pd.read_csv("output/control/measure_control_ap_prescribing_new_all.csv").dropna()
df_all_ad_new_control = pd.read_csv("output/control/measure_control_ad_prescribing_new_all.csv").dropna()
df_region_ap_new_control = pd.read_csv("output/control/measure_control_ap_prescribing_new_region.csv").dropna()
df_region_ad_new_control = pd.read_csv("output/control/measure_control_ad_prescribing_new_region.csv").dropna()
df_age_ap_new_control = pd.read_csv("output/control/measure_control_ap_prescribing_new_age.csv").dropna()
df_age_ad_new_control = pd.read_csv("output/control/measure_control_ad_prescribing_new_age.csv").dropna()


df_all_ap['date'] = pd.to_datetime(df_all_ap['date'])
df_region_ap['date'] = pd.to_datetime(df_region_ap['date'])
df_age_ap['date'] = pd.to_datetime(df_age_ap['date'])
df_all_ad['date'] = pd.to_datetime(df_all_ad['date'])
df_region_ad['date'] = pd.to_datetime(df_region_ad['date'])
df_age_ad['date'] = pd.to_datetime(df_age_ad['date'])

df_all_ap_new['date'] = pd.to_datetime(df_all_ap_new['date'])
df_region_ap_new['date'] = pd.to_datetime(df_region_ap_new['date'])
df_age_ap_new['date'] = pd.to_datetime(df_age_ap_new['date'])
df_all_ad_new['date'] = pd.to_datetime(df_all_ad_new['date'])
df_region_ad_new['date'] = pd.to_datetime(df_region_ad_new['date'])
df_age_ad_new['date'] = pd.to_datetime(df_age_ad_new['date'])

df_all_ap_control['date'] = pd.to_datetime(df_all_ap_control['date'])
df_region_ap_control['date'] = pd.to_datetime(df_region_ap_control['date'])
df_age_ap_control['date'] = pd.to_datetime(df_age_ap_control['date'])
df_all_ad_control['date'] = pd.to_datetime(df_all_ad_control['date'])
df_region_ad_control['date'] = pd.to_datetime(df_region_ad_control['date'])
df_age_ad_control['date'] = pd.to_datetime(df_age_ad_control['date'])

df_all_ap_new_control['date'] = pd.to_datetime(df_all_ap_new_control['date'])
df_region_ap_new_control['date'] = pd.to_datetime(df_region_ap_new_control['date'])
df_age_ap_new_control['date'] = pd.to_datetime(df_age_ap_new_control['date'])
df_all_ad_new_control['date'] = pd.to_datetime(df_all_ad_new_control['date'])
df_region_ad_new_control['date'] = pd.to_datetime(df_region_ad_new_control['date'])
df_age_ad_new_control['date'] = pd.to_datetime(df_age_ad_new_control['date'])


# Plotly figure 1
fig1 = px.line(df_region_ad, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig1.update_layout(title='Antidepressent Prescribing, Region' , showlegend=True, yaxis_tickformat= ',.0%')
#fig1.update_yaxes(tickformat = ',.0%')
#fig1.write_html("output/graphs/region_ad.html", include_plotlyjs="cdn")

# Plotly figure 2
fig2 = px.line(df_age_ad, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig2.update_layout(title='Antidepressent Prescribing, Age' , showlegend=True)
fig2.update_yaxes(tickformat = ',.0%')
# fig2.write_html("output/graphs/age_ad.html", include_plotlyjs="cdn")

# Plotly figure 3
fig3 = px.line(df_all_ad, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig3.update_layout(title='Antidepressent Prescribing, Care Home Type' , showlegend=True)
fig3.update_yaxes(tickformat = ',.0%')
# fig3.write_html("output/graphs/carehome_ad.html", include_plotlyjs="cdn")


# Plotly figure 4
fig4 = px.line(df_region_ap, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig4.update_layout(title='Antipsychotic Prescribing, Region' , showlegend=True)
fig4.update_yaxes(tickformat = ',.0%')
# fig4.write_html("output/graphs/region_ap.html", include_plotlyjs="cdn")

# Plotly figure 5
fig5 = px.line(df_age_ap, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig5.update_layout(title='Antipsychotic Prescribing, Age' , showlegend=True)
fig5.update_yaxes(tickformat = ',.0%')
# fig5.write_html("output/graphs/age_ap.html", include_plotlyjs="cdn")

# Plotly figure 6
fig6 = px.line(df_all_ap, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig6.update_layout(title='Antipsychotic Prescribing, Care Home Type' , showlegend=True)
fig6.update_yaxes(tickformat = ',.0%')
# fig6.write_html("output/graphs/carehome_ap.html", include_plotlyjs="cdn")



# Plotly figure 7
fig7 = px.line(df_region_ad_new, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig7.update_layout(title='Antidepressent New, Region' , showlegend=True)
fig7.update_yaxes(tickformat = ',.0%')
# fig7.write_html("output/graphs/region_ad_new.html", include_plotlyjs="cdn")

# Plotly figure 8
fig8 = px.line(df_age_ad_new, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig8.update_layout(title='Antidepressent New, Age' , showlegend=True)
fig8.update_yaxes(tickformat = ',.0%')
# fig8.write_html("output/graphs/age_ad_new.html", include_plotlyjs="cdn")

# Plotly figure 9
fig9 = px.line(df_all_ad_new, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig9.update_layout(title='Antidepressent New, Care Home Type' , showlegend=True)
fig9.update_yaxes(tickformat = ',.0%')
# fig9.write_html("output/graphs/carehome_ad_new.html", include_plotlyjs="cdn")


# Plotly figure 10
fig10 = px.line(df_region_ap_new, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig10.update_layout(title='Antipsychotic New, Region' , showlegend=True)
fig10.update_yaxes(tickformat = ',.0%')
# fig10.write_html("output/graphs/region_ap_new.html", include_plotlyjs="cdn")

# Plotly figure 11
fig11 = px.line(df_age_ap_new, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig11.update_layout(title='Antipsychotic New, Age' , showlegend=True)
fig11.update_yaxes(tickformat = ',.0%')
# fig11.write_html("output/graphs/age_ap_new.html", include_plotlyjs="cdn")

# Plotly figure 12
fig12 = px.line(df_all_ap_new, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig12.update_layout(title='Antipsychotic New, Care Home Type' , showlegend=True)
fig12.update_yaxes(tickformat = ',.0%')
# fig12.write_html("output/graphs/carehome_ap_new.html", include_plotlyjs="cdn")



##Control graphs
# Plotly figure 1
fig13 = px.line(df_region_ad_control, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig13.update_layout(title='Control Antidepressent Prescribing, Region' , showlegend=True)
fig13.update_yaxes(tickformat = ',.0%')
# fig13.write_html("output/control_region_ad.html")

# Plotly figure 2
fig14 = px.line(df_age_ad_control, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig14.update_layout(title='Control Antidepressent Prescribing, Age' , showlegend=True)
fig14.update_yaxes(tickformat = ',.0%')
# fig14.write_html("output/control_age_ad.html")

# Plotly figure 3
fig15 = px.line(df_all_ad_control, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig15.update_layout(title='Control Antidepressent Prescribing, Care Home Type' , showlegend=True)
fig15.update_yaxes(tickformat = ',.0%')
# fig15.write_html("output/control_carehome_ad.html")


# Plotly figure 4
fig16 = px.line(df_region_ap_control, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig16.update_layout(title='Control Antipsychotic Prescribing, Region' , showlegend=True)
fig16.update_yaxes(tickformat = ',.0%')
# fig16.write_html("output/control_region_ap.html")

# Plotly figure 5
fig17 = px.line(df_age_ap_control, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig17.update_layout(title='Control Antipsychotic Prescribing, Age' , showlegend=True)
fig17.update_yaxes(tickformat = ',.0%')
# fig17.write_html("output/control_age_ap.html")

# Plotly figure 6
fig18 = px.line(df_all_ap_control, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig18.update_layout(title='Control Antipsychotic Prescribing, Care Home Type' , showlegend=True)
fig18.update_yaxes(tickformat = ',.0%')
# fig18.write_html("output/control_carehome_ap.html")



# Plotly figure 7
fig19 = px.line(df_region_ad_new_control, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig19.update_layout(title='Control Antidepressent New, Region' , showlegend=True)
fig19.update_yaxes(tickformat = ',.0%')
# fig19.write_html("output/control_region_ad_new.html")

# Plotly figure 8
fig20 = px.line(df_age_ad_new_control, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig20.update_layout(title='Control Antidepressent New, Age' , showlegend=True)
fig20.update_yaxes(tickformat = ',.0%')
# fig20.write_html("output/control_age_ad_new.html")

# Plotly figure 9
fig21 = px.line(df_all_ad_new_control, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig21.update_layout(title='Control Antidepressent New, Care Home Type' , showlegend=True)
fig21.update_yaxes(tickformat = ',.0%')
# fig21.write_html("output/control_carehome_ad_new.html")


# Plotly figure 10
fig22 = px.line(df_region_ap_new_control, x='date', y='value',
              color="region",
              line_group="region", hover_name="region")
fig22.update_layout(title='Control Antipsychotic New, Region' , showlegend=True)
fig22.update_yaxes(tickformat = ',.0%')
# fig22.write_html("output/control_region_ap_new.html")

# Plotly figure 11
fig23 = px.line(df_age_ap_new_control, x='date', y='value',
              color="ageband_narrow",
              line_group="ageband_narrow", hover_name="ageband_narrow")
fig23.update_layout(title='Control Antipsychotic New, Age' , showlegend=True)
fig23.update_yaxes(tickformat = ',.0%')
# fig23.write_html("output/control_age_ap_new.html")

# Plotly figure 12
fig24 = px.line(df_all_ap_new_control, x='date', y='value',
              color="care_home_type",
              line_group="care_home_type", hover_name="care_home_type")
fig24.update_layout(title='Control Antipsychotic New, Care Home Type' , showlegend=True)
fig24.update_yaxes(tickformat = ',.0%')
# fig12.write_html("output/control_carehome_ap_new.html")


figfinal = make_subplots(rows=12, cols=2,subplot_titles=(
'Antidepressent Prescribing,Region','Control Antidepressent Prescribing, Region',
'Antidepressent Prescribing, Age','Control Antidepressent Prescribing, Age',
'Antidepressent Prescribing, Care Home Type','Control Antidepressent Prescribing, Care Home Type',
'Antipsychotic Prescribing, Region','Control Antipsychotic Prescribing, Region',
'Antipsychotic Prescribing, Age','Control Antipsychotic Prescribing, Age',
'Antipsychotic Prescribing, Care Home Type','Control Antipsychotic Prescribing, Care Home Type',
'Antidepressent New, Region','Control Antidepressent New, Region',
'Antidepressent New, Age','Control Antidepressent New, Age',
'Antidepressent New, Care Home Type','Control Antidepressent New, Care Home Type',
'Antipsychotic New, Region','Control Antipsychotic New, Region',
'Antipsychotic New, Age','Control Antipsychotic New, Age',
'Antipsychotic New, Care Home Type','Control Antipsychotic New, Care Home Type'
))


for d in fig1.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=1)
        
for d in fig2.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=2, col=1)
    
for d in fig3.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=3, col=1)
    
for d in fig4.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=4, col=1)
    
for d in fig5.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=5, col=1)
    
for d in fig6.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=6, col=1)
    
for d in fig7.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=7, col=1)
    
for d in fig8.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=8, col=1)
    
for d in fig9.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=9, col=1)
    
for d in fig10.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=10, col=1)
    
for d in fig11.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=11, col=1)
    
for d in fig12.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=12, col=1)
    
    
    
for d in fig13.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=1, col=2)
        
for d in fig14.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=2, col=2)
    
for d in fig15.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=3, col=2)
    
for d in fig16.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=4, col=2)
    
for d in fig17.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=5, col=2)
    
for d in fig18.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=6, col=2)
    
for d in fig19.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=7, col=2)
    
for d in fig20.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=8, col=2)
    
for d in fig21.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=9, col=2)
    
for d in fig22.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=10, col=2)
    
for d in fig23.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=11, col=2)
    
for d in fig24.data:
    figfinal.add_trace((go.Scatter(x=d['x'], y=d['y'], name = d['name'])), row=12, col=2)

figfinal.update_layout(height=8000, width=2000)
figfinal.update_yaxes(tickformat = ',.1%')
figfinal.write_html("output/graphs/figfinal.html")