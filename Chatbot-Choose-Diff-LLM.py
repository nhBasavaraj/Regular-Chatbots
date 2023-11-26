import streamlit as st
import requests
import asyncio
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from bs4 import BeautifulSoup
import cohere
import google.generativeai as palm

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
OPENAI_API_KEY = "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"
COHERE_API_KEY = 'OyjmiSGIOTWSxwyP2sPxhzUKi7WYP6KwUqPG5N3N'
HUGGINGFACEHUB_API_TOKEN = "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"
PALM_API_KEY = "AIzaSyAwv6Rg2JH5L-aIKMDrubH3zq0OJC69ISQ"

# Define chatbot options
chatbot_options = ["OpenAI GPT-3", "Falcon LLM", "Cohere", "PaLM", "Jina"]

# Create a sidebar with the chatbot selection dropdown
selected_chatbot = st.sidebar.selectbox("Select Chatbot", chatbot_options)

# Display the selected chatbot title
#st.title(f"🤖 Chatbot: {selected_chatbot}")

# OpenAI GPT-3 Chatbot
if selected_chatbot == "OpenAI GPT-3":
    st.title("🤖 chatBot : OpenAI GPT-3 + Streamlit")

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    def generate_response(prompt):
        url = 'https://api.openai.com/v1/chat/completions'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENAI_API_KEY}'
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


# Falcon LLM Chatbot
elif selected_chatbot == "Falcon LLM":
    repo_id = "tiiuae/falcon-7b-instruct"
    llm = HuggingFaceHub(
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        repo_id=repo_id,
        model_kwargs={"temperature": 0.7, "max_new_tokens": 500}
    )

    template = """Question: {question}

    Answer: {answer}"""

    # Initialize Streamlit session state
    if "llm_chain" not in st.session_state:
        st.session_state.llm_chain = None

    # Initialize the conversation history
    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    # Main function for Streamlit app
    def get_llm_chain():
        prompt = PromptTemplate(template=template, input_variables=["question", "answer"])
        return LLMChain(prompt=prompt, llm=llm, verbose=True)

    # Main Streamlit app logic
    if st.session_state.llm_chain is None:
        st.session_state.llm_chain = get_llm_chain()

    # Set the title
    st.title("🤖 CHATBOT with FALCON LLM")

    # Use the form API to handle form submission
    with st.form(key="question_form"):
        # Get user input
        question = st.text_input("Ask a question:", key="question_key", value="")

        # Display a submit button
        submit_button = st.form_submit_button("Submit")

    # Process user input and get response
    if submit_button:
        llm_chain = st.session_state.llm_chain

        # Call the chain asynchronously
        async def async_acall():
            return await llm_chain.acall({'question': question, 'answer': ''})

        # Run the asynchronous function in an event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(async_acall())

        # Remove HTML tags from the response
        response_text = BeautifulSoup(response["text"], "html.parser").get_text()

        # Add the current question and answer to the conversation history
        st.session_state.conversation.append({"question": question, "answer": response_text})

        # Display the entire conversation in reverse order
        for conv in reversed(st.session_state.conversation):
            st.text(f"Question 🧑: {conv['question']}\nAnswer 🤖: {conv['answer']}")

        # Clear the input field
        question = ""

    # Reset the llm_chain state after processing
    if st.session_state.llm_chain is None:
        st.session_state.llm_chain = get_llm_chain()

# Cohere Chatbot
elif selected_chatbot == "Cohere":
    st.title("🤖 Cohere Chatbot")

    # Replace 'YOUR_COHERE_API_KEY' with your actual Cohere API key
    COHERE_API_KEY = 'OyjmiSGIOTWSxwyP2sPxhzUKi7WYP6KwUqPG5N3N'
    co = cohere.Client(COHERE_API_KEY)

    # Initialize the conversation history
    if "cohere_conversation" not in st.session_state:
        st.session_state.cohere_conversation = []

    # Streamlit form for user prompt
    with st.form(key="cohere_form"):
        # Streamlit input for user prompt
        user_prompt = st.text_input("Type a message", key="cohere_user_input", help="Press Enter to generate a response")

        # Process user input and get response when Enter is pressed, and prompt is not empty
        if st.form_submit_button("Submit") and user_prompt:
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
            st.session_state.cohere_conversation.append({"user": user_prompt, "bot": response.generations[0].text})

    # Display previous responses in descending order
    if st.session_state.cohere_conversation:
        for conv in reversed(st.session_state.cohere_conversation):
            st.write(f"User 👨‍🦱: {conv['user']}")
            st.write(f"Bot 🤖: {conv['bot']}")
            st.write("----------------")

            
#PaLM chatbot
elif selected_chatbot == "PaLM":
    st.title("🌴 PaLM 2 (Bison-001) Chatbot ")

    palm.configure(api_key=PALM_API_KEY)

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
            st.text(f"You 🧑: {conv['question']}\nPaLM-Bot 🌴: {conv['answer']}")

        # Clear the input field
        question = ""

    # Reset the palm_chain state after processing
    if st.session_state.palm_chain is None:
        st.session_state.palm_chain = get_palm_chain()


#jina chatbot
elif selected_chatbot == "Jina":
    def get_jina_embeddings(texts):
        url = 'https://api.jina.ai/v1/embeddings'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer jina_7f866ddc08134f3a9c19e7940fcb5e37QS9XyVII6_fVp8RKyHy54Y7AD8KE'
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

