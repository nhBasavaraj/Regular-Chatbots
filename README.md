# Falcon Chatbot

Falcon Chatbot is a conversational AI powered by the Falcon language model. This chatbot leverages the capabilities of Hugging Face's Falcon 7B model through the LangChain library to provide natural language understanding and generation.

## Features

- **Conversational AI:** Engage in natural language conversations with the Falcon Chatbot.
- **Hugging Face Integration:** Utilizes the Hugging Face model hub for seamless access to powerful language models.
- **Streamlit Interface:** Deployed as a Streamlit app, making it easy to interact with the chatbot through a user-friendly interface.
- **Conversation History:** Keep track of your conversation with the chatbot in a convenient history display.

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/falcon-chatbot.git
    cd falcon-chatbot
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Access Hugging Face API Token:**
   - Visit the [Hugging Face website](https://huggingface.co/).
   - Sign in or create an account.
   - Navigate to your [API tokens page](https://huggingface.co/settings/token).
   - Copy your API token.

4. **Run the Streamlit app:**
    ```bash
    streamlit run your_app_name.py
    ```

5. **Interact with the chatbot:**
   Open your web browser and navigate to the provided local address (usually http://localhost:8501). Enter prompts and receive natural language responses from Falcon Chatbot.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Hugging Face Falcon 7B model](https://huggingface.co/tiiuae/falcon-7b-instruct)

