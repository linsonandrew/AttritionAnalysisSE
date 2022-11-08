import streamlit as st
import pandas as pd


# if 'page' not in st.session_state:

#     st.session_state['page'] = 'home'

# if 'inp' not in st.session_state:

#     st.session_state['inp'] = 'default'

# if 'login' not in st.session_state:

#     st.session_state['login'] = 'No'



if st.session_state['login'] == 'No':

    st.title("Please go to login page and login first!")

else:

    st.subheader("Please chose the dataset.")
    df = pd.read_csv("format.xls")

    st.write("This is the required format:")
    st.dataframe(df,20,10)

    data = st.file_uploader("Drag or select your file")

    if data is not None:

        st.write("This is the selected file")
        df= pd.read_csv(data)
        st.dataframe(df)
