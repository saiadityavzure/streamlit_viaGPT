import streamlit as st
from htmlTemplates import css


import requests
import json 


def main():
    st.set_page_config(page_title="Chat with your data!",
                       page_icon=":books:")
    #st.write(css, unsafe_allow_html=True)

    
    # Store LLM generated responses
    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    url = "http://10.20.1.95:8000/runmodel/"

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    def generate_response(user_question):
        #here we will write the user question and the password
        url = "http://10.20.1.95:8000/runmodel/"
        payload = {"query": user_question}
        response = requests.post(url, payload)
        #st.write(response)
        #Now we got the response and the response.json will return a dictionary with the key of "answer"
        #we will return just the value of the answer
        return (response.json()["answer"])
            
    # User-provided prompt
    if user_question := st.chat_input("Ask questions about your data here"):
        st.session_state.messages.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.write(user_question)
    
    #now we will generate the response if the last message is not the ai's chat
    if st.session_state.messages[-1]["role"] != "assistant":
        #now we will generate the response
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                response_json = generate_response(user_question)
                st.write(response_json)

        new_message = {"role": "assistant", "content": response_json}
        st.session_state.messages.append(new_message)




    # st.header("Chat :")
    # user_question = st.text_input("Ask a question about your documents:")
    # if user_question:
        
    #     url = "http://10.20.1.95:8000/runmodel/"
    #     if st.button("Ask Question"):
    #         payload = {"query": user_question}
    #         response = requests.post(url, payload)
    #         st.write(response)
    #         st.write(response.json())
        

    #with st.sidebar:
        #st.write("VISCALAR chat application")
    #     uploaded_files = st.file_uploader("Choose a pdf, csv or text files:", accept_multiple_files=True)
    #     for uploaded_file in uploaded_files:
    #         bytes_data = uploaded_file.read()
    #         st.write("filename:", uploaded_file.name)
    #         st.write(bytes_data)
    #         #here we will write the data
    





if __name__ == '__main__':
    main()
