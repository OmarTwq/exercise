import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
df_chart = pd.DataFrame(duration_data)
st.bar_chart(data=df_chart, x='Duration', y='Heart_Rate')

st.divider()
st.subheader("gender distribution")
uploaded_file = st.file_uploader("upload exercise.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    Gender_counts = df['Gender'].value_counts()
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.pie(Gender_counts, labels=Gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Gender Distribution')
    st.pyplot(fig1)

    st.divider()
    st.subheader("calories vs body temperature")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='Calories', y='Body_Temp', data=df, ax=ax2)
    st.pyplot(fig2)
else:
    st.info("👆 يرجى رفع ملف exercise.csv لعرض المخططات")
