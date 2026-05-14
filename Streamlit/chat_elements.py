import streamlit as st
with st.chat_message("ai"):
    st.write("Hello there!")
    
prompt=st.chat_input("Type your message",max_chars=10)
if prompt:
    st.write(f"User message:{prompt}")