# 🤖 Pychat-groq — AI Developer Chatbot

pychatbot-groq is a terminal-based AI chatbot built with Python that answers software development questions. It uses **Groq's LLaMA 3.3 70B** model for fast, streamed responses directly in your terminal.

---

## Features

- Ask any software development related question
- Real-time streamed responses in the terminal
- Powered by Groq's ultra-fast LLaMA 3.3 70B model
- Simple and lightweight CLI interface

---

## Tech Stack

- **Python 3**
- **Groq SDK** — LLM API client
- **LLaMA 3.3 70B Versatile** — underlying AI model
- **python-dotenv** — environment variable management

---

## Project Structure

```
pychatbot-groq/
├── src/
│   └── main.py        # main application logic
├── .env.example       # example env file
├── .gitignore
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd pychatbot-groq
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

> Get your free API key from [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
python src/main.py
```

---

## Usage

```
Enter 1 to ask questions and 2 to exit
Enter your choice
> 1
🤖 : what is your question
> What is a REST API?
🤖 :
A REST API (Representational State Transfer) is...
```

- Enter `1` to ask a question
- Enter `2` to exit

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

---

## License

MIT
