# 🤖 Evihian - Setup & Usage Guide

A comprehensive guide to set up and run the Evihian with Gemini API and custom orange/gray/black theme.

## 📋 Prerequisites

- Python 3.8 or higher
- Internet connection
- Google Gemini API key

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. API Configuration

The project is configured to use **Google Gemini API** with the `gemini-2.0-flash` model.

Your API key is already configured in the `.env` file:
- **Gemini API Key**: `enter your key here`
- **Model**: `gemini-2.0-flash`

### 3. Verify Setup

Run the test script to ensure everything is working:

```bash
python test_setup.py
```

You should see all tests pass:
- ✅ Imports
- ✅ Database
- ✅ LLM API (Gemini)
- ✅ Tutorial Agent

## 🎨 Theme Configuration

The app features a custom **orange/gray/black** color scheme:

| Color | Hex Code | Usage |
|-------|----------|--------|
| Orange | `#ffa31a` | Primary buttons, headers, accents |
| Gray | `#808080` | Secondary text, borders |
| Dark Gray | `#292929` | Cards, secondary backgrounds |
| Black | `#1b1b1b` | Main background |
| White | `#ffffff` | Primary text |

## 🖥️ Running the Application

### Option 1: Web Interface (Recommended)

**Windows:**
```bash
# Double-click start_app.bat
# OR run manually:
streamlit run streamlit_app.py --server.port 8501
```

**Mac/Linux:**
```bash
streamlit run streamlit_app.py --server.port 8501
```

The app will open at: `http://localhost:8501`

### Option 2: Command Line Interface

```bash
python cli_demo.py
```

**CLI Commands:**
- `learn <subject>` - Start a new tutorial
- `test` - Request evaluation questions
- `history` - View past sessions
- `help` - Show available commands
- `quit` - Exit the application

## 📖 How to Use

### Starting a Tutorial

1. **Web Interface:**
   - Enter a subject in the sidebar
   - Click "Start Tutorial"
   - Or click any of the example topics

2. **CLI Interface:**
   ```
   > learn Python functions
   ```

### Interacting with the AI

- **Ask Questions**: Type any question about the subject
- **Get Evaluated**: Click "Test Me" or type "test me"
- **Quick Actions**: Use preset buttons for common requests

### Example Subjects

- Python Programming
- Machine Learning
- Data Science
- Web Development
- Statistics
- Linear Algebra
- Computer Networks
- Database Design
- React.js
- Docker

## 🔧 Configuration

### Environment Variables

All configuration is stored in `.env`:

```env
# Gemini API Configuration
GEMINI_API_KEY=enter ur key
LLM_MODEL=gemini-2.0-flash
LLM_TEMPERATURE=0.7

# Site Configuration
SITE_URL=http://localhost:8501
SITE_NAME=Evihian

# Database
DATABASE_PATH=tutorial_agent.db

# Theme Colors
THEME_PRIMARY_COLOR=#ffa31a
THEME_SECONDARY_COLOR=#808080
THEME_BACKGROUND_COLOR=#1b1b1b
THEME_SECONDARY_BACKGROUND_COLOR=#292929
THEME_TEXT_COLOR=#ffffff
THEME_CARD_COLOR=#292929
THEME_BORDER_COLOR=#808080
```

### Customizing the Theme

To modify colors, update the values in `.env` and restart the app.

## 🗄️ Database

- **Type**: SQLite
- **File**: `tutorial_agent.db`
- **Purpose**: Stores conversation history and learning progress
- **Location**: Project root directory

### Database Schema

```sql
-- Conversations table
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY,
    session_id TEXT,
    subject TEXT,
    created_at TIMESTAMP
);

-- Messages table
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    conversation_id INTEGER,
    role TEXT,
    content TEXT,
    message_type TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);
```

## 🔍 Troubleshooting

### Common Issues

1. **API Errors**
   - Verify your Gemini API key in `.env`
   - Check internet connection
   - Ensure API quota is not exceeded

2. **Port Already in Use**
   ```bash
   # Try different ports
   streamlit run streamlit_app.py --server.port 8502
   streamlit run streamlit_app.py --server.port 8503
   ```

3. **Import Errors**
   ```bash
   # Reinstall dependencies
   pip install --upgrade -r requirements.txt
   ```

4. **Database Issues**
   ```bash
   # Delete and recreate database
   del tutorial_agent.db  # Windows
   rm tutorial_agent.db   # Mac/Linux
   ```

5. **Theme Not Loading**
   - Ensure `theme.css` exists in the project directory
   - Check browser cache (Ctrl+F5 to hard refresh)

### Debugging Steps

1. Run the test script: `python test_setup.py`
2. Check the console output for error messages
3. Verify all files are present in the project directory
4. Ensure `.env` file has correct API key

## 📁 Project Structure

```
AITutorAgent/
├── .env                 # Environment variables (API keys, config)
├── theme.css           # Custom CSS theme
├── streamlit_app.py    # Main web application
├── cli_demo.py         # Command-line interface
├── tutorial_agent.py   # Core AI agent logic
├── database.py         # Database operations
├── LLM_api.py          # Gemini API integration
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── test_setup.py       # Setup verification script
├── start_app.bat       # Windows launcher script
└── tutorial_agent.db   # SQLite database (created on first run)
```

## 🚀 Features

### Core Functionality
- **📚 Subject Learning**: Generate comprehensive tutorials on any topic
- **💬 Interactive Q&A**: Ask follow-up questions and get detailed explanations
- **🧠 Knowledge Testing**: Automated evaluation questions to test understanding
- **💾 Conversation Persistence**: All interactions saved to SQLite database
- **🌐 Web Interface**: Beautiful Streamlit UI with custom theme
- **🖥️ CLI Interface**: Command-line option for quick testing

### Technical Features
- **LangGraph Orchestration**: Sophisticated agent workflow management
- **State Management**: Maintains conversation context and learning progress
- **Database Integration**: SQLite for reliable data persistence
- **Error Handling**: Robust error management throughout the system
- **Modular Design**: Clean, maintainable code structure
- **Custom Theming**: Professional orange/gray/black color scheme

## 🎯 Usage Tips

1. **Start Simple**: Begin with basic subjects to familiarize yourself
2. **Ask Specific Questions**: More specific questions yield better responses
3. **Use Evaluations**: Regular testing helps reinforce learning
4. **Review History**: Access previous sessions to continue learning
5. **Experiment**: Try different subjects and question types

## 🆘 Support

If you encounter issues:

1. Check this guide's troubleshooting section
2. Run the test script to identify problems
3. Verify your API key and internet connection
4. Ensure all dependencies are installed correctly

## 🎉 Ready to Learn!

Your Evihian is now configured and ready to use! 

**Quick Start:**
1. Run: `streamlit run streamlit_app.py`
2. Open: `http://localhost:8501`
3. Choose a subject and start learning!

Enjoy your personalized AI tutoring experience! 🚀📚