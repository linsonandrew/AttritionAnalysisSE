import streamlit as st
import pandas as pd

#UWUu

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

    #TODO REMOVE B4 ANIMESH
    #st.write(st.session_state['model_res'])

    st.title("Overview")

    df = st.session_state['model_res']
    tab1,tab2,tab3=st.tabs(["High Attrition","Medium Attrition","Low Attrition"])
    
    styl = f"""
    <style>
    #tabs-bui4-tab-0 {{
        color: rgb(255, 75, 75);
    }}

    #tabs-bui4-tab-1 {{
        color: rgb(255, 217, 0);
    }}

    #tabs-bui4-tab-2 {{
        color: rgb(0, 255, 42);
    }}
    </style>"""
    st.markdown(styl, unsafe_allow_html=True)

    mapping =  {1:["Intense Workload","Lessen the workload"],
            2:["No clear Understanding and weak ManagerRelationship","Training Enhancement"],
            3:["Less Projects than Usual","Urgent Couselling and Affirmation of value forEmployee to be shown"],
            4:["Project Workload","Balancing of Projects by reducing the number of projects in accordance to the number of work hours"],
            5:["Working for long hours","Insentives ++"],
            6:["Recently entering the seniority zone with more projects","More Mentoring"]
    }

    with tab1:

        st.markdown(styl, unsafe_allow_html=True)
        num = 250

        for index, row in df.iterrows():
            
            num = num -1

            if num<0:
            
                break
            
            if row["odds"]>0.7:
            
                with st.expander("Employee No:"+str(int((row['Emp_ID'])))):
            
                    st.metric("Odds: ",str(int((row['odds'])*100))+"%")
                    st.write("Reasons:")
                    lst=[]
            
                    for i in row['reason']:
            
                        lst.append(mapping[i][0])
            
                    for i in lst:
            
                        st.markdown("* " + i)
            
                    agree = st.checkbox("Click this to see more details in the details page",key = int((row['Emp_ID'])))
            
                    if agree:
            
                        st.session_state['inp'] = int((row['Emp_ID']))
    
    with tab2:

        st.markdown(styl, unsafe_allow_html=True)
        num = 250

        for index, row in df.iterrows():
            
            num = num -1
           
            if num<0:
           
                break
           
            if row["odds"]<0.7 and row["odds"]>0.35:
           
                with st.expander("Employee No:"+str(int((row['Emp_ID'])))):
           
                    st.metric("Odds: ",str(int((row['odds'])*100))+"%")
                    st.write("Reasons:")
                    lst=[]
           
                    for i in row['reason']:
           
                        lst.append(mapping[i][0])
           
                    for i in lst:
           
                        st.markdown("* " + i)
           
                    agree2 = st.checkbox("Click this to see more details in the details page",key = int((row['Emp_ID'])))
            
                    if agree2:
         
                        st.session_state['inp'] = int((row['Emp_ID']))

    with tab3:

        st.markdown(styl, unsafe_allow_html=True)
        num = 250

        for index, row in df.iterrows():
            
            num = num -1
        
            if num<0:
        
                break
        
            if row["odds"]<0.35:
        
                with st.expander("Employee No:"+str(int((row['Emp_ID'])))):
        
                    st.metric("Odds: ",str(int((row['odds'])*100))+"%")
                    st.write("Reasons:")
                    lst=[]
        
                    for i in row['reason']:
        
                        lst.append(mapping[i][0])
        
                    for i in lst:
        
                        st.markdown("* " + i)
        
                    agree3 = st.checkbox("Click this to see more details in the details page",key = int((row['Emp_ID'])))
            
                if agree3:
        
                    st.session_state['inp'] = int((row['Emp_ID']))
