import streamlit as st

st.title('BMI Calculator')

weigth = st.number_input (
    label='Enter weight (kg) :',
    min_value=10,
    max_value=200,
    value=50
)

heigth = st.number_input (
    label='Enter height (m) :',
    min_value=1.0,
    max_value=2.0,
    value=1.5,
    step=0.01,
)

if st.button('Calculator'):
    bmi = weigth / heigth ** 2
    st.write(f'your BMI is: {bmi:.2f}')