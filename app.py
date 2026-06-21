
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Exercise Bootcamp", page_icon="🏃")
st.title("Exercise Data Analysis with python")
st.write("welcome to our dashboard")
st.divider()

st.subheader("average calories by gender")
gender_data = {
"male" : 105.5,
"female" : 95.2
}
selected_gender = st.selectbox("Select a gender to see average calories:", list(gender_data.keys()))
st.success(f"Average calories: {gender_data[selected_gender]}")
 
st.divider()
st.subheader("heart rate by duration")
duration_data = {
'Duration':['5 min','10 min','15 min','20 min','25 min'],
'Heart_Rate' : [85, 90, 95, 100, 105]
}
df = pd.DataFrame(duration_data)
st.bar_chart(data=df, x='Duration', y='Heart_Rate')
