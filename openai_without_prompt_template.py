from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

from langchain_openai import ChatOpenAI

chat = ChatOpenAI()
ai_response = chat.invoke("Tell me a joke about Micheal Jackson")

print(ai_response.content)



