import streamlit as st
import cohere

st.title("🤖 Cohere Chatbot")

# Cohere API key
cohere_key = 'YOUR_COHERE_API_KEY'
co = cohere.Client(cohere_key)

# Initialize the conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Streamlit form for user prompt
with st.form(key="question_form"):
    # Streamlit input for user prompt
    user_prompt = st.text_input("Type a message", key="user_input", help="Press Enter to generate a response")

    # Process user input and get response when Enter is pressed
    if st.form_submit_button("Submit") or st.session_state.conversation:
        # Cohere API call
        response = co.generate(
            model='command-nightly',
            prompt=user_prompt,
            max_tokens=300,
            temperature=0.9,
            k=0,
            p=0.75,
            stop_sequences=[],
            return_likelihoods='NONE'
        )

        # Append the current conversation to the list
        st.session_state.conversation.append({"user": user_prompt, "bot": response.generations[0].text})

# Display previous responses in descending order
if st.session_state.conversation:
    for conv in reversed(st.session_state.conversation):
        st.write(f"User 👨‍🦱: {conv['user']}")
        st.write(f"Bot 🤖: {conv['bot']}")
        st.write("----------------")
