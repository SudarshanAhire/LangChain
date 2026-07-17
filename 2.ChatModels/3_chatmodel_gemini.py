from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenAI(model="gemini-1.5-t")

result = model.invoke("Write a poem about the ocean."   )

print(result)