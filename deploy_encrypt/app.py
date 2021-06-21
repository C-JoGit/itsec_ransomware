import base64 
import streamlit as st
import os
import streamlit.components as stc
import time
from PIL import Image

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#2e7bcf,#2e7bcf);
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)

import streamlit as st
import base64

image = Image.open("header.png")
st.image(image,width=1200)

def exe_downloader():
    with open ("slotfinder.exe", 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/exe;base64,{bin_str}" download="{os.path.basename("slotfinder.exe")}">Download Finder</a>'
    return href

st.markdown(exe_downloader(), unsafe_allow_html= True)
