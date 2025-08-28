from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv
import os
from agno.models.openai import OpenAIChat

load_dotenv()

API_Key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="""
    Você é um agente do YouTube.
    Obtenha as legendas de um vídeo do YouTube e responda às perguntas.
    """
)

agent.print_response("Sumarize esse video: https://www.youtube.com/watch?v=-yY30BhUSck", markdown=True)