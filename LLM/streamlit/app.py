import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

#  create a sample DataFrame

df = pd.DataFrame({
    'first_column': [1, 2, 3, 4, 5],
    'second_column': [10, 20, 30, 40, 50],
})

st.write("Here is a sample DataFrame:")
st.write(df)

# Create a simple line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a', 'b', 'c']
)
st.line_chart(chart_data)