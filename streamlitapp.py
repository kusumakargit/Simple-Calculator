import streamlit as st

st.title("SIMPLE CALCULATOR")

st.header('Slide To Get The Square Of A Number')

x = st.slider("Slide the Pointer")

st.write("The Squared Value of", x , "is", x * x)

st.header('Input The Numbers To Get The Sum Of Them')

def sum_two_numbers(a, b):
    return a + b

a = st.number_input("Enter the first number:",step=1,key="1")
b = st.number_input("Enter the second number:",step=1,key="2")

sum = sum_two_numbers(a, b)

st.write("The sum of", a, "and", b, "is", sum)

st.header('Input The Numbers To Get The Difference Between Them')

def diff_two_numbers(c, d):
    return c - d

c = st.number_input("Enter the first number:",step=1,key="3")
d = st.number_input("Enter the second number:",step=1,key="4")

diff = diff_two_numbers(c, d)

st.write("The difference between", c, "and", d, "is", diff)

st.header('Input The Numbers To Get The Product of Them')

def prod_two_numbers(c, d):
    return c * d

c = st.number_input("Enter the first number:",step=1,key="5")
d = st.number_input("Enter the second number:",step=1,key="6")

prod = prod_two_numbers(c, d)

st.write("The Product of", c, "and", d, "is", prod)
