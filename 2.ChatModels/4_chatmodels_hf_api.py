from langchain_huggingface_hub import HuggingFaceHub, HUggingFaceEndpoint  
from dotenv import load_dotenv

load_dotenv()  

model_id = "google/flan-t5-xxl"  # Replace with your desired model ID
llm = HuggingFaceHub(
    repo_id=model_id,
    model_kwargs={"temperature": 0, "max_length": 512}
)

result = llm("What is the capital of France?")

print(result)