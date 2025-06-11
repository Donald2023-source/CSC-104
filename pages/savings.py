import streamlit as st
from savings_account import SavingsAccount


st.set_page_config(page_title='BANK APP', layout='centered')

savings = SavingsAccount(200000)

with st.form('savings_form'):
    amount = st.number_input("Enter Amount")
    operations = st.selectbox('Deposit or Withdraw', ("deposit","withdraw"))
    submit = st.form_submit_button('submit')


if  submit and operations == 'withdraw':
    with st.spinner(' Processing... '): 
        savings.withdraw(amount)
        st.write(savings.balance)

# ST. WRITE FOR LIMIT ' LIMIT 
