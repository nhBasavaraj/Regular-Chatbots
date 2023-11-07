import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = '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'

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

st.title("🤖 chatBot : openAI GPT-3 + Streamlit")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_input = st.text_input("👤 You: ", "Hello", key="input")

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        st.markdown(
            f'<p style="font-size: 16px; color: #ff5733;">👤 You: {st.session_state["past"][i]}</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<p style="font-size: 20px; color: #33ccff;">🤖 Bot: {st.session_state["generated"][i]}</p>',
            unsafe_allow_html=True,
        )
        st.text("-------------")
