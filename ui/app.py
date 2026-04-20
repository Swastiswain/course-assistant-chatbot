import sys
import os

# ✅ Fix import path (IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from graph.agent_graph import build_graph

# Build graph once
app = build_graph()

st.set_page_config(page_title="Course Assistant Chatbot")

st.title("🤖 Course Assistant Chatbot")

# ✅ Initialize memory
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Ask your question:")

# Button
if st.button("Send"):
    if user_input:
        state = {
            "query": user_input,
            "history": st.session_state.history
        }

        result = app.invoke(state)

        # Update memory
        st.session_state.history = result["history"]

# Display conversation
st.subheader("Conversation")

for item in st.session_state.history:
    st.markdown(f"**🧑 You:** {item['question']}")
    st.markdown(f"**🤖 Bot:** {item['answer']}")