from app.agents.llm import ask_llm


def health_agent_node(state):

    user_message = state["user_message"]

    prompt = f"""
You are a helpful health assistant.

Give short general health guidance.

Never claim to be a doctor.

User:
{user_message}
"""

    response = ask_llm(prompt)

    state["response"] = response

    return state