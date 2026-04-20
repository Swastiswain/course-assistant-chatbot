from typing import TypedDict, List
from langgraph.graph import StateGraph
from rag.retriever import get_relevant_docs


# ✅ State (with memory)
class AgentState(TypedDict):
    query: str
    docs: List[str]
    answer: str
    history: List[dict]


# ✅ Step 1: Retrieve docs
def retrieve(state: AgentState):
    query = state["query"]
    docs = get_relevant_docs(query)
    return {"docs": docs}


# ✅ Step 2: Generate answer (with memory)
def generate(state: AgentState):
    query = state["query"]
    docs = state["docs"]
    history = state.get("history", [])

    context = "\n".join(docs)

    answer = f"""
Previous Conversation:
{history}

Current Question:
{query}

Context:
{context}

Answer:
LangChain is a framework for building LLM-powered applications.
"""

    # ✅ Update memory
    history.append({
        "question": query,
        "answer": answer
    })

    return {
        "answer": answer,
        "history": history
    }


# ✅ Build Graph
def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("retrieve", retrieve)
    builder.add_node("generate", generate)

    builder.set_entry_point("retrieve")
    builder.add_edge("retrieve", "generate")

    graph = builder.compile()
    return graph