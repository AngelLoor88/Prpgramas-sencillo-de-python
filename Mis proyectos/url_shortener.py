import pyshorteners
import streamlit as st

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url


#creamos la app web con streamlit

st.set_page_config(page_title="URL SHORTENER",page_icon="/", layout="centered")
st.image("img/logo dow.png", use_column_width=True)
st.title("URL shortener")
url= st.text_input("enter the URL")
if st.button("Generate new URL"):
    st.write("Url shortened: ",shorten_url(url))
