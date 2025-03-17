import streamlit as st

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
    st.write(content)