from rag.retriever import get_relevant_docs

query = "What is LangChain?"

docs = get_relevant_docs(query)

print("\nRelevant Documents:\n")
for d in docs:
    print("-", d)