import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("C://Users//anany//Downloads//Ananya_Porfolio.jpeg")

with col2:
    st.title("Ananya Anamandala")
    content = """
    Hello all! I am Ananya, I am a Data Scientist at Kellton. I graduated with a masters in Data Analytics Engineering 
    from George Mason University
    """
    st.info(content)

col3, col4 = st.columns(2)


df = pandas.read_csv("datax.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


