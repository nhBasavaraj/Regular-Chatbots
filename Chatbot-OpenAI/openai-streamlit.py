import requests
import streamlit as st

# OpenAI GPT-3 Chatbot
st.title("🤖 chatBot : OpenAI GPT-3 + Streamlit")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def generate_response(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {"OPEN_AI_API_KEY"}'
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    completion = response_data['choices'][0]['message']['content'] if 'choices' in response_data else 'No completion available'
    return completion

    # Streamlit input for user prompt
user_input = st.text_input("Type a message", key="user_input", help="Press Enter to generate a response")

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        st.markdown(
            f'<p style="font-size: 20px; color: #ff5733;">👤 You: {st.session_state["past"][i]}</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="font-size: 20px; color: #FFFFFF;">🤖 Bot: {st.session_state["generated"][i]}</p>',
            unsafe_allow_html=True,
        )
        st.text("----------------------")
