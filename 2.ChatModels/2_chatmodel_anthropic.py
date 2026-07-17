from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-v1")

result = model.invoke("Write a poem about the ocean."   )

print(result)