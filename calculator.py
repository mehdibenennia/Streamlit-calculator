import streamlit as st

class Calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def add(self):
        return self.value1 + self.value2

    def subtract(self):
        return self.value1 - self.value2

    def multiply(self):
        return self.value1 * self.value2

    def divide(self):
        try:
            result = self.value1 / self.value2
        except ZeroDivisionError:
            result = "Cannot divide by 0"
        return result

st.title("Welcome to Our Calculator")

value1 = st.number_input('Enter a number', key="value1")
value2 = st.number_input('Enter a number', key="value2")

calculator = Calculator(value1, value2)

if st.button('Addition'):
    st.write(f"Addition: {calculator.add()}")

if st.button('Subtraction'):
    st.write(f"Subtraction: {calculator.subtract()}")

if st.button('Division'):
    st.write(f"Division: {calculator.divide()}")

if st.button('Multiplication'):
    st.write(f"Multiplication: {calculator.multiply()}")

if st.button('Clear'):
    st.session_state.value1 = 0
    st.session_state.value2 = 0
