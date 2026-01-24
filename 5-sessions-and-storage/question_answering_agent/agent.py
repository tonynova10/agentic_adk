from google.adk.agents import Agent

question_answering_agent = Agent(
    model='gemini-2.0-flash-001',
    name='question_answering_agent',
    description='Question answering agent',
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)
