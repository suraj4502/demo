import streamlit as st
import  pandas as pd
import  numpy as np


# pip install streamlit
# streamlir run main.py

#
# st.title("Stramlit demo")
# st.sidebar.title("sidebar title")
#
# st.header("this is a header.")
# st.subheader("this is a subheader")
#
# st.write("this is a normal text.")
#
# st.success("this is  a success message")
# st.warning("IHL")
# st.info("jhdlfs")
# st.error("dsfs")
#
# st.metric("This is a metric",value=85000,delta='-1')
#
# inp = st.sidebar.text_input("enter something")
# st.title(inp)
#
# radio_inp = st.radio('Radio',['a','b','c'])
# if radio_inp == 'a':
#     st.write("a selected")
#
#
# check = st.checkbox('checkbox')
#
# if check:
#     st.title("checkec")
#
#
# sidebar_value = st.sidebar.selectbox('Selectbox',['a','b0','v'])
#
# a = st.button("Button")
#
# if a:
#     st.header("button clicked")




st.title("sample Calculator.")

st.sidebar.image('calc.gif')

col1, col2 = st.columns([1,1])
with col1:
    n1 = st.text_input("ENter a number",value='0')

with col2:
    n2 = st.text_input("ENter 2nd  number",value='0')


op = st.selectbox("Select Operation",['+','-','*','/'])

n1 = float(n1)
n2 = float(n2)



if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    result = n1 / n2

c1,c2,c3  = st.columns([1,1,1])

with c2:
    btn = st.button("Calculate")

if btn:
    st.success(f"The result is {result}.")