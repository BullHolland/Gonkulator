import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import json

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Student AI Assistant - Customer Research",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #1f77b4;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left-color: #2196f3;
    }
    .assistant-message {
        background-color: #f3e5f5;
        border-left-color: #9c27b0;
    }
    .info-box {
        background-color: #e8f5e8;
        border: 1px solid #4caf50;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Knowledge base content (you can replace this with actual book content)
KNOWLEDGE_BASE = {
    "Talking To Humans": """
    Talking To Humans is a comprehensive guide to customer discovery and validation. 
    Key concepts include:
    
    1. **Customer Discovery Process**: Systematic approach to understanding customer needs
    2. **Interview Techniques**: How to conduct effective customer interviews
    3. **Problem Validation**: Identifying and validating real customer problems
    4. **Solution Testing**: Testing proposed solutions with potential customers
    5. **Market Research**: Understanding market dynamics and competition
    6. **Pivot Strategies**: When and how to pivot based on customer feedback
    
    The book emphasizes the importance of getting out of the building and talking to real customers
    rather than making assumptions about what they want or need.
    """,
    
    "The Mom Test": """
    The Mom Test by Rob Fitzpatrick focuses on how to ask better questions to get honest feedback.
    Key principles include:
    
    1. **The Mom Test Rule**: If you can't tell your mom about your business without her lying to you,
       you're asking the wrong questions.
    
    2. **Avoiding Biased Questions**: Don't ask questions that lead to false positives or make people
       want to please you.
    
    3. **Focusing on Past Behavior**: Ask about what people have actually done, not what they would do.
    
    4. **Specific vs. Vague Questions**: Ask for specific examples and concrete details.
    
    5. **Commitment and Advancement**: Look for signs of real commitment, not just polite interest.
    
    6. **The Three Types of Bad Data**:
       - Compliments (people being nice)
       - Fluff (generic, non-actionable feedback)
       - Ideas (people suggesting features instead of describing problems)
    
    The book teaches how to structure conversations to get honest, actionable feedback that can
    guide product development decisions.
    """
}

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'conversation_chain' not in st.session_state:
        st.session_state.conversation_chain = None
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None

def create_knowledge_base():
    """Create a vector store from the knowledge base"""
    try:
        # Combine all knowledge base content
        combined_text = ""
        for book, content in KNOWLEDGE_BASE.items():
            combined_text += f"Book: {book}\n{content}\n\n"
        
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(combined_text)
        
        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(chunks, embeddings)
        
        return vector_store
    except Exception as e:
        st.error(f"Error creating knowledge base: {str(e)}")
        return None

def create_conversation_chain(vector_store):
    """Create a conversation chain with the vector store"""
    try:
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
            return_source_documents=True
        )
        
        return conversation_chain
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None

def display_chat_message(role, content):
    """Display a chat message with proper styling"""
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>AI Assistant:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">🤖 Student AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Customer Research & Validation Expert</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📚 Knowledge Base")
        st.write("This AI assistant has been trained on:")
        
        for book in KNOWLEDGE_BASE.keys():
            st.write(f"• **{book}**")
        
        st.markdown("---")
        
        st.header("🎯 Suggested Questions")
        st.write("Try asking about:")
        st.write("• Customer interview techniques")
        st.write("• How to validate problems")
        st.write("• Avoiding biased questions")
        st.write("• The Mom Test principles")
        st.write("• Customer discovery process")
        
        st.markdown("---")
        
        # API Key input
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Enter your OpenAI API key to use the AI assistant"
        )
        
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            
            # Initialize AI if not already done
            if st.session_state.conversation_chain is None:
                with st.spinner("Initializing AI assistant..."):
                    vector_store = create_knowledge_base()
                    if vector_store:
                        st.session_state.vector_store = vector_store
                        st.session_state.conversation_chain = create_conversation_chain(vector_store)
                        st.success("AI assistant ready!")
    
    # Main content area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Info box
        if st.session_state.conversation_chain is None:
            st.markdown("""
            <div class="info-box">
                <strong>Getting Started:</strong><br>
                1. Enter your OpenAI API key in the sidebar<br>
                2. Wait for the AI assistant to initialize<br>
                3. Start asking questions about customer research and validation!
            </div>
            """, unsafe_allow_html=True)
        
        # Chat interface
        if st.session_state.conversation_chain:
            # Display chat history
            for message in st.session_state.messages:
                display_chat_message(message["role"], message["content"])
            
            # Chat input
            if prompt := st.chat_input("Ask me about customer research and validation..."):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                display_chat_message("user", prompt)
                
                # Get AI response
                with st.spinner("Thinking..."):
                    try:
                        response = st.session_state.conversation_chain({"question": prompt})
                        ai_response = response["answer"]
                        
                        # Add AI response to chat history
                        st.session_state.messages.append({"role": "assistant", "content": ai_response})
                        display_chat_message("assistant", ai_response)
                        
                    except Exception as e:
                        error_msg = f"Sorry, I encountered an error: {str(e)}"
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})
                        display_chat_message("assistant", error_msg)
            
            # Clear chat button
            if st.button("Clear Chat History"):
                st.session_state.messages = []
                st.rerun()

if __name__ == "__main__":
    main() 