import streamlit as st
import pandas as pd
import plotly.express as px
import pygwalker as pyg
import tempfile
import base64
from PIL import Image

def resize_image(input_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = width / height
    new_height = size
    new_width = int(new_height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height))
    return resized_image

st.set_page_config(layout="wide")

st.write("---")
st.title("Data Visualization and Analysis")

st.write("---")
st.subheader('Project Overview')
st.markdown("""
<p style='text-align: justify;'>
Welcome to a data-driven voyage where I fuse useful art data visualization with insightful analysis. My distinctive style merges creativity and precision, 
breathing life into complex datasets, and translating them into compelling visuals that resonate. Delving into data's depths, I uncover hidden patterns while 
keeping the broader context in sight, providing holistic insights for informed decisions. Crafting data analysis reports is an art in itself; my approach weaves clarity and usability into every word and visualization, 
presenting a harmonious narrative that guides readers through findings, analysis, and actionable conclusions. Get ready to experience a symphony of data where information takes form,
and insights are elegantly unveiled.
</p>
""", unsafe_allow_html=True)


st.write("---")
st.subheader('Data Visualisasi')
st.write("[Take a look at the dataset >](https://drive.google.com/file/d/1yIIT8YJKeljClfMvTQ4RGI_SKfl244-q/view?usp=sharing)")
st.markdown("""
<p style='text-align: justify;'>
This project aims to provide comprehensive insights into customer behavior in the banking industry and how certain factors can contribute to their success in subscribing to banking services. The results of this analysis are expected to assist banks in developing more effective customer retention strategies and improving the overall customer experience.
</p> <p style='text-align: justify;'>
Now let's examine the correlation of each feature that needs to be analyzed!
There are features <b>gender, age, balance, activated_member & country</b> to be analyzed.
</p>
""", unsafe_allow_html=True)

show_image = "images/corr.png"  
st.image(show_image, width=5, use_column_width=True)

st.write("---")
st.subheader('Data Report')


show_image = "images/looker.png"  
st.image(show_image, width=100, use_column_width=True)
st.markdown("""
<p style='text-align: justify;'>
1. <b>Churn</b> : The Pie Chart shows the proportion of the number of customers who churned and retained. Out of a total of 10,000 customers, 20.4% (2,040 customers) are churned, while 79.6% (7,960 customers) are retained..<br>
2. <b>Gender </b>: Berdasarkan gender, ratio churn terbesar terjadi pada Female sebesar 0.250715,
Perubahan dalam prioritas atau kebutuhan pelanggan Female dapat memengaruhi
keputusan mereka untuk berhenti menggunakan layanan atau produk tertentu.<br>
3.<b>Age</b> : It shows that individuals in the age range of 49 to 57 years are more likely to stop using the service. At this age, many people face greater financial burdens, such as buying a house, educating children, and preparing for retirement. This can shift their financial priorities and lead them to reduce unnecessary expenses, including service subscriptions.<br> 
4.<b>Balance</b> : Based on the balance of money in the customer's account (balance), it is observed that the largest churn occurs in the balance group > 200,001 with a proportion of 55%, while the smallest churn occurs in the balance group between 50,001 - 100,000 with a proportion of 20%.<br>
5.<b>Active Member</b> : This finding indicates that non-active users are more likely to stop using the service ("churn"). It means that those who are inactive in using the service tend to abandon it.<br>
6. <b>Country</b> : Based on country, the largest churn ratio occurs for Germany at 0.324432, followed by Spain and France at 0.166734 and 0.161548, respectively.

</p>
""", unsafe_allow_html=True)





st.write("---")
st.subheader('Suggestions')


show_image = "images/suges.png"  
st.image(show_image, width=100, use_column_width=True)

st.write("---")
st.subheader('More Data Analysis')
st.markdown('<h2 style="font-size: 31px; text-align: center;">🙀 Sorry This Section is Under Development 😿</h2>', unsafe_allow_html=True)

