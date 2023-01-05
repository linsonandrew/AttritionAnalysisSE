import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Attrition Solver",
    page_icon="shark",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/wambyat/AttritionAnalysisSE',
        'Report a bug': "https://github.com/wambyat/AttritionAnalysisSE",
        'About': "This application will figure out which of your employees are most likely to leave. It can also tell you why and suggest a few basic solutions. Call 1800-this-a-proj for addition help"
    }
)

# Initializing all the session_state variables
#This is tecnically a leftover
# reused to track which solutions have been chosen
if 'page' not in st.session_state:

    st.session_state['page'] = {}

#This is tecnically a leftover
# Reused to track which employee is selected
if 'inp' not in st.session_state:

    st.session_state['inp'] = 'default'

#This is used to track if the user has logged in
if 'login' not in st.session_state:

    st.session_state['login'] = 'No'

#This is used to track if the input is given.
if 'input' not in st.session_state:

    st.session_state['input'] = 'No'

#This is also used to track user login
#TODO Merge this and 'login'
if 'login_test' not in st.session_state:

    st.session_state['login_test'] = 0

if 'model' not in st.session_state:
    st.session_state['model'] = 'No'
    

if st.session_state['login'] == 'No':

    st.title("Please go to login page and login first!")

elif st.session_state['model'] == 'No':
    st.title("Please give an input and run the model.")
    st.subheader("Navigate to the input page to do this.")

else:

    st.title("Images you can use")

    d = {"Employees Left vs Employees not Left" : "Graph depicting  count of Employees Left vs not Left","Number of Projects Per Employee":"","DEPARTMENTS VS LEFT":"Relationship between Departmants and count of employees who leave ","atrributes vs left":"attributes vs Employees who leave "}

    temp = [str(i) for i in d.keys()]
    tabs_list = st.tabs(temp)

    for i in range(len(tabs_list)):
        
        with tabs_list[i]:
            

            img = Image.open(str(list(d.keys())[i])+".png")
            if img.size[1]>500:
                x = 900 / img.size[0]
                img = img.resize((int(img.size[0]*x),(int(img.size[1]*x))))

            st.subheader(d[str(list(d.keys())[i])])
            st.image(img)
            
