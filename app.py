import streamlit as st

st.title('Subtraction Of Two Numbers')
st.subheader('Gigi')


number1 = st.text_input('Enter the first number : ')
number2 = st.text_input('Enter the second number : ')

button = st.button('Submit')



if button:
    if number1 and number2:
        try:
            number1 = int(number1)
            number2 = int(number2)
            st.markdown(f"## {number1} / {number2} = {float(number1)-float(number2)}")
        except ValueError:
            st.error("Please enter numbers")
    else:
        st.error('Please enter numbers')