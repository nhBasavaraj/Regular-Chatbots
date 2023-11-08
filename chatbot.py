import requests
import streamlit as st

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
API_KEY = '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'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def generate_response(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    completion = response_data['choices'][0]['message']['content'] if 'choices' in response_data else 'No completion available'
    return completion

st.title("🤖 chatBot : openAI GPT-3 + Streamlit")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input("👤 You: ", "Hello Chatbot", key="input")

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
