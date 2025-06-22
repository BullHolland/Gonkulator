import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import tempfile

# Load environment variables
load_dotenv()

# --- App Configuration ---
st.set_page_config(
    page_title="AI Knowledge Base Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #4a4a4a;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1.2rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        border-left: 5px solid #0d6efd;
    }
    .user-message {
        background-color: #e9f5ff;
        border-left-color: #0d6efd;
    }
    .assistant-message {
        background-color: #f8f9fa;
        border-left-color: #6c757d;
    }
    .info-box {
        background-color: #e6f7ff;
        border: 1px solid #91d5ff;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    .upload-section {
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
def initialize_session_state():
    """Initializes session state variables if they don't exist."""
    st.session_state.setdefault('messages', [])
    st.session_state.setdefault('conversation_chain', None)
    st.session_state.setdefault('uploaded_files_info', [])
    st.session_state.setdefault('vector_store', None)


# --- Core Functions ---
def process_uploaded_files(uploaded_files):
    """Processes uploaded PDF files, extracts text, and returns document chunks."""
    all_chunks = []
    for uploaded_file in uploaded_files:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            loader = PyPDFLoader(tmp_file_path)
            documents = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1200, chunk_overlap=200
            )
            chunks = text_splitter.split_documents(documents)
            all_chunks.extend(chunks)

            os.unlink(tmp_file_path)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
    return all_chunks


def create_vector_store(text_chunks):
    """Creates a vector store from document chunks."""
    if not text_chunks:
        st.warning("No text content found in the uploaded files.")
        return None
    try:
        embeddings = OpenAIEmbeddings()
        vector_store = Chroma.from_documents(documents=text_chunks, embedding=embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Error creating vector store: {e}")
        return None


def create_conversation_chain(vector_store):
    """Creates a conversational retrieval chain."""
    try:
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.6,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
        )
        return conversation_chain
    except Exception as e:
        st.error(f"Error creating conversation chain: {e}")
        return None


def display_chat_message(role, content):
    """Displays a chat message with appropriate styling."""
    role_map = {"user": "You", "assistant": "AI Assistant"}
    message_class = f"{role}-message"
    st.markdown(f"""
    <div class="chat-message {message_class}">
        <strong>{role_map.get(role, "Unknown")}:</strong><br>
        {content}
    </div>
    """, unsafe_allow_html=True)


# --- Main Application ---
def main():
    initialize_session_state()

    st.markdown('<h1 class="main-header">🧠 AI Knowledge Base Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Upload your documents and start a conversation with your own AI assistant.</p>', unsafe_allow_html=True)

    # --- Sidebar ---
    with st.sidebar:
        st.header("⚙️ Configuration")
        st.markdown("---")

        st.subheader("1. Enter your API Key")
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
            help="Get your API key from https://platform.openai.com/api-keys"
        )
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key

        st.subheader("2. Upload Your Documents")
        uploaded_files = st.file_uploader(
            "Upload PDF files to build your knowledge base.",
            type=['pdf'],
            accept_multiple_files=True,
            help="You can upload multiple PDF files."
        )

        if st.button("Build Knowledge Base"):
            if not api_key:
                st.warning("Please enter your OpenAI API key first.")
            elif not uploaded_files:
                st.warning("Please upload at least one PDF file.")
            else:
                with st.spinner("Processing documents and building knowledge base... This may take a moment."):
                    text_chunks = process_uploaded_files(uploaded_files)
                    vector_store = create_vector_store(text_chunks)
                    if vector_store:
                        st.session_state.vector_store = vector_store
                        st.session_state.conversation_chain = create_conversation_chain(vector_store)
                        st.session_state.uploaded_files_info = [f.name for f in uploaded_files]
                        st.success("Knowledge base is ready!")
                    else:
                        st.error("Failed to build the knowledge base. Please check the files and try again.")
        
        st.markdown("---")
        if st.session_state.uploaded_files_info:
            st.subheader("✅ Active Knowledge Base")
            for filename in st.session_state.uploaded_files_info:
                st.write(f"• {filename}")
        
        if st.button("Clear Knowledge Base"):
            initialize_session_state() # Resets all session state
            st.rerun()

    # --- Main Chat Area ---
    if not st.session_state.conversation_chain:
        st.info("Please configure your API key and build a knowledge base in the sidebar to begin.")
    else:
        # Display chat history
        for message in st.session_state.messages:
            display_chat_message(message["role"], message["content"])

        # Chat input
        if prompt := st.chat_input("Ask a question about your documents..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            display_chat_message("user", prompt)

            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.conversation_chain({"question": prompt})
                    ai_response = response["answer"]
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                    display_chat_message("assistant", ai_response)
                except Exception as e:
                    error_msg = f"Sorry, an error occurred: {str(e)}"
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
                    display_chat_message("assistant", error_msg)

if __name__ == "__main__":
    main() 