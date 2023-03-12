import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Collisions in Seattle"
st.table(pd.DataFrame({
    'Collision Type': ['Opposite Direction - Both Going Straight - Sideswipe', 'Motor Vehicle Struck Pedalcyclist, Front End at Angle', 'From Opposite Direction - One Left Turn - One Straight', 'From Same Direction -Both Going Straight-Both Moving- Sideswipe', 'From Same Direction - Both Going Straight - One Stopped - Rear End', 'From Opposite Direction - Both Moving - Head On']
    'Number of Incidents': [98302, 64094, 10664, 8318, 5399, 3771]
    'Injuries': [40706, 27831, 3791, 8571, 1885, 3561]
    'Fatalities': [84, 16, 81, 171, 32, 25]}))

st.title("Opposite Direction - Both Going Straight - Sideswipe")
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

label_l26 = 'Dark', 'Daylight', 'Other'
size_l26 = [2604, 2175, 345]
fig_l26, ax_l26 = plt.subplots()
ax_l26.pie(size_l26, labels=label_l26, autopct='%1.1f%%', startangle=90)
ax_l26.axis('equal')  
st.pyplot(fig_l26)

st.title("Motor Vehicle Struck Pedalcyclist, Front End at Angle")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Overcast', 'Raining', 'Other'],
    'Count': [2561, 522, 401, 84]}))
 
label_w18 = 'Clear', 'Overcast', 'Raining', 'Other'
size_w18 = [2561, 522, 401, 84]
fig_w18, ax_w18 = plt.subplots()
ax_w18.pie(size_w18, labels=label_w18, autopct='%1.1f%%', startangle=90)
ax_w18.axis('equal')  
st.pyplot(fig_w18)

st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [2853, 630, 84]}))

label_r18 = 'Dry', 'Wet', 'Other'
size_r18 = [2728, 2130, 97]
fig_r18, ax_r18 = plt.subplots()
ax_r18.pie(size_r18, labels=label_r18, autopct='%1.1f%%', startangle=90)
ax_r18.axis('equal')  
st.pyplot(fig_r18)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Other'],
    'Count': [2682, 684, 151, 165, 55]}))

label_l18 = 'Daylight', 'Dark', 'Other'
size_l18 = [2682, 684, 271]
fig_l18, ax_l18 = plt.subplots()
ax_l18.pie(size_l18, labels=label_l18, autopct='%1.1f%%', startangle=90)
ax_l18.axis('equal')  
st.pyplot(fig_l18)

st.title("From Opposite Direction - One Left Turn - One Straight ")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [5514, 2220, 1763, 532]}))
 
label_w28 = 'Clear', 'Overcast', 'Raining', 'Other'
size_w28 = [5514, 2220, 1763, 532]
fig_w28, ax_w28 = plt.subplots()
ax_w28.pie(size_w28, labels=label_w28, autopct='%1.1f%%', startangle=90)
ax_w28.axis('equal')  
st.pyplot(fig_w28)

st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Ice', 'Other'],
    'Count': [6039, 3329, 251, 448]}))

label_r28 = 'Dry', 'Wet', 'Ice', 'Other'
size_r28 = [6039, 3329, 251, 448]
fig_r28, ax_r28 = plt.subplots()
ax_r28.pie(size_r28, labels=label_r28, autopct='%1.1f%%', startangle=90)
ax_r28.axis('equal')  
st.pyplot(fig_r28)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Dark', 'Daylight', 'Dusk', 'Dawn', 'Other'],
    'Count': [5268, 4084, 243, 216, 240]}))

label_l28 = 'Dark', 'Daylight', 'Dusk', 'Dawn', 'Other'
size_l28 = [5268, 4084, 243, 216, 240]
fig_l28, ax_l28 = plt.subplots()
ax_l28.pie(size_l28, labels=label_l28, autopct='%1.1f%%', startangle=90)
ax_l28.axis('equal')  
st.pyplot(fig_l28)

st.title("From Same Direction -Both Going Straight-Both Moving- Sideswipe ")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [55191, 16125, 13970, 4336]}))
 
label_w11 = 'Clear', 'Raining', 'Overcast', 'Other'
size_w11 = [55191, 16125, 13970, 4336]
fig_w11, ax_w11 = plt.subplots()
ax_w11.pie(size_w11, labels=label_w11, autopct='%1.1f%%', startangle=90)
ax_w11.axis('equal')  
st.pyplot(fig_w11)

st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [62354, 23133, 4156]}))

label_r11 = 'Dry', 'Wet', 'Other'
size_r11 = [62354, 23133, 4156]
fig_r11, ax_r11 = plt.subplots()
ax_r11.pie(size_r11, labels=label_r11, autopct='%1.1f%%', startangle=90)
ax_r11.axis('equal')  
st.pyplot(fig_r11)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Other'],
    'Count': [59850, 22579, 3026, 1115, 3006]}))

label_l11 = 'Dark', 'Daylight', 'Dusk', 'Dawn', 'Other'
size_l11 = [59850, 22579, 3026, 1115, 3006]
fig_l11, ax_l11 = plt.subplots()
ax_l11.pie(size_l11, labels=label_l11, autopct='%1.1f%%', startangle=90)
ax_l11.axis('equal')  
st.pyplot(fig_l11)

st.title("From Same Direction - Both Going Straight - One Stopped - Rear End  ")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [34489, 10254, 8537, 3606]}))
 
label_w14 = 'Clear', 'Raining', 'Overcast', 'Other'
size_w14 = [34489, 10254, 8537, 3606]
fig_w14, ax_w14 = plt.subplots()
ax_w14.pie(size_w14, labels=label_w14, autopct='%1.1f%%', startangle=90)
ax_w14.axis('equal')  
st.pyplot(fig_w14)

st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [38551, 14718, 3629]}))

label_r14 = 'Dry', 'Wet', 'Other'
size_r14 = [38551, 14718, 3629]
fig_r14, ax_r14 = plt.subplots()
ax_r14.pie(size_r14, labels=label_r14, autopct='%1.1f%%', startangle=90)
ax_r14.axis('equal')  
st.pyplot(fig_r14)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Other'],
    'Count': [36961, 14694, 1798, 742, 2652]}))

label_l14 = 'Dark', 'Daylight', 'Dusk', 'Dawn', 'Other'
size_l14 = [36961, 14694, 1798, 742, 2652]
fig_l14, ax_l14 = plt.subplots()
ax_l14.pie(size_l14, labels=label_l14, autopct='%1.1f%%', startangle=90)
ax_l14.axis('equal')  
st.pyplot(fig_l14)

st.title("From Opposite Direction - Both Moving - Head On")
st.write("Weather")

st.table(pd.DataFrame({
    'Weather': ['Clear', 'Raining', 'Overcast', 'Other'],
    'Count': [4602, 1921, 1148, 256]}))
 
label_w24 = 'Clear', 'Raining', 'Overcast', 'Other'
size_w24 = [4602, 1921, 1148, 256]
fig_w24, ax_w24 = plt.subplots()
ax_w24.pie(size_w24, labels=label_w24, autopct='%1.1f%%', startangle=90)
ax_w24.axis('equal')  
st.pyplot(fig_w24)

st.write("Road Condition")

st.table(pd.DataFrame({
    'Road': ['Dry', 'Wet', 'Other'],
    'Count': [5198, 2507, 228]}))

label_r24 = 'Dry', 'Wet', 'Other'
size_r24 = [5198, 2507, 228]
fig_r24, ax_r24 = plt.subplots()
ax_r24.pie(size_r24, labels=label_r24, autopct='%1.1f%%', startangle=90)
ax_r24.axis('equal')  
st.pyplot(fig_r24)

st.write("Light Conditions")

st.table(pd.DataFrame({
    'Light': ['Daylight', 'Dark', 'Dusk', 'Dawn', 'Other'],
    'Count': [4551, 2811, 277, 168, 122]}))

label_l24 = 'Dark', 'Daylight', 'Dusk', 'Dawn', 'Other'
size_l24 = [4551, 2811, 277, 168, 122]
fig_l24, ax_l24 = plt.subplots()
ax_l24.pie(size_l24, labels=label_l24, autopct='%1.1f%%', startangle=90)
ax_l24.axis('equal')  
st.pyplot(fig_l24)

