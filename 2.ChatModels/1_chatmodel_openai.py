from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = 'gpt-4o', temperature = 0.9)

result = model.invoke("What is the capital of delhi")

print(result.content)