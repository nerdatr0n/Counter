import streamlit as st

st.set_page_config(page_title="Wingspan")

# To run
# streamlit run E:\Projects\Counter\main.py

def openPage():
    st.title("Wingpan")


    playerAmount = st.sidebar.number_input("Player Amount", 2, 5, 4, 1)
    cols = st.columns(playerAmount)


    for i, x in enumerate(cols):
        with x:
            st.text_area("Name", "Player " + str(i), 0, key = "Player Name" + str(i))
            one = st.number_input("Birds", 0, key = "Birds" + str(i))
            two = st.number_input("Bonus Cards", 0, key = "Bonus Cards" + str(i))
            three = st.number_input("End-of-round Goals", 0, key = "End-of-round Goals" + str(i))
            four = st.number_input("Eggs", 0, key = "Eggs" + str(i))
            five = st.number_input("Food on Cards", 0, key = "Food on Cards" + str(i))
            six = st.number_input("Tucked Cards", 0, key = "Tucked Cards" + str(i))
    
            total = one + two + three + four + five + six
            st.text("Score: " + str(total))

openPage()