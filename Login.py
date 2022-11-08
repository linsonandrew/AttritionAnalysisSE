import streamlit as st
import mysql.connector

# if 'page' not in st.session_state:

#     st.session_state['page'] = 'home'

# if 'inp' not in st.session_state:

#     st.session_state['inp'] = 'default'

# if 'login' not in st.session_state:

#     st.session_state['login'] = 'No'

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

with st.form("Login:"):

    login_id = st.text_input("Login ID").lower()
    password = st.text_input("Password").lower()

    submitted = st.form_submit_button("Submit")

############################################################
# /******************************************************* #
# * THIS QUERIES THE LOGIN TABLE TO CHEACK FOR PASSWORD *  #
# *******************************************************/ #
############################################################

login_check = 0

if submitted:

    sql = "SELECT * FROM login"
    cursor.execute(sql)

    login_table = []

    for i in cursor.fetchall():

        login_table.append(i)

    if login_id != '' and password != '':

        login_check = login_checker(login_table, login_id, password)

    else:

        print("hoyo")


if login_check == 1:

    st.session_state['login'] = 'Yes'
    st.write([login_id, password])

else:
    st.session_state['login'] = 'No'
    print([0, 0])