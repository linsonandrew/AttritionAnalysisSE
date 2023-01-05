import streamlit as st
import pandas as pd
import mysql.connector

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
    

db_name = "attrition"


def login_checker(login_table,login_id,password):

    db_name = "attrition"
    db=mysql.connector.connect(

        host = "localhost",
        user = "root",
        password = "password",
        database = db_name

    )
    cursor=db.cursor()

    for i in login_table:

        if login_id == i[0]:

            if password == i[1]:

                st.success("Logging you in! :)")
                st.session_state['page'] = {}
                st.session_state['inp'] = 'default'
                st.session_state['input'] = 'No'
                st.session_state['model'] = 'No'

                return 1

            else:

                st.error("Incorrect Password!!! :( ")

                return 0

    sql = "INSERT INTO login (id, password) VALUES (%s, %s)"
    val = (login_id, password)
    cursor.execute( sql, val)

    st.info("New login detected! Creating login ID and password.")
    db.commit()

    return 1


db = mysql.connector.connect(

    host="localhost",
    user="root",
    password="password",
    database=db_name

)
cursor = db.cursor()


#################################
# /**************************** #
# * THIS CREATES THE BUTTONS *  #
# ****************************/ #
#################################


st.title("Attrition Solver 1000")

if st.session_state['login_test'] != 1:
    with st.form("Login:"):

        login_id = st.text_input("Login ID").lower()
        password = st.text_input("Password").lower()

        submitted = st.form_submit_button("Submit")

    ############################################################
    # /******************************************************* #
    # * THIS QUERIES THE LOGIN TABLE TO CHEACK FOR PASSWORD *  #
    # *******************************************************/ #
    ############################################################


    if submitted:

        sql = "SELECT * FROM login"
        cursor.execute(sql)

        login_table = []

        for i in cursor.fetchall():

            login_table.append(i)

        if login_id != '' and password != '':
            
            st.session_state['login_test'] = login_checker(login_table, login_id, password)

        else:

            print("hoyo")


    if st.session_state['login_test'] == 1:

        st.session_state['login'] = 'Yes'
        #st.write([login_id, password])


    else:
        st.session_state['login'] = 'No'
        print([0, 0])


else:

    st.title("You have logged in!")
    logout = st.button("Click this to logout")

    if logout:

        st.session_state['login_test'] = 0
        st.experimental_rerun()