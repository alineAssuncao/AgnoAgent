from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

load_dotenv()

API_Key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini", api_key=API_Key),
    tools = [YFinanceTools(stock_price=True)], # habilita consulta de preço de ações
    markdown=True
)

agent.print_response("Qual o preço atual da ação do Google?", stream=True)