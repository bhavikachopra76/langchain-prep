from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()

model = init_chat_model(
    model = "groq:llama-3.1-8B-instant",
    temperature = 0
)

response = model.invoke("Hello how are you?")
print(response.content)