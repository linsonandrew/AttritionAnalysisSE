import streamlit as st
import pandas as pd
from logist import mega
import time

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


elif st.session_state['input'] == 'No':

    st.title("Input page")

    st.header("Please chose the dataset.")
    df = pd.read_csv("format.xls")

    st.subheader("This is the required format:")
    st.dataframe(df)

    temp = st.subheader("Drag or select your file")
    data = st.file_uploader("")

    if data is not None:

        st.subheader("This is the selected file")
        df= pd.read_csv(data)
        st.dataframe(df)
    
        st.subheader("Does this data look correct?")
        col = st.columns(9)
        acc = col[0].button("Yes")
        rej = col[1].button("No")

        if acc:

            st.session_state['input'] = 'Yes'
            st.session_state['model_res'] = df
            st.experimental_rerun()
        
        elif rej:

            st.session_state['input'] = 'No'
            st.success("You can change the selected file :)")

else:

    st.title("Click the button to run the model")
    a = st.button("Click me to run the models!")
    b = st.button("Click this to change data")

    if b:

        st.session_state['input'] = 'No'
        st.experimental_rerun()


    if a:

        if st.session_state['model'] == 'Yes':
            st.error("Please reinput the data.")

        else:
            data1 = pd.read_csv(r'HR_Dataset.xls')
            print("MODEL ONCE                            OMG BRO")
            
            #Animation options
            #https://lottiefiles.com/82707-finish-tick-animation
            #https://lottiefiles.com/95088-success
            
            with st.spinner("Model 1 is running"):

                st.session_state['model_res'] = mega(st.session_state['model_res'])
            
            st.success("Model 1 has finished")

            with st.spinner("Model 2 is running"):
                
                time.sleep(8)

            st.success("Model 2 has finished")

            with st.spinner("Model 3 is running"):
                
                time.sleep(4)    

            st.success("Model 3 has finished")
            
            st.session_state['model'] = 'Yes'

