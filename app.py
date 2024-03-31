import streamlit as st

st.set_page_config(page_title="Chat",
                   page_icon=":hugging_face:",                   
                   layout="wide",
                   menu_items={
                       'About': "birthday"
                   })

st.markdown("<h1 style='text-align: center; color: purple;'>HAPPY BIRTHDAY MY DEAR!</h1>", unsafe_allow_html=True)

st.balloons()

left_co, cent_co, last_co = st.columns(3)

with cent_co:
    st.image("imgs/happy.jpg")

st.balloons()

left_co2, cent_co2, last_co2 = st.columns(3)

with cent_co2:
    st.image("imgs/wood.jpg")

st.markdown("""<h1 style='text-align: center; color: red;'> YOU ARE INVITED!</h1>""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: center; color: red;'> TO Discover Woodcrafting</h1>""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: center; color: red;'>Time and Locations:</h1>""", unsafe_allow_html=True)

st.markdown("""<h1 style='text-align: center; color: red;'>Hertensteinstrasse 20, Zürich, Switzerland
                    Saturday, April 6, 2024 10:00 AM</h1>""", unsafe_allow_html=True)

st.balloons()