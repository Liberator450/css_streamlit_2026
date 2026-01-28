# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello, I hope you are having a great day")

st.title("Let me introduce you to my world")

st.write("I am just a boy")

st.header("Rate me out of 10")

number = st.slider("Pick a number", 1, 10)
st.write(f"You picked: {number}")