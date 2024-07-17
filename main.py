import streamlit as st

st.set_page_config(page_title="Wingspan")



def openPage():
    st.title("Wingpan")

    playerAmount = st.number_input("Player Amount", 2, 5, 2, 1)
    cols = st.columns(playerAmount)


    for i, x in enumerate(cols):
        with x:
            st.text_area("Name", "Player " + str(i), 0)
            one = st.number_input("No 1", 0, i + 999)
            two = st.number_input("No 2", 0, i)
    
            total = one + two
            st.text("Score: " + str(total))

openPage()