
import streamlit as st
import pandas as pd
import os

# st.sidebar.subheader(st.session_state)

menu = ["South", "North", "East", "West"]
choice = st.sidebar.selectbox("Choose your region", menu)



if choice == "South":
    html_temp = '''
    <div style="background-color:#f2b016;padding:1.5px">
    <h1 style="color:white;text-align:center;">South Indian Diet Plan</h1>
    </div><br>'''
    st.markdown(html_temp,unsafe_allow_html=True)

    image_filenames = os.listdir('images/South')
    for filename in image_filenames:
        st.image(f'images/South/{filename}')

elif choice == "North":
    html_temp = '''
    <div style="background-color:#f2b016;padding:1.5px">
    <h1 style="color:white;text-align:center;">North Indian Diet Plan</h1>
    </div><br>'''
    st.markdown(html_temp,unsafe_allow_html=True)

    image_filenames = os.listdir('images/North')
    for filename in image_filenames:
        st.image(f'images/North/{filename}')

elif choice == "East":
    html_temp = '''
    <div style="background-color:#f2b016;padding:1.5px">
    <h1 style="color:white;text-align:center;">East Indian Diet Plan</h1>
    </div><br>'''
    st.markdown(html_temp,unsafe_allow_html=True)

    image_filenames = os.listdir('images/East')
    for filename in image_filenames:
        st.image(f'images/East/{filename}')

elif choice == "West":
    html_temp = '''
    <div style="background-color:#f2b016;padding:1.5px">
    <h1 style="color:white;text-align:center;">West Indian Diet Plan</h1>
    </div><br>'''
    st.markdown(html_temp,unsafe_allow_html=True)

    image_filenames = os.listdir('images/West')
    for filename in image_filenames:
        st.image(f'images/West/{filename}')