from langchain_huggingface_hub import HuggingFaceHub, HUggingFaceEndpoint  
from dotenv import load_dotenv

load_dotenv()  

llm = HuggingFaceEndpoint(
    repo_id = "tinybird/llama-2-7b-chat-hf",
    task = "text-generation"
)

model = ChatHuggingFaceHub(llm=llm)

result = model.invoke("What is the capital of France?")

print(result.content)