# Multi AI Agent Finance Assistant

## Overview
This is a **Multi AI Agent Finance Assistant**, designed to provide financial insights and web search capabilities. It operates as an AI-driven assistant that can:
- Fetch real-time stock market data using **yfinance via phidata**.
- Perform web searches using **DuckDuckGo via phidata**.
- Provide AI-powered financial insights using **Llama 3.3-70B Versatile** via **Groq API**.

This assistant is useful for traders, investors, and financial analysts who need quick and accurate financial data along with AI-powered insights.

## Technologies Used
- **Python**
- **phidata** (AI agent framework, handling workflows, finance data retrieval, and web search)
- **yfinance** (Financial data retrieval via phidata)
- **duckduckgo-search** (Web search via phidata)
- **Groq API** (Llama 3.3-70B Versatile for AI responses)
- **GitHub** (Version control)

## How It Works
This finance assistant consists of three AI agents working together:

1. **Web Search Agent**: Uses DuckDuckGo via phidata to fetch relevant financial news and information.
2. **Financial Agent**: Retrieves real-time stock market data using yfinance via phidata.
3. **Multi AI Agent**: Combines both agents and processes user queries using Llama 3.3-70B Versatile via the Groq API.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip
- A Groq API key (store it in a `.env` file as `GROQ_API_KEY`)

## Installation
1. Clone this repository:
```bash
   git clone https://github.com/MuhammadSheesShoaib/Multi-AI-Agent-Finance-Assistant-phidata.git
   cd Multi-AI-Agent-Finance-Assistant-phidata
```
2. Install dependencies:
```bash
  pip install -r requirements.txt
```
3. Set up your .env file:
```bash
  GROQ_API_KEY=your_api_key_here
```

## Usage
Run the assistant:
```bash
  python main.py
```
