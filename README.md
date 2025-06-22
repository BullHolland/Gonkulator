# AI Knowledge Base Assistant

A Streamlit application that allows you to build a personal AI assistant by uploading your own documents to create a searchable knowledge base.

## 🚀 Features

- **Upload Your Own Documents**: Create a knowledge base from multiple PDF files.
- **AI-Powered Chat Interface**: Have a conversation with an AI that knows the content of your documents.
- **Dynamic Knowledge Base**: Easily clear and build new knowledge bases on the fly.
- **Conversation Memory**: The AI maintains context throughout your conversation.
- **Modern UI**: A clean and intuitive interface for a seamless user experience.
- **Secure API Key Handling**: Your OpenAI API key is handled securely.

## 🛠️ How It Works

The application uses the following technologies:

1.  **Streamlit**: For building the interactive web interface.
2.  **LangChain**: To orchestrate the flow of data between the user, the documents, and the language model.
3.  **OpenAI**: To generate embeddings for the documents and to power the conversational AI.
4.  **ChromaDB**: As the vector store to efficiently search the document knowledge base.

When you upload your documents, the app splits them into smaller chunks, converts them into numerical representations (embeddings), and stores them in a vector database. When you ask a question, the app searches the database for the most relevant chunks of text and provides them to the AI, along with your question, to generate a well-informed answer.

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.9+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Gonkulator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables (Optional)
You can create a `.env` file to store your OpenAI API key, or you can enter it directly into the application's interface.
```
OPENAI_API_KEY="your-api-key-here"
```

## 🚀 Running the Application

### Local Development
To run the app on your local machine, use the following command:
```bash
streamlit run app.py
```
The application will open in your browser at `http://localhost:8501`.

### Deployment to Streamlit Cloud
1.  Push your code to a GitHub repository.
2.  Visit [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3.  Connect your GitHub repository and select `app.py` as the main file.
4.  **Important**: Add your OpenAI API key as a "Secret" in the advanced settings of your Streamlit app. Use `OPENAI_API_KEY` as the secret name.

## 📖 Usage Guide

1.  **Enter your OpenAI API Key** in the sidebar.
2.  **Upload one or more PDF documents** using the file uploader.
3.  **Click "Build Knowledge Base"**. The app will process your documents.
4.  Once the knowledge base is ready, you can **start asking questions** in the chat interface.
5.  To start over with new documents, click **"Clear Knowledge Base"**.

## 🔧 Customization

You can easily customize the application:

-   **Language Model**: Change the `model_name` in the `create_conversation_chain` function in `app.py` to use a different OpenAI model (e.g., `gpt-4`).
-   **Text Splitting**: Adjust the `chunk_size` and `chunk_overlap` in the `process_uploaded_files` function to fine-tune how the documents are processed.
-   **UI and Styling**: Modify the CSS styles and Streamlit elements to change the look and feel of the app.

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