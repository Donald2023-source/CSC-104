import streamlit as st
from saving_account import SavingAccount


cols1, cols2, cols3 = st.columns(3)

# st.set_page_config("BANK APP", layout="centered", )

savings = SavingAccount(300000)
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


st.markdown(f"""
<div class="card" style="display: flex; margin: 20px 0; width: 100%; background: #7F00FF; border-radius: 16px; padding: 3rem; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37); flex-direction: column; align-items: center; justify-content: center;">   
    <h5 style="text-align:left">Savings Account</h5>
    <p style="font-weight: 600">Account Balance: N{savings.balance}</p>
</div>
""", unsafe_allow_html=True)



with st.form('current_form'):
    operations = st.selectbox('Deposit or Withdraw', ("deposit","withdraw"))
    amount = st.number_input("Enter Amount", key='current_amount')
    submit = st.form_submit_button('submit');

if submit and operations == 'withdraw':
    with st.spinner(' Processing... '):
        savings.withdraw(amount)
        st.write(f"New Balance: N{savings.balance}")

        if amount > savings.balance:
            st.markdown(f"<p style='color: red;'>Insufficient funds for withdrawal.</p>", unsafe_allow_html=True)
        elif amount > 6000:
            st.markdown(f"<p style='color: red;'>Withdrawal amount cannot be above N6,000.</p>", unsafe_allow_html=True)
        else:
            st.write(f"Withdrawal was successful!.")
            st.write(f"New Balance: {savings.balance}")
            
if submit and operations == "deposit":
    with st.spinner("Please wait ...."):
        savings.deposit(amount)
        st.write(f"Deposit was successful!.")
        st.markdown(f"<p style='color: green;'>Your new balance: N{savings.balance}</p>", unsafe_allow_html=True)