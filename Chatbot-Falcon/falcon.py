import streamlit as st
import asyncio
from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain
from bs4 import BeautifulSoup  # Make sure to install this library

HUGGINGFACEHUB_API_TOKEN = "ENTER HUGGINGFACE_API_TOKEN_KEY"

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
