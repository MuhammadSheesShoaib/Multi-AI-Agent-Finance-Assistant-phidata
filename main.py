from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv


load_dotenv()
Groq.api_key=os.getenv("GROQ_API_KEY")


web_search_agent = Agent(
    name = "Web search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,
)

financial_agent = Agent(
    name = "Financial Agent",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, income_statements=True)],
    instructions = ["Use table to display the data"],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent = Agent(
    team = [web_search_agent, financial_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions = ["Always include sources", "Use table to display the data"],
    show_tool_calls = True,
    markdown = True,
)

query = input("Ask your Financial Assistant: ")

multi_ai_agent.print_response(query)

