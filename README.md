# Chatbot-Choose-Diff-LLM
## Chatbot with Multiple Language Models

This project features a variety of chatbots powered by different language models, providing users with the flexibility to choose from various conversational AI technologies. Each chatbot offers unique features and characteristics, enhancing the overall user experience.

## Available Chatbots

### PaLM-2 Streamlit Chatbot
PaLM-2 (Bison 001) is a powerful language model that drives the conversational abilities of this chatbot. It is deployed as a user-friendly web application using Streamlit and can be hosted locally for convenient testing and development.

**Features:**
- **Enhanced Conversational Abilities:** Utilizes the PaLM-2 (Bison 001) language model.
- **User-Friendly Web App:** Deployed with Streamlit for easy interaction.
- **Local Hosting:** Convenient for testing and development.
-------------------------
### Cohere Chatbot
Engage in natural language conversations with the Cohere Streamlit Chatbot. This chatbot utilizes the Cohere language model and is deployed as a Streamlit app, providing a user-friendly interface for interaction. Keep track of your conversation with the chatbot in a convenient history display.

**Features:**
- **Conversational AI:** Engage in natural language conversations with the Cohere Streamlit Chatbot.
- **Streamlit Interface:** User-friendly app for easy interaction.
- **Conversation History:** Keep track of your conversation with the chatbot.
---------
### Falcon Chatbot
The Falcon Chatbot is powered by the Falcon language model available on Hugging Face. Leverage the capabilities of Hugging Face's Falcon 7B model through the LangChain library for natural language understanding and generation. The chatbot is deployed as a Streamlit app, making it easy to interact with a user-friendly interface.

**Features:**
- **Conversational AI:** Engage in natural language conversations with the Falcon Chatbot.
- **Hugging Face Integration:** Utilizes the Hugging Face model hub for seamless access to powerful language models.
- **Streamlit Interface:** Deployed as a Streamlit app for user-friendly interaction.
- **Conversation History:** Keep track of your conversation with the chatbot.
-----------
### OpenAI GPT-3 Chatbot
This chatbot is created using Python, OpenAI, and Streamlit libraries. It is powered by the GPT-3 text-davinci-003 model, allowing users to communicate by entering prompts and receiving responses generated by the OpenAI API. The chat history is stored in the Streamlit session state and displayed in a chat window for users to view.

**Features:**
- **Integration with OpenAI GPT-3:** Robust natural language processing capabilities.
- **User-Friendly Streamlit Interface:** Interactive conversations through a user-friendly interface.
- **Conversation History Tracking:** The chat history is stored and displayed in a chat window.
-----------
## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/chatbot-multi-llm.git
    cd chatbot-multi-llm
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API keys:**
   - **OpenAI:**
     - Generate your OpenAI API key [here](https://platform.openai.com/api-keys).

   - **Cohere:**
     - Obtain your Cohere API key from [here](https://dashboard.cohere.com/api-keys).

   - **PaLM:**
     - Generate your PaLM API key from [Google Maker Suite](https://makersuite.google.com/app/apikey).

   - **Falcon (Hugging Face Token):**
     - Visit the [Hugging Face website](https://huggingface.co/).
     - Sign in or create an account.
     - Navigate to your [API tokens page](https://huggingface.co/settings/tokens).
     - Copy your Hugging Face API token.

4. **Run the Streamlit app:**
    ```bash
    streamlit run your_app_name.py
    ```

5. **Interact with the chatbot:**
   Open your web browser and navigate to the provided local address (usually http://localhost:8501). Enter prompts and receive natural language responses from the chatbot.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Hugging Face Falcon 7B model](https://huggingface.co/tiiuae/falcon-7b-instruct)
- [Cohere](https://cohere.com/)
- [PaLM (Bison-001)](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/)
- [Replicate API](https://replicate.ai/)
- [OpenAI GPT-3](https://chat.openai.com/)



