import streamlit as st
from bs4 import BeautifulSoup  # Make sure to install this library
import asyncio
import google.generativeai as palm

palm.configure(api_key="YOUR_PALM_2_API_KEY")

defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
}

# Initialize Streamlit session state
if "palm_chain" not in st.session_state:
    st.session_state.palm_chain = None

# Initialize the conversation history
if "palm_conversation" not in st.session_state:
    st.session_state.palm_conversation = []

# Main function for Streamlit app
def get_palm_chain():
    return palm

# Main Streamlit app logic
if st.session_state.palm_chain is None:
    st.session_state.palm_chain = get_palm_chain()

# Set the title
st.title("🌴 PaLM 2 (Bison-001) Chatbot ")

# Use the form API to handle form submission
with st.form(key="palm_form"):
    # Get user input
    question = st.text_input("Ask a question:", key="palm_question_key", value="")

    # Display a submit button
    submit_button = st.form_submit_button("Submit")

# Process user input and get response
if submit_button:
    palm_chain = st.session_state.palm_chain

    # Call the chain asynchronously
    async def async_acall():
        response = palm_chain.generate_text(**defaults, prompt=question)
        return response.result

    # Run the asynchronous function in an event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response_text = loop.run_until_complete(async_acall())

    # Add the current question and answer to the conversation history
    st.session_state.palm_conversation.append({"question": question, "answer": response_text})

    # Display the entire conversation in reverse order
    for conv in reversed(st.session_state.palm_conversation):
        st.text(f"You 🧑: {conv['question']}\nPalm-Bot 🌴: {conv['answer']}")

    # Clear the input field
    question = ""

# Reset the palm_chain state after processing
if st.session_state.palm_chain is None:
    st.session_state.palm_chain = get_palm_chain()
