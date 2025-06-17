import streamlit as st
cols1, cols2, cols3 = st.columns(3)

# st.set_page_config("BANK APP", layout="centered", )


cols1.markdown(
    """
    <style>
    .stApp {
        background-color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<style>
      .card:hover{
            transform: scale(1.06);
            transition: ease-in-out 300ms;
            cursor: pointer
        }      
</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    [data-testid="stSidebar"] {
       background-color: #000;
       color: #000;
    }
    </style>
    """, unsafe_allow_html=True
)


st.markdown("""
<div style="display: flex; align-items: center; justify-content: center;">   
            <img src="https://img.icons8.com/?size=100&id=VbL8v3mm1qyp&format=png&color=000000 alt=">
            <h2 style="color: #000;">Easy Bank</h2>
            </div>
""", unsafe_allow_html=True) 



st.markdown("""<div style="color:#000; text-align:center">Welcome to the Bank App! Please select an account type from the sidebar to proceed.</div>""", unsafe_allow_html=True)


st.markdown("""
<div style="display: flex; align-items: center; gap: 30px; width: 100vw; margin: 20px 0">
            <div class="card" style="display: flex; margin: 20px 0; width: 400px; background: #7F00FF; border-radius: 16px; padding: 0.8rem; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); flex-direction: column; align-items: center; justify-content: center;">   
            <img style="height: 30px" src="https://img.icons8.com/?size=100&id=VbL8v3mm1qyp&format=png&color=000000 alt=">
            <h5>Current Account</h5>
            <p style="text-align:center">With easy bank you get to have an exceptional current account, that helps to spend as you like. No limit. Enjoy ya sefff!!!<p>
            </div>
             <div class="card" style="display: flex; margin: 20px 0; width: 400px; background: linear-gradient(to right, #0000FF, #7F00FF); border-radius: 16px; padding: 0.8rem; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); flex-direction: column; align-items: center; justify-content: center;">   
            <img style="height: 30px" src="https://img.icons8.com/?size=100&id=VbL8v3mm1qyp&format=png&color=000000 alt=">
            <h5>Savings Account</h5>
            <p style="text-align:center">Want to save?. Easy bank's got your back. Welcome to a seamless savings account to help you maximise your finance<p>
            </div>
         </div>
""", unsafe_allow_html=True) 


