# 🚀 Deployment Guide - Streamlit Cloud

This guide will help you deploy your Student AI Assistant to Streamlit Cloud for free.

## Prerequisites

1. **GitHub Account**: You'll need a GitHub account to host your code
2. **OpenAI API Key**: Get one from [OpenAI Platform](https://platform.openai.com/api-keys)
3. **Streamlit Account**: Sign up at [Streamlit Cloud](https://streamlit.io/cloud)

## Step-by-Step Deployment

### 1. Prepare Your Repository

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit: Student AI Assistant"
   git push origin main
   ```

2. **Verify Files**: Make sure these files are in your repository:
   - `app.py` (main application)
   - `advanced_app.py` (advanced version with PDF upload)
   - `requirements.txt` (dependencies)
   - `README.md` (documentation)
   - `.streamlit/config.toml` (Streamlit configuration)

### 2. Deploy to Streamlit Cloud

1. **Visit Streamlit Cloud**: Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)

2. **Sign In**: Use your GitHub account to sign in

3. **New App**: Click "New app"

4. **Connect Repository**:
   - Select your GitHub repository
   - Choose the branch (usually `main`)

5. **Configure App**:
   - **Main file path**: `app.py` (or `advanced_app.py` for the advanced version)
   - **App URL**: Will be auto-generated
   - **Python version**: 3.9 (recommended)

6. **Advanced Settings** (Optional):
   - **Secrets**: Add your OpenAI API key as a secret
   - **Requirements**: Should auto-detect from `requirements.txt`

### 3. Configure Secrets (Recommended)

Instead of asking users to enter their API key, you can set it as a secret:

1. **In Streamlit Cloud**:
   - Go to your app settings
   - Click "Secrets"
   - Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your-actual-api-key-here"
   ```

2. **Update the app** to use secrets:
   ```python
   # In app.py, replace the API key input with:
   api_key = st.secrets.get("OPENAI_API_KEY")
   if not api_key:
       st.error("OpenAI API key not found in secrets. Please contact the administrator.")
       st.stop()
   ```

### 4. Environment Variables

If you prefer environment variables, you can set them in Streamlit Cloud:

1. **Go to App Settings**
2. **Environment Variables**
3. **Add**:
   - Key: `OPENAI_API_KEY`
   - Value: Your actual API key

## 🎯 Quick Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] All required files present
- [ ] `requirements.txt` includes all dependencies
- [ ] App configured in Streamlit Cloud
- [ ] API key configured (secrets or environment variables)
- [ ] App deployed successfully
- [ ] Test the application

## 🔧 Troubleshooting

### Common Issues

**"Module not found" errors**
- Check that all dependencies are in `requirements.txt`
- Verify Python version compatibility

**"OpenAI API key not found"**
- Ensure API key is set in secrets or environment variables
- Check that the key is valid and has credits

**"App won't start"**
- Check the logs in Streamlit Cloud
- Verify the main file path is correct
- Ensure no syntax errors in your code

**"Slow loading"**
- Consider using a lighter model like `gpt-3.5-turbo`
- Optimize the knowledge base size

### Performance Optimization

1. **Use Caching**: Add `@st.cache_data` to expensive operations
2. **Optimize Dependencies**: Remove unused packages
3. **Reduce Model Size**: Use smaller models for faster responses
4. **Limit Knowledge Base**: Keep only essential content

## 📊 Monitoring

Streamlit Cloud provides:
- **App Analytics**: View usage statistics
- **Error Logs**: Monitor for issues
- **Performance Metrics**: Track response times

## 🔄 Updates

To update your deployed app:
1. Make changes to your code
2. Push to GitHub
3. Streamlit Cloud will automatically redeploy

## 🌐 Custom Domain (Optional)

For a custom domain:
1. **Purchase Domain**: From any registrar
2. **Configure DNS**: Point to Streamlit Cloud
3. **Add Domain**: In Streamlit Cloud settings
4. **SSL Certificate**: Automatically provided

## 📱 Mobile Optimization

The app is already mobile-responsive, but you can optimize further:
- Test on mobile devices
- Adjust font sizes if needed
- Ensure touch-friendly buttons

## 🔒 Security Considerations

1. **API Key Protection**: Never expose API keys in code
2. **Rate Limiting**: Consider implementing rate limits
3. **Input Validation**: Validate user inputs
4. **Error Handling**: Don't expose sensitive information in errors

## 📈 Scaling

If you need to scale:
1. **Upgrade Plan**: Consider paid Streamlit Cloud plans
2. **Optimize Code**: Reduce resource usage
3. **Caching**: Implement more aggressive caching
4. **CDN**: Use content delivery networks

## 🎉 Success!

Once deployed, your app will be available at:
`https://your-app-name-your-username.streamlit.app`

Share this URL with your students to start using the AI assistant! 