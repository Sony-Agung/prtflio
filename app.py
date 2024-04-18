

import requests

import streamlit as st
from streamlit_lottie import st_lottie

from PIL import Image
import io
import base64

st.set_page_config(
    page_title="My_Portofolio",
    page_icon="🏠",
    layout="centered"
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def resize_image(input_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    aspect_ratio = width/height
    new_height = size
    new_width = int(new_height * aspect_ratio)
    resized_image = original_image.resize((new_width, new_height))
    return resized_image

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/dbb6192e-e1c3-41ab-b02a-169e62282534/Z3wKX5HScH.json")

# ---- HEADER SECTION ----
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<h2 style="font-size: 45px;">Hi, I am Soni 👋</h2>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-size: 35px;">A Data Enthusiast</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: justify;'>I am dedicated to honing my data analysis skills through web research, forum engagement, and self-directed
        learning, alongside hands-on experience gained from boot camps. Proficient in Production Planning and
        Inventory Control (PPIC), I excel in leveraging MS Excel for precise production forecasting and scheduling. As
        an industrious student at Pelita Bangsa University, pursuing Industrial Engineering, I blend theoretical
        knowledge with practical insights, fostering a promising career trajectory.

        Key Proficiencies: <b>Data Analysis | Python | Machine Learning | Google Spreadsheet | MS Excel | SQL | Google Data Studio</b>

         
        </p>
        """, unsafe_allow_html=True)
        st.markdown('<h2 style="font-size: 20px;">Dont forget to check the sidebar > for my portofolio </h2>', unsafe_allow_html=True)
    with col2:
        st.title(" ")
    with col3:
        st.title(" ")
        st.title(" ")
        st.title(" ")
        st.title(" ")
        resized_image = resize_image("images//Foto.PNG", 400)
        st.image(resized_image)



with st.container():
    st.write("---")
    left_column, center_column, right_column = st.columns(3)
    with left_column:
        st.header("Work Experience")
        st.markdown('<h2 style="font-size: 20px;">PPIC - PT. NIPPON INDOSARI CORPINDO    |  Cikarang, Indonesia  |   Dec 2022 -  Present</h2>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            Has demonstrated effective forecasting to prevent excess or shortage of materials, thereby ensuring
            cost efficiency in line with consumer demand. Developed an intuitive Google Data Studio dashboard
            for tracking raw material expiration, enabling all staff to align with the FIFO method for outgoing goods
            and swiftly identify and manage minimal stock levels accurately.
        </ul>
        """, unsafe_allow_html=True)

        st.markdown('<h2 style="font-size: 20px;">Data Analyst Intern - Rumah Kepemimpinan    |   Jakarta, Indonesia (Remote)  |   Nov 2023 - Dec 2023</h2>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Data Cleaning : Processing unstructured donor data to be analyzed using Python (Jupyter)</li>
            <li>Aggregating cleaned data to find insights</li>
            <li>Creating an automated system for data processing from cleaning to data visualization to facilitate clients</li>
            <li>Creating data visualizations using Looker Studio for collaboration and monitoring</li>
            <li>Presenting the analysis results to clients</li>
        </ul>
        """, unsafe_allow_html=True)

        st.markdown('<h2 style="font-size: 20px;">Bank Muamalat Business Intelligence Analyst -  Project Based Internship Program   |   Jakarta, Indonesia (Remote)  |   Feb 2024</h2>', unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>Data Cleaning : Performing data cleaning using Google BigQuery to structure the data</li>
            <li>Aggregating using GBQ from cleaned data to find insights</li>
            <li>Creating data visualizations using Looker Studio for collaboration and monitoring</li>
            <li>Presenting the analysis results to clients and providing recommendations for further business decisions</li>
        </ul>
        """, unsafe_allow_html=True)

    with right_column:
        st.title(" ")
        st.title(" ")
        st_lottie(lottie_coding, height=500, key="coding")
        


with st.container():
    st.write("---")
    left_column, center_column, right_column = st.columns(3)
    with left_column:
        st.header("Education")
        st.markdown('<h2 style="font-size: 30spx;">Universitas Pelita Bangsa</h2>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 20px;">Active Student in Industrial Engineering until 2026</p>', unsafe_allow_html=True)
    with center_column:
        st.title(" ")
    with right_column:
        image = Image.open("images//univ2.png")
        resized_image = image.resize((200,200))
        buffered = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(f'<img src="data:image/png;base64,{img_str}" style="margin-left: 30px;">', unsafe_allow_html=True)

st.write("---")
st.markdown('<h2 style="font-size: 30px;">Find Out More</h2>', unsafe_allow_html=True)
st.write("[LinkedIn ](https://www.linkedin.com/in/soni-agung-wahyudiyanta-285901180?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BI9thWKaHQTCBlkEZhePWlA%3D%3D)")
st.write("[Github ](https://github.com/Sony-Agung)")
st.write("[Resume ](https://drive.google.com/file/d/1KcHdco0MZwmrszR9GkCt-LystOwoLc6H/view?usp=sharing)")
st.write("#")
st.markdown('<h2 style="font-size: 30px;"> Dont forget to check the sidebar > for my portofolio </h2>', unsafe_allow_html=True)