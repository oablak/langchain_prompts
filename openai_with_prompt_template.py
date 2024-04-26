from dotenv import load_dotenv, find_dotenv

load_dotenv()

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Tell me a joke about {person_name}")

#prompt.format(person_name="Bill Clinton")


from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

chat = ChatOpenAI()
chain = prompt | chat | StrOutputParser()
response = chain.invoke({"person_name": "Bob Marley"})

print(response)