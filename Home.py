import streamlit as st
import pandas as pd
from logistic import mega

if 'page' not in st.session_state:

    st.session_state['page'] = 'home'

if 'inp' not in st.session_state:

    st.session_state['inp'] = 'default'

if 'login' not in st.session_state:

    st.session_state['login'] = 'No'

if st.session_state['login'] == 'No':

    st.title("Please go to login page and login first!")

else:

    st.title("Click the button to run the model")
    a = st.button("The model lies within your grasp!")
    
    if a:

        data1 = pd.read_csv(r'HR_Dataset.xls')
        print("MODEL ONCE                            OMG BRO")
        
        #Animation options
        #https://lottiefiles.com/82707-finish-tick-animation
        #https://lottiefiles.com/95088-success
        
        with st.spinner("The model is running"):
    
            mega(data1)
        
        st.success("Model 1 has finished")
