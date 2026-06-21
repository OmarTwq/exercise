import streamlit as st
import pandas as pd

st.set_page_config(page_title="Exercise Data Bootcamp", page_icon="🏃", layout="wide")

st.title("🏃‍♂️ Data Analysis Bootcamp - Exercise Dataset")
st.write("لوحة تحكم لتحليل بيانات التمارين الرياضية والسعرات الحرارية")
st.divider()

uploaded_file = st.file_uploader("قم برفع ملف exercise.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    for col in ['Age', 'Duration', 'Heart_Rate', 'Height']:
        if col in df.columns and df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    st.success(" تم تحميل البيانات وتنظيفها بنجاح")

    st.subheader(" نظرة عامة على البيانات")
    col1, col2, col3 = st.columns(3)
    col1.metric("عدد السجلات", df.shape[0])
    col2.metric("عدد الأعمدة", df.shape[1])
    col3.metric("القيم المفقودة المتبقية", int(df.isnull().sum().sum()))

    st.dataframe(df.head(10))
    st.divider()

    st.subheader("🧍 فلترة البيانات حسب الجنس")
    gender_options = ["الكل"] + sorted(df['Gender'].unique().tolist())
    selected_gender = st.selectbox("اختر الجنس:", gender_options)

    if selected_gender != "الكل":
        filtered_df = df[df['Gender'] == selected_gender]
    else:
        filtered_df = df

    st.write(f"عدد السجلات بعد الفلترة: **{filtered_df.shape[0]}**")
    st.divider()

    st.subheader(" المؤشرات الإحصائية الرئيسية")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("متوسط العمر", f"{filtered_df['Age'].mean():.1f}")
    m2.metric("متوسط مدة التمرين (دقيقة)", f"{filtered_df['Duration'].mean():.1f}")
    m3.metric("متوسط معدل النبض", f"{filtered_df['Heart_Rate'].mean():.1f}")
    m4.metric("متوسط السعرات المحروقة", f"{filtered_df['Calories'].mean():.1f}")
    st.divider()

    st.subheader(" العلاقة بين مدة التمرين والسعرات الحرارية المحروقة")
    chart_data = filtered_df[['Duration', 'Calories']].sort_values('Duration')
    st.scatter_chart(chart_data, x='Duration', y='Calories')
    st.divider()

    st.subheader("👤 متوسط السعرات المحروقة حسب فئة العمر")
    bins = [0, 20, 30, 40, 50, 60, 70, 100]
    labels = ['<20', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
    filtered_df = filtered_df.copy()
    filtered_df['Age_Group'] = pd.cut(filtered_df['Age'], bins=bins, labels=labels)
    age_group_avg = filtered_df.groupby('Age_Group')['Calories'].mean().reset_index()
    st.bar_chart(data=age_group_avg, x='Age_Group', y='Calories')
    st.divider()

    st.subheader(" توزيع معدل النبض (Heart Rate)")
    st.bar_chart(filtered_df['Heart_Rate'].value_counts().sort_index())
    st.divider()

    st.subheader(" الإحصاء الوصفي الكامل")
    st.dataframe(filtered_df.describe())

    st.divider()
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" تحميل البيانات بعد التنظيف",
        data=csv,
        file_name="clean_exercise.csv",
        mime="text/csv"
    )

else:
    st.info(" يرجى رفع ملف exercise.csv للبدء في عرض التحليل")
