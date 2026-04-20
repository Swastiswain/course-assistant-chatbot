from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from data.documents import documents

# Step 1: Convert documents into text list
texts = [doc["text"] for doc in documents]

# Step 2: Create embeddings model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 3: Create vector DB
vectorstore = Chroma.from_texts(
    texts=texts,
    embedding=embedding_model
)

# Step 4: Create retriever
retriever = vectorstore.as_retriever()

# Function to use in project
def get_relevant_docs(query):
    docs = retriever.invoke(query)
    return [doc.page_content for doc in docs]