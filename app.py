import os
import openpyxl
import json
import requests
import streamlit as st
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage
from streamlit_lottie import st_lottie
from st_aggrid import AgGrid
from datetime import datetime
import streamlit.components.v1 as components
import altair as alt
import streamlit as st

action = st.sidebar.radio("Choose one of the following options -", ("Home", "Donors Data", "Receivers Data", "Contact"))
with st.sidebar:
    
    def load_lottieurl(url:str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()
    lottie_animation = load_lottieurl("https://lottie.host/77a4caff-8adb-4cea-9e4f-4a278c3d365a/Yr5u13yEZm.json")
    st_lottie(lottie_animation, key="animation")
st.sidebar.markdown("Made by - Tulip Aggarwal")

#Main home page
if action == "Home":
    st.title("Ahaar")  
    st.subheader("Feeding Generations")
    st.markdown("This project showcases the visualizations of the stakeholder data for Aahaar which is a web portal that connects surplus food nodes like banquet halls and caterers with people in need through NGOs, orphanages, and old age homes to donate the surplus food post social events.")
    st.markdown("Ahaars aim to develop an effective and sustainable solution to manage food waste that addresses the root causes of food waste and reduces waste at every stage of the food supply chain. This includes tackling issues such as overproduction, spoilage, improper storage and transportation, and changing consumer behavior to minimize waste")
    
    st.markdown("The visualizations shown in this project are made using the following datasets - ")
    col1, col2 = st.columns((1,2.5))
    with col1:
        def embed_donor_button(link_url, button_label):
            link_button = f'<a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vT27w0PecMYVj-gVmMPedf7Vwhg9Sqq7m5dbzyDgU8cXHFOLzfZQaPRHa2V51BPKAgLl0HLGHnsW77M/pub?gid=0&single=true&output=csv" target="_blank"><button>{button_label}</button></a>'
            st.markdown(link_button, unsafe_allow_html=True)
        # Call the function to embed the link in a button
        embed_donor_button("https://docs.google.com/spreadsheets/d/e/2PACX-1vT27w0PecMYVj-gVmMPedf7Vwhg9Sqq7m5dbzyDgU8cXHFOLzfZQaPRHa2V51BPKAgLl0HLGHnsW77M/pub?gid=0&single=true&output=csv", "Download Donors Dataset")
    
    with col2:
        def embed_receiver_button(link_url, button_label):
            link_button = f'<a href="https://docs.google.com/spreadsheets/d/e/2PACX-1vT27w0PecMYVj-gVmMPedf7Vwhg9Sqq7m5dbzyDgU8cXHFOLzfZQaPRHa2V51BPKAgLl0HLGHnsW77M/pub?gid=611349706&single=true&output=csv" target="_blank"><button>{button_label}</button></a>'
            st.markdown(link_button, unsafe_allow_html=True)
        # Call the function to embed the link in a button
        embed_receiver_button("https://docs.google.com/spreadsheets/d/e/2PACX-1vT27w0PecMYVj-gVmMPedf7Vwhg9Sqq7m5dbzyDgU8cXHFOLzfZQaPRHa2V51BPKAgLl0HLGHnsW77M/pub?gid=611349706&single=true&output=csv", "Download Receivers Dataset")

    

elif action == "Donors Data":

    st.title("Ahaar")
    st.subheader("Donors Data")
    st.markdown("By connecting food donors with food banks, shelters, and other organizations that distribute food, the website can help ensure that those in need have access to nutritious food. This can be especially important in areas where food insecurity is a significant issue, or during times of crisis or emergency.")
    
    tableau_embed_code = """
        <iframe src="https://public.tableau.com/views/DonorDataVisualization_16844426074900/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link?:showVizHome=no&:embed=true" width="100%" height="950" frameborder="0"></iframe>
    """

    # Embed the Tableau dashboard using components.iframe
    st.markdown(tableau_embed_code, unsafe_allow_html=True)

elif action == "Receivers Data":
    st.title("Ahaar")
    st.subheader("Receivers Data")
    st.markdown("For a food receiver, the website plays a crucial role in connecting them with food donors, food banks, shelters, and other organizations dedicated to distributing food. This connection ensures that they have access to nutritious food when they are in need. Particularly in areas where food insecurity is a prevalent concern or during times of crisis or emergency, this platform becomes even more vital.")
    
    tableau_embed_code = """
        <iframe src="https://public.tableau.com/views/ReceiversData1/ReceiversData?:language=en-US&:display_count=n&:origin=viz_share_link?:showVizHome=no&:embed=true" width="100%" height="950" frameborder="0"></iframe>
    """
    # Embed the Tableau dashboard using components.iframe
    st.markdown(tableau_embed_code, unsafe_allow_html=True)

elif action == "Contact":

    st.title("Ahaar")
    st.subheader("Contact me")
    # Define the HTML code for the buttons
    linkedin_button = '<a href="https://www.linkedin.com/in/tulipaggarwal/" target="_blank" style="text-align: center; margin: 0px 10px; padding: 5px 10px; border-radius: 5px; color: white; background-color: #0077B5; text-decoration: none">LinkedIn</a>'
    github_button = '<a href="https://github.com/TulipAggarwal" target="_blank" style="text-align: center; margin: 0px 10px; padding: 5px 10px; border-radius: 5px; color: white; background-color: #24292E; text-decoration: none">GitHub</a>'
    # Display the buttons in the app
    st.markdown(f'{linkedin_button} {github_button} ', unsafe_allow_html=True)

    #Contact form
    st.markdown('Please fill out the form below to contact me. Thank you so much!')

    # Define the form fields
    with st.form('Contact Form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        message = st.text_area('Message')
        submit_button = st.form_submit_button(label='Submit')

    # Process the form submission
    if submit_button:
        # Send the form data to a backend service, or save it to a database
        # Here, we're simply printing the form data to the console
        print(f'Name: {name}')
        print(f'Email: {email}')
        print(f'Message: {message}')
        st.success('Thank you for reaching out to me. I will get back to you as soon as possible.')
