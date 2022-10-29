import streamlit as st
import sys
sys.path.insert(0,".\pages")
from login import login_function
hide_file="""
<style>
#something{
    visibility:hidden;
}
</style>
"""
login_function()
st.markdown(hide_file,unsafe_allow_html=True)
#############################
#      ABC= ST.EMPTY()      #
#     C=ABC.CONTAINER()     #
# A = C.BUTTON("CLICK ME!") #
#   B = C.WRITE("NOICE")    #
#           IF A:           #
#        ABC.EMPTY()        #
#      ST.WRITE("UEU")      #
#############################
