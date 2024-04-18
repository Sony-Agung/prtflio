import streamlit as st
import pandas as pd
import plotly.express as px
import pygwalker as pyg
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html
import streamlit.components.v1 as components

cp = pd.read_csv("pages/bankchurn.csv")
gwalker = pyg.walk(cp)

# Set page layout to wide
st.set_page_config(layout="wide")

st.write("---")
st.title("Bank Churn Data Analysis with PyGWalker Interactive Dashboard")

st.write("---")
st.subheader('Project Overview')
st.markdown("""
<p style='text-align: justify;'>
In this project, I will be building an interactive dashboard similar to Tableau using PyGWalker and Streamlit.Here, a simple yet detailed data understanding is provided, both in the data presented and in the visualization, to understand the values ​​of each data feature.
</p>
""", unsafe_allow_html=True)

st.write("---")
intro_text = """
### Introduction to PyGWalker

PyGWalker is a Python library that provides a Tableau-like UI for data exploration and visualization within Jupyter Notebook and other Jupyter-based environments. It simplifies the data analysis and visualization process by offering a no-code user interface for visual exploration. You can leverage dragging and dropping functionality to quickly create interactive visualizations without writing code.

Here are some key points about PyGWalker:

- PyGWalker is a Python binding of Graphic Walker, an open-source alternative to Tableau.
- It can take a Pandas, Polars, or Modin DataFrame and turn it into a visual exploration interface.
- PyGWalker is compatible with Jupyter Notebook, Jupyter Lab, Google Colab, Kaggle Code, Databricks Notebook, Visual Studio (with Jupyter Notebook extension), Hex Projects, IPython, and other Jupyter-based environments.
- It supports various environments, including Streamlit, Jupyter Extension for Visual Studio Code, and most web applications compatible with IPython kernels.
- PyGWalker can be installed using pip with the command pip install pygwalker. You can also use conda to install it with conda install -c conda-forge pygwalker.
- The library provides configuration options, such as privacy settings, that can be modified using the command line interface or through Python code.

Please note that PyGWalker may have specific use cases or limitations that are not covered in the available information. It's always a good idea to refer to the official documentation and examples provided by the library's creators for more detailed information on how to use PyGWalker in your projects.

"""
st.markdown(intro_text)
st.write("[Documentation](https://docs.kanaries.net/pygwalker)")


st.write("---")
st.subheader("Bank Churn Data")
st.dataframe(cp)


st.write("---")
st.subheader("PyGWalker Interactive Dashboard")
st.write("[Watch the demo first !!](https://drive.google.com/file/d/1GUAnClV-P8PpeZZHstkTuZu23NmT1V_L/view?usp=sharing)")


df = pd.read_csv("pages/bankchurn.csv")
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
components.html(pyg_html, height=800, scrolling=True)

