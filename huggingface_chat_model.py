from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    model = "Qwen/Qwen3-8B",
    temperature = 0,
    task = "text generation"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of South Korea?")
print(response.content)