import base64 
import streamlit as st
import os
import streamlit.components as stc
import time

def exe_downloader():
    with open (r"./dist/encrypt.exe", 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/exe;base64,{bin_str}" download="{os.path.basename(r"./dist/encrypt.exe")}">Click Me!!</a>'
    return href

st.markdown(exe_downloader(), unsafe_allow_html= True) 