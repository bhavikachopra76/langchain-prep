from dotenv import load_dotenv
from langchain_mistralai import MistralAIEmbeddings
load_dotenv()

embeddings = MistralAIEmbeddings(
    model = "codestral-embed-2505",
)

documents = [
    "What is the capital of India?",
    "What do you know about cricket?",
    "What is copper?"
]

result = embeddings.embed_query("Hi, How are you?")
result2 = embeddings.embed_documents(documents)
# print(str(result))
print(str(result2))