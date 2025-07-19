# 🧠 Ayurveda Research Agent

An AI agent built using [Agno](https://docs.agno.ai) and Gemini 1.5 Flash that answers user questions based on a specific Ayurveda research paper and sends the responses to the user’s email using SMTP via `agno.tools.email`.  
Includes retrieval-augmented generation (RAG), conversation memory, and natural language reasoning.

---

## Features

- **PDF Knowledge Base**: Embedded Ayurveda research paper (from PubMed)
- **AI Agent (Gemini 1.5 Flash)**: Reasoning-powered responses with Agno’s tool system
- **Conversation Memory**: Context-aware answers and follow-ups
- **Email Integration**: Sends responses to user emails using SMTP (`agno.tools.email`)
- **SQLite Storage**: Saves memory context to `history.db`

---

## Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/yourusername/ayurveda-query-agent.git
cd ayurveda-query-agent
```
### 2. Install Requirements
```
pip install -r requirements.txt
```
### 3. Add Your .env File
Create a .env file in the root directory:
```
GOOGLE_API_KEY=your_gemini_api_key
SENDER_EMAIL=youremail@example.com
SENDER_NAME=Your Name
SENDER_PASSKEY=your_app_password
DEFAULT_EMAIL=recipient@example.com
```
### 4. Run the Agent
```
python agent.py
```
You'll be prompted to enter the recipient's email and your question. The agent will fetch the answer and email it.
---
## Example
```
Enter receiver email (press Enter to use default): xyz@gmail.com
Hello, how may I help you? : Can ayurveda help with epilepsy?
```
You will receive an email with the response like:
```
"As you asked, here is the information from the research paper: The herbs mentioned for stress reduction are Ashwagandha and Brahmi..."
```
```
✅ Email sent to: xyz@gmail.com
```
---
## Built With
Agno – LLM agent framework

Gemini 1.5 Flash – Google’s multimodal LLM

agno.tools.email – Built-in SMTP email sender

lancedb – Vector storage for RAG

SQLite – Memory persistence
---
## Project Structure :
```
📂 ayurveda-research-agent/
├── agent.py # Main agent logic + email sending
├── knowledge_base.py # Loads PDF into vector DB
├── history.db # Conversation memory (SQLite)
├── .env # Secrets and credentials
├── requirements.txt
└── README.md
```
### Demo Video :
Watch the demo video [here](https://drive.google.com/file/d/14wySShbcZVO-UGQ_--m-e0WNU1mD0Sp8/view?usp=sharing)
