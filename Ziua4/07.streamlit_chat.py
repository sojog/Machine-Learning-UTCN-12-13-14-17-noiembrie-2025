import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import pickle

st.title("Aici va fi titlul ")

st.write("Bună seara!")


MESSAGES_KEY = "messages"

if not st.session_state.get(MESSAGES_KEY):
    st.session_state[MESSAGES_KEY] = []

mesaj = st.chat_input("Care este varsta sta? sa vedem daca rezistai pe Titanic")

if mesaj:
    print("Mesajul primit: ", mesaj)
    st.session_state[MESSAGES_KEY].append(mesaj)

print("st.session_state", st.session_state)


with open("random_forest_model.pkl", "rb") as file_reader:
    model:RandomForestClassifier = pickle.load(file_reader)


for msg in st.session_state.get(MESSAGES_KEY):
    # st.write(msg)
    with st.chat_message("human") as chat_msg:
        st.write(msg)

    age = int(msg)

    ## AICI SE POATE CONECTA LA AI... 
    prediction = model.predict([[ 3.    , age   ,  7.8292,  1.    ,  1.    ,  0.    ,  0.    ,
         1.    ,  0.    ,  1.    ,  0.    ]])

    with st.chat_message("ai") as chat_msg:
        st.write(f"Raspunsul la varsta {msg} este {prediction}")


###
## { 
##   "messages": [
        #     {"user":"ce a scris-user"},
        ##     {"ai": "ce a raspuns-ai-ul"},
        ##    {"user":"ce a scris-user"},
        ##     {"ai": "ce a raspuns-ai-ul"},
## }
###




