# app.py

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Create a simple DataFrame for demonstration
df = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
})

# Streamlit app begins here
st.title('Streamlit Docker Example')

# Display a DataFrame
st.write('Displaying a random DataFrame:')
st.write(df)

# Create an interactive scatter plot using Altair
scatter_chart = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y',
    tooltip=['x', 'y']
).interactive()

# Display the scatter plot
st.write('Interactive Scatter Plot:')
st.altair_chart(scatter_chart, use_container_width=True)

