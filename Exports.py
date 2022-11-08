import streamlit as st
from PIL import Image

# if 'page' not in st.session_state:

#     st.session_state['page'] = 'home'

# if 'inp' not in st.session_state:

#     st.session_state['inp'] = 'default'

# if 'login' not in st.session_state:

#     st.session_state['login'] = 'No'


if st.session_state['login'] == 'No':

    st.title("Please go to login page and login first!")

else:

    num_of_files=7
    temp = [str(i) for i in range(num_of_files)]
    tabs_list = st.tabs(temp)
    for i in range(num_of_files):
        with tabs_list[i]:
            img = Image.open(str(i)+".png")
            st.image(img)
