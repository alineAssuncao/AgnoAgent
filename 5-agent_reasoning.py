from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools

load_dotenv()

API_Key = os.getenv("OPENAI_API_KEY")

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini", api_key=API_Key),
    tools = [
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            company_info=True,
            analyst_recommendations=True,
            company_news=True
        )
    ], 
    instructions=[
        "Usar tabelas para exibir os resultados.",
        "Exibir apenas o relatório, nenhum outro texto."
    ],
    markdown=True
)

agent.print_response("Escreva um relatório sobre a empresa Banco do Bradesco?", 
                     stream=True, 
                     show_full_reasoning=True,
                     stream_intermediate_steps=True)