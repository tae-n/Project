import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("Opposite Diretion - Both Going Straight - Sideswipe")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [2494, 1630, 809, 180]}))
 
label_w26 = 'Clear', 'Raining', 'Overcast', 'Other'
size_w26 = [2494, 1630, 809, 180]
fig_w26, ax_w26 = plt.subplots()
ax_w26.pie(size_w26, labels=label_w26, autopct='%1.1f%%', startangle=90)
ax_w26.axis('equal')  
st.pyplot(fig_w26)
   
st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [2728, 2130, 97]}))

label_r26 = 'Dry', 'Wet', 'Other'
size_r26 = [2728, 2130, 97]
fig_r26, ax_r26 = plt.subplots()
ax_r26.pie(size_r26, labels=label_r26, autopct='%1.1f%%', startangle=90)
ax_r26.axis('equal')  
st.pyplot(fig_r26)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Dark', 'Daylight', 'Dawn', 'Dusk', 'Other'],
    'Count': [2604, 2175, 129, 128, 88]}))

label_l26 = 'Dark', 'Daylight', 'Dawn', 'Dusk', 'Other'
size_l26 = [2604, 2175, 129, 128, 88]
fig_l26, ax_l26 = plt.subplots()
ax_l26.pie(size_l26, labels=label_l26, autopct='%1.1f%%', startangle=90)
ax_l26.axis('equal')  
st.pyplot(fig_l26)
