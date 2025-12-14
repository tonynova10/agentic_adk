from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

# def get_current_time() -> dict:
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
#     return {
#         "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     } 

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='tool_agent',
    description='A helpful assistant for user questions.',
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search""",
    tools=[google_search], # Built-in tool from ADK
    # tools=[get_current_time], # Using a custom tool 
    # tools=[google_search, get_current_time] # <--- Doesn't work
)
