# Student AI Assistant - Customer Research & Validation

A Streamlit-based AI assistant that helps students learn about customer research and validation techniques based on "Talking To Humans" and "The Mom Test" by Rob Fitzpatrick.

## 🚀 Features

- **AI-Powered Chat Interface**: Interactive conversation with an AI trained on customer research methodologies
- **Knowledge Base**: Built-in knowledge from "Talking To Humans" and "The Mom Test"
- **Conversation Memory**: Maintains context throughout the conversation
- **Modern UI**: Clean, responsive interface with custom styling
- **Real-time Responses**: Instant AI responses using OpenAI's GPT models
- **Suggested Questions**: Pre-built prompts to help students get started

## 📚 Knowledge Base

The AI assistant has been trained on key concepts from:

### Talking To Humans
- Customer Discovery Process
- Interview Techniques
- Problem Validation
- Solution Testing
- Market Research
- Pivot Strategies

### The Mom Test
- The Mom Test Rule
- Avoiding Biased Questions
- Focusing on Past Behavior
- Specific vs. Vague Questions
- Commitment and Advancement
- The Three Types of Bad Data

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Gonkulator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# Copy the example file
cp env_example.txt .env

# Edit the .env file and add your OpenAI API key
OPENAI_API_KEY=your_actual_api_key_here
```

### 4. Get OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in
3. Create a new API key
4. Copy the key to your `.env` file

## 🚀 Running the Application

### Local Development
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Deployment to Streamlit Cloud
1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy the app

## 📖 Usage Guide

### Getting Started
1. **Enter API Key**: Input your OpenAI API key in the sidebar
2. **Wait for Initialization**: The AI assistant will load the knowledge base
3. **Start Chatting**: Begin asking questions about customer research

### Suggested Questions
- "How do I conduct effective customer interviews?"
- "What is the Mom Test and how do I apply it?"
- "How can I validate if my problem is real?"
- "What are the three types of bad data in customer research?"
- "How do I avoid asking biased questions?"
- "What's the customer discovery process?"

### Features
- **Chat History**: All conversations are saved during the session
- **Clear Chat**: Reset the conversation at any time
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Processing**: Instant responses from the AI

## 🏗️ Architecture

The application uses:
- **Streamlit**: Web framework for the user interface
- **LangChain**: Framework for building LLM applications
- **OpenAI GPT**: Language model for generating responses
- **FAISS**: Vector database for efficient knowledge retrieval
- **ConversationalRetrievalChain**: Manages conversation flow and context

## 🔧 Customization

### Adding More Knowledge
To add more content to the knowledge base, edit the `KNOWLEDGE_BASE` dictionary in `app.py`:

```python
KNOWLEDGE_BASE = {
    "Your Book Title": """
    Your book content here...
    """,
    # Add more books as needed
}
```

### Changing AI Model
Modify the model settings in the `create_conversation_chain` function:

```python
llm = ChatOpenAI(
    model_name="gpt-4",  # Change to gpt-4 for better responses
    temperature=0.5,     # Adjust creativity (0.0-1.0)
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🐛 Troubleshooting

### Common Issues

**"OpenAI API key not found"**
- Ensure your `.env` file exists and contains the correct API key
- Check that the API key is valid and has sufficient credits

**"Error creating knowledge base"**
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check your internet connection

**"AI responses are slow"**
- Consider using a faster model like `gpt-3.5-turbo`
- Reduce the number of retrieved documents in the search

### Support
For issues and questions, please open an issue on GitHub.

## 📚 Additional Resources

- [Talking To Humans](https://talkingtohumans.com/)
- [The Mom Test](https://momtestbook.com/)
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/) 