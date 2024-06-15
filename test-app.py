
import streamlit as st

import pandas as pd 

st.write("hl st")
sds = st.text_input("favorite film ? ")
st.write(sds)

st.button("clikc")


dt = pd.read_csv("./movies.csv")

st.write(dt)