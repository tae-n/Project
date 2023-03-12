import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("Opposite Diretion - Both Going Straight - Sideswipe")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [2494, 1630, 809, 180]}))
 
label_w26 = 'CLear', 'Raining', 'Overcast', 'Other'
size_w26 = [2494, 1630, 809, 180]

fig_w26, ax_w26 = plt.subplots()
ax_w26.pie(size_w26, labels=label_w26, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig_w26)
   
st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [2728, 2130, 97]}))

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Dark', 'Daylight', 'Dawn', 'Dusk', 'Other'],
    'Count': [2604, 2175, 129, 128, 88]}))
