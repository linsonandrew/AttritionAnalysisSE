import streamlit as st
import time
import sys
from login import login_function
from input_screen import Inputs_func
from Exports import Exports_func
from Detail import Details_func
from Overview import Overview_func
import time

#################################################################
#                        SESSION STATES:                        #
#        TRACK ==> THIS CHECKS IF THE USER HAS LOGGED IN        #
#          CREDS ==> THIS STORE THE LOGIN INFORMATION           #
# LASTPAGE ==> THIS STORES THE LATEST PAGE THE USER HAS GONE TO #
#################################################################

#This changes session state to After Login and also forcefully reloads the page
def login_func():
    st.session_state['track'] = "After Login"
    time.sleep(1.3)
    st.experimental_rerun()

#This changes session state to Before Login
def logout_func():
    st.session_state['track'] = "Before Login"

#This initializes all the seesion states.
if 'track' not in st.session_state:
    st.session_state['track'] = "Before Login"
if 'creds' not in st.session_state:
    st.session_state['creds'] = ['1','2']
if 'lastpage' not in st.session_state:
    st.session_state['lastpage'] = "Overview"

#This renders login page if the use rhas not logged in
if st.session_state['track'] == "Before Login":
    credentials=['1','2']
    credentials = login_function()
    if credentials[0] != 0:
        st.session_state['creds'] = [credentials[0],credentials[1]]
        login_func()

#This creates the buttons in the sidebar only after the user has logged in
elif st.session_state['track'] == "After Login":
    st.sidebar.button("Overview",on_click=Overview_func)
    st.sidebar.button("Input",on_click=Inputs_func)
    st.sidebar.button("Details",on_click=Details_func)
    st.sidebar.button("Exports",on_click=Exports_func)
    st.sidebar.button("Logout",on_click=logout_func)

#This is just to go to the Overview page immidiatly after login
    if st.session_state['lastpage'] == "Overview":
        Overview_func()
#############################
#      ABC= ST.EMPTY()      #
#     C=ABC.CONTAINER()     #
# A = C.BUTTON("CLICK ME!") #
#   B = C.WRITE("NOICE")    #
#           IF A:           #
#        ABC.EMPTY()        #
#      ST.WRITE("UEU")      #
#############################
