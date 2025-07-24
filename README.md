
# ✨ GemBot: A Conversational AI with DeepSeek & Streamlit

Unleash the power of conversational AI with GemBot, a sleek and intelligent chatbot built with Streamlit and LangChain. Powered by Hugging Face's `deepseek-ai/DeepSeek-R1-0528` model, GemBot offers a natural, context-aware chat experience wrapped in a beautiful, dark-themed interface.

---

## 🚀 Key Features

| Feature             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| 🧠 Intelligent Core  | Leverages the powerful DeepSeek R1 model for nuanced and human-like conversational abilities. |
| 💬 Context-Aware     | Built-in LangChain memory ensures the chatbot remembers previous parts of the conversation. |
| 🎨 Sleek UI          | A modern, fully responsive, and dark-themed interface created with Streamlit. |
| 🔐 Secure & Simple   | Manages API keys securely using a .env file, keeping your credentials safe. |
| ⚙️ Easy to Run       | Get up and running in minutes with a simple installation process and minimal dependencies. |

---

## 🛠️ Tech Stack

- 🐍 **Python 3.10+**
- 🎈 **Streamlit**: For the interactive web application front-end.
- 🔗 **LangChain**: As the core framework for building the LLM application logic and memory.
- 🤗 **Hugging Face**: For providing the Inference API to the DeepSeek model.
- 🔐 **dotenv (`python-dotenv`)**: For managing environment variables securely.

---

## 📦 Getting Started

Follow these steps to set up and run GemBot on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gembot-chatbot.git
cd gembot-chatbot
```

### 2. Create a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Your API Key

Create a `.env` file in the root directory of the project:

```env
HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_key_here"
```

> You can get your API key from your Hugging Face account settings.

### 5. Run the Application

```bash
streamlit run app.py
```

Navigate to [http://localhost:8501](http://localhost:8501) in your browser to start chatting with GemBot!

---

## 💡 How to Use

1. Open the web application in your browser.
2. Type your message into the chat input at the bottom of the screen.
3. Press Enter or click the send button.
4. Enjoy your conversation! The bot will remember what you've talked about in the current session.

---

## 📂 Project Structure

```
gembot-chatbot/
├── .env                  # Stores environment variables (API key)
├── .gitignore            # Files to be ignored by Git
├── app.py                # The main Streamlit application script
├── requirements.txt      # Project dependencies
└── README.md
```

---


## 🙌 Acknowledgements

A huge thank you to the teams behind these incredible tools:

- DeepSeek AI  
- LangChain  
- Streamlit  
- Hugging Face  

---

### 💙 Made with love by [Abhinav Rai](https://github.com/abhinavrai03) 💙
