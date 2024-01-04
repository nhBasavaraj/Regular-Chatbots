#!/bin/bash

# Set the URL of the Regular-Chatbots repository
regular_chatbots_repo="https://github.com/Fig-MLOps/Regular-Chatbots.git"

# Clone the Regular-Chatbots repository
git clone $regular_chatbots_repo Regular-Chatbots
cd Regular-Chatbots

# Set the remote name for Chatbot-LLM
remote_chatbot_llm="remote_Chatbot-LLM"

# Add the remote for Chatbot-LLM and merge the repository
git remote add -f $remote_chatbot_llm "https://github.com/Fig-MLOps/Chatbot-LLM.git"
git merge -s ours --no-commit --allow-unrelated-histories $remote_chatbot_llm/main
git read-tree --prefix=Chatbot-LLM/ -u $remote_chatbot_llm/main
git commit -m "Merge Chatbot-LLM into Regular-Chatbots"
git push origin main

# Remove the remote to avoid conflicts with subsequent iterations
git remote remove $remote_chatbot_llm
