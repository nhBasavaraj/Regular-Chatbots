import streamlit as st
import requests
from sklearn.metrics.pairwise import cosine_similarity

def get_jina_embeddings(texts):
    url = 'https://api.jina.ai/v1/embeddings'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer JINA_API_KEY'
    }
    data = {
        'input': texts,
        'model': 'jina-embeddings-v2-base-en'
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Streamlit UI
st.title("🤖 chatBot : Jina LLM + Streamlit")

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

# Jina bot function
def generate_response(prompt, conversation, generated_responses):
    all_user_inputs = conversation + [prompt]
    embeddings_response = get_jina_embeddings(all_user_inputs)
    embeddings = embeddings_response['data'][-1]['embedding']
    return embeddings, generated_responses

# Streamlit input for user prompt
user_input = st.text_input("Type a message", key="user_input", help="Press Enter to generate a response")

if user_input:
    output, generated_responses = generate_response(user_input, st.session_state['conversation'], st.session_state['generated'])
    st.session_state['conversation'].append(user_input)
    st.session_state['generated'].append(output)

    st.write("Chat History:")
    for i in range(len(st.session_state['conversation']) - 1, -1, -1):
        st.write(f"👤 You: {st.session_state['conversation'][i]}")
        if i < len(generated_responses):
            st.write(f"🤖 Bot: {generated_responses[i]}")
        st.text("----------------------")


