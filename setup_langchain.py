from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Connect to Qdrant
client = QdrantClient("http://localhost:6333")

# Load the embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a vector store using Qdrant and embeddings
vector_store = Qdrant(client, collection_name="my_collection", embeddings=embeddings)

# Define the OpenAI API key
import openai
openai.api_key = "your_openai_api_key"

# Load the OpenAI LLM model
llm = OpenAI()

# Define a prompt template for the LLM
prompt_template = PromptTemplate(
    input_variables=["retrieved_text", "question"],
    template="Based on the following information: {retrieved_text}, answer the question: {question}"
)

# Create a chain that uses the LLM
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

def generate_response(question):
    # Retrieve relevant information from the vector store
    docs = vector_store.similarity_search(query=question, k=3)
    retrieved_text = " ".join([doc.page_content for doc in docs])

    # Generate a response using the LLM
    response = llm_chain.run({"retrieved_text": retrieved_text, "question": question})
    return response

# Example usage
if __name__ == "__main__":
    prompt = "Tell me something interesting about AI."
    print(generate_response(prompt))
