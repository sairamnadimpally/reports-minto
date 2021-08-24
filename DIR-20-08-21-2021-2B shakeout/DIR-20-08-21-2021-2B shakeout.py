
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
import psycopg2
from datetime import date
from datetime import timedelta
from PIL import Image
Descrption1='''
**Warning Indication:**
\n
The THD of the machine is high from 1st June 2021, it has a increasing trend since then Ref(THD).
\n
'''
Descrption4='''
**Diagnosis:**

\n
* 2-B shakeout has NJ 310 C4 bearing.  Bearing frequencies are as follows, Ball Passing Outer Race (BPFO)=81.3008; Ball Passing Inner Race (BPFI)=118.6192;	Ball Spin Frequency(BSF)=6.8306; Cage Frequency:42.8162.
\n
* Increase of energies at Bearing(11FS-BPFI=384 Hz, 13FS-BPFI=484Hz) frequencies the motor is observed. Ref(Increase in energies at 11FS-BPFI in the spectrum) Ref (Trend of energies at  11FS-BPFI frequency).
'''
Descrption2='''
**Possible Root Cause:**
\n
* 2-B shakeout is changed multiple times since march 2021(Ref RPM Speed representing machine change).
\n
Even the machine is changed the odd Harmonics are getting increased Ref(Increase in energies at harmonics in the spectrum), Ref (Trend of 5th Harmonic of Fundamental frequency). It is increasing irrespective of Machine changes. This increase could cause increase in bearing frequencies. \n

'''
Descrption3='''
**Effects of Increased Harmonics:**
\n
* Harmonics losses manifest as additional heat.  It can cause bearing grease to loose lubricity, and can degrade winding insulation therby reduces motor's life. Depending on the level of harmonics present, the heat generated may cause the tripping of thermal protection systems in your motors.\n
'''



image2= Image.open("RPMspeed4Machinechanges.jpg")
image1= Image.open("THD.jpg")
image3= Image.open("IncreasedHarmonics.jpg")
image4= Image.open("IncreasedHarmonics FFA.jpg")
image5= Image.open("11FS-BPFI-FFA.jpg")
image6= Image.open("11FS-BPFI.jpg")
image7= Image.open("11FS-BPFI instant.jpg")
logo =Image.open(r"logo small.png")
#st.image(image, caption='Example to Understand Current unbalance: Clear current unbalance - Red phase has a different RMS value compared with the other 2 phases.')
st.title('DIR-20-08-21-2021-2B Stationary shakeout')
st.markdown('**Machine Insight**')
st.markdown(Descrption1)

st.image(image1, caption='THD')

st.markdown(Descrption4)
st.image(image6, caption='Increase in energies at 11FS-BPFI in the spectrum')
st.image(image5, caption='Trend of energies at  11FS-BPFI frequency(Daily)')
st.image(image7, caption='Trend of energies at  11FS-BPFI frequency (Instant)')
st.markdown(Descrption2)
st.image(image2, caption='RPM Speed representing machine change')
st.image(image3, caption='Increase in energies at harmonics in the spectrum')
st.image(image4, caption='Trend of 5th Harmonic of Fundamental frequency')
st.markdown(Descrption3)
st.sidebar.image(logo, use_column_width=True)
st.write("[Vist spidersense™ for more analysis](https://d2usohdxpgrgb9.cloudfront.net/console/analytics)")
