from graph.agent_graph import build_graph

app = build_graph()

# ✅ Initial state with empty memory
state = {
    "query": "What is LangChain?",
    "history": []
}

# First question
result = app.invoke(state)

print("\nFIRST RESPONSE:\n")
print(result["answer"])

# Second question (memory test)
state["query"] = "Why is it used?"

result = app.invoke(state)

print("\nSECOND RESPONSE (with memory):\n")
print(result["answer"])