
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
import psycopg2
from datetime import date
from datetime import timedelta
from PIL import Image
today=date.today()
LastMonth=today - timedelta(days = 45)
date30 = LastMonth.strftime('%Y-%m-%d %H:%M:%S')

conn = psycopg2.connect(database = 'mintoprod',
                        user =     'mintomaster',
                        password = 'minto.ai',
                        host =     'minto-prod.ckz6cv88gn8n.us-east-2.rds.amazonaws.com',
                        port =     '5432')


cur = conn.cursor()

cur.execute('''
            select
	id,
	name,
	telemetry_time_ist_day,
	avg_riskscore_2,
	avg_thd,
	avg_i_rms
from
	aggregated_data_daily_v2 adhv
where
    id in (5,7,8,9,10,13) and
	telemetry_time_ist_day >= '''+"'"+date30+"'"+'''
	and avg_i_rms is not null
	and avg_riskscore_2 is not null
	and avg_i_rms is not null
order by
	telemetry_time_ist_day,
	id


            ''')

lister = cur.fetchall()

df = pd.DataFrame(lister,columns = ['id',	'name',	'telemetry_time_ist_day','avg_riskscore_2','avg_thd','avg_i_rms'])

df.index = pd.to_datetime(df.telemetry_time_ist_day)


#st.selectbox('Select Faultcode', ['Bearing', 'Winding'])
#df = pd.read_csv(r"C:/Users/Sairam/Downloads/out.csv");
#df.index=df.telemetry_time_ist_day
df=df.drop(columns='telemetry_time_ist_day')
df = df.sort_values(["id", "telemetry_time_ist_day"], ascending = (True, True))
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
dfTable = pd.read_csv(r"Currentunbalance.csv")
dfTable.index=dfTable[dfTable.columns[0]]
dfTable=dfTable.drop(columns=dfTable.columns[0])
dfTable1 = pd.read_csv(r"Voltage Unbalance.csv")
dfTable1.index=dfTable1[dfTable1.columns[0]]
dfTable1=dfTable1.drop(columns=dfTable1.columns[0])
image = Image.open("Current unbalance.jpg")
logo =Image.open(r"logo small.png")
#st.image(image, caption='Example to Understand Current unbalance: Clear current unbalance - Red phase has a different RMS value compared with the other 2 phases.')
st.title('DIR PATIL 21-08-2021 - Current Unbalance')
st.markdown('**Machine Insight**')
st.markdown('''
* **Cause** \n
Most often a current unbalance is directly caused by an unbalance in voltage. In these cases, the current unbalance is usually higher than the voltage unbalance.
In Our Case, The voltage Unbalance is under acceptable conditions. So, Here current unbalance is due to either a resistive or inductive (i.e. reactive) unbalance in the motor.
 \n* **Effect**\n
The current unbalance in the motor will lead to increase in Negative sequence current harmonics(Figure) thereby increasing the Current THD of machine.(Figure)
A current unbalance will generate excess heat which can melt insulation, leading to stator winding faults and hence a further current unbalance. Unbalance will also result in an uneven torque being produced by the electric motor, reducing its efficiency, and increasing vibration. This will damage the motor and driven equipment.
 \n* **Diagnosis** \n
The IEEE standard (IE2) for voltage and current unbalances in industrial applications is to set a maximum threshold of 1%.  As a rule of thumb 1% voltage unbalance leads to 5% current unbalance which causes a 10° heat increase.  This heat increase can half the life of the motor.
If a very high current unbalance is present without a corresponding voltage unbalance, then this could be a sign of a fault in one of the phases. However, as noted earlier, current unbalance is almost always higher than voltage unbalance.
''')
st.table(dfTable)
st.table(dfTable1)
st.markdown('''
 \n* **Action** \n
If the current unbalance is due to a reactive unbalance in the stator windings, they will have to be re-wound or replaced if damaged. If it is due to a voltage unbalance the incoming supply system should be checked for faults. See the voltage unbalance diagnostic sheet for more information on this.
''')
st.image(image, caption='Visual Current unbalance: Clear current unbalance - Red phase has a different RMS value compared with the other 2 phases.')
st.sidebar.image(logo, use_column_width=True)
df.sort_index(inplace = True,ascending=False)
fig = px.line(df, x=df.index, y="avg_thd",facet_col='name', facet_col_wrap=2,height=600, facet_row_spacing=0.08,facet_col_spacing=0.08, width= 1000,#color=if "avg_i_rms">50:'r';else:'g',
              title="Daily average THD of the machines")
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.update_xaxes(showticklabels=True)
fig.update_yaxes(showticklabels=True)
fig.update_yaxes(matches=None)

st.plotly_chart(fig)
st.markdown(''' \* For these graphs Please visit analyse page of spidersense™''')
st.write("[Analyse page of spidersense™ ](https://d2usohdxpgrgb9.cloudfront.net/console/analytics)")
