from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat

load_dotenv()

API_Key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(
        api_key=API_Key,
        id="gpt-4o-mini"
    ),
    markdown=True
)

agent.print_response("Conte uma frase impactante sobre programação")