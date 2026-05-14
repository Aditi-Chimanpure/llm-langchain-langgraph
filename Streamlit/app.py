import streamlit as st
st.title("This is title text")
st.title('_This_ is :blue[title text]:speech_balloon:')
st.title('$E=mc^2$')
st.header("This is header")
st.subheader("This is subheader")
st.text("This is plain text with no formatting")
st.markdown("# This is a header\n **This is bold text** \n - This is a list item") 
st.write("This is plain text with st.write")
data={"Name":"Alice","Age":30,"Occupation":"Engineer"}
st.write(data)