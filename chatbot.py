import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")
st.markdown("Ask anything! Your conversation is private and stays on your device.")

# Initialize session state
if "chat_h" not in st.session_state:
    st.session_state.chat_h = [SystemMessage(content="You are a helpful assistant.")]
    st.session_state.display_history = []

# Chat form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message and press Enter...")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    st.session_state.chat_h.append(HumanMessage(content=user_input))
    response = model.invoke(st.session_state.chat_h)
    st.session_state.chat_h.append(AIMessage(content=response.content))
    st.session_state.display_history.append(("You", user_input))
    st.session_state.display_history.append(("AI", response.content))

# Display chat and allow downloading specific query-response
st.markdown("### 💬 Chat History")
for i in range(0, len(st.session_state.display_history), 2):
    user_msg = st.session_state.display_history[i][1]
    ai_msg = st.session_state.display_history[i + 1][1] if i + 1 < len(st.session_state.display_history) else "No reply"
    
    with st.expander(f"🧑 You: {user_msg[:50]}..."):
        st.markdown(f"**🧑 You:** {user_msg}")
        st.markdown(f"**🤖 AI:** {ai_msg}")
        download_text = f"You: {user_msg}\nAI: {ai_msg}"
        st.download_button(
            label="⬇️ Download This Conversation",
            data=download_text,
            file_name=f"query_{i//2 + 1}.txt",
            mime="text/plain",
            use_container_width=True
        )

# Full chat download
if st.session_state.display_history:
    chat_text = "\n".join([f"{speaker}: {msg}" for speaker, msg in st.session_state.display_history])
    st.download_button(
        label="⬇️ Download Full Chat History",
        data=chat_text,
        file_name="full_chat_history.txt",
        mime="text/plain",
        use_container_width=True
    )

# Clear chat
if st.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state.chat_h = [SystemMessage(content="You are a helpful assistant.")]
    st.session_state.display_history = []
    st.experimental_rerun()

st.markdown("---")

