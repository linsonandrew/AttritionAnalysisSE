import streamlit as st
import mysql.connector


def login_shit(login_table):   
    for i in login_table:
        if login_id==i[0]:
            if passeord==i[1]:
                st.write("Logging you in! :)")
            else:
                st.write("Incorrect Password!!! :( ")
            return 0
    st.write("Y THE HELL ARE YOU HERE")
    sql = "INSERT INTO login (id, password) VALUES (%s, %s)"
    val = (login_id, passeord)
    cursor.execute(sql,val)
    st.write("New login detected! Creating login ID and password.")
    return 1
    

db_name="attrition"

db=mysql.connector.connect(
    host= "localhost",
    user="root",
    password="password",
    database=db_name
)
cursor=db.cursor()

st.write("Welcome to Attrition Solver 1000")
login_id=st.text_input("Login ID")
passeord=st.text_input("Password")

sql="SELECT * FROM login"
cursor.execute(sql)

login_table=[]
for i in cursor.fetchall():
    login_table.append(i)

garbage=0
if login_id!='' and passeord!='':
    garbage=login_shit(login_table)

db.commit()

