from agno.agent import Agent
from agno.models.google import Gemini
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.tools.reasoning import ReasoningTools
from agno.tools.email import EmailTools
from knowledge_base import knowledge_base

import os
from dotenv import load_dotenv 

load_dotenv() 

memory = Memory(
    model=Gemini(id='gemini-1.5-flash', api_key=os.getenv('GOOGLE_API_KEY')),
    db=SqliteMemoryDb(table_name="paper_info", db_file="history.db"),
    delete_memories=False,
    clear_memories=False,
)
instructions = [
    "You are an expert in Ayurveda, with access to a research paper knowledge base.",
    "Always search your knowledge base first before responding.",
    "Only if you cannot answer with knowledge from your database, you can use your internal knowledge.",
    "Remember our conversation history and refer to previous questions when relevant.",
    "If the user asks follow-up questions, connect them to our previous discussion.",
    "Perform exhaustive reasoning before answering.",
]

agent = Agent(
    model=Gemini(id='gemini-1.5-flash', api_key=os.getenv('GOOGLE_API_KEY')),
    tools=[
        ReasoningTools(add_instructions=True), 
        EmailTools(
            sender_email=os.getenv("SENDER_EMAIL"),
            sender_name=os.getenv("SENDER_NAME"),
            sender_passkey=os.getenv("SENDER_PASSKEY"),
        ),
    ],
    knowledge=knowledge_base,
    search_knowledge=True,
    memory=memory,
    add_history_to_messages=True,  #
    num_history_runs=10,
    enable_agentic_memory=True,
    show_tool_calls=True,
    markdown=True,
    instructions=instructions,
)

def ask_and_email():
    user_input = input("Enter receiver email (press Enter to use default): ").strip()
    if user_input and '@' in user_input and '.' in user_input:
        receiver_email = user_input
    else:
        print("Invalid or no email entered. Using default.")
        receiver_email = os.getenv('DEFAULT_EMAIL')

    user_query = input("Hello, how may I help you? : ").strip()

    for tool in agent.tools:
        if isinstance(tool, EmailTools):
            tool.receiver_email = receiver_email

    prompt = f"""
        Answer this question based on the Ayurveda diabetes research paper:
        "{user_query}"
        
        Then, send the answer to {receiver_email} via email.
    """

    response = agent.run(prompt)

    print("\n✅ Email sent to", receiver_email)
    print("📬 Agent Response:\n", response)



if __name__ == "__main__":
    ask_and_email()
