import json

from app.agents.llm import ask_llm


def router_node(state):

    user_message = state["user_message"]

    prompt = f"""
You are an AI router.

Possible intents:
- update_profile
- health_advice

Return ONLY JSON.

Examples:

{{
    "intent": "update_profile"
}}

{{
    "intent": "health_advice"
}}

User:
{user_message}
"""

    response = ask_llm(prompt)

    response = response.replace(
        "```json",
        ""
    ).replace(
        "```",
        ""
    )

    data = json.loads(response)

    state["intent"] = data["intent"]

    return state