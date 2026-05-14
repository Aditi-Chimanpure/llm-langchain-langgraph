import streamlit as st
st.title("Nested Buttons Example")
if "show_second_button" not in st.session_state:
    st.session_state.show_second_button=False
if "second_button_clicked" not in st.session_state:
    st.session_state.second_button_clicked=False
    
# if st.button("First Button"):
#     st.write("Revealed")
#     if st.button("second Button"):
#         st.write("second Button clicked")
        
if st.button("First Button"):
    st.session_state.show_second_button=True
if st.session_state.show_second_button:
    st.write("Revealed")
    if st.button("second Button"):
        st.session_state.second_button_clicked=True
        
if st.session_state.second_button_clicked:
    st.write("Second Button Clicked!")