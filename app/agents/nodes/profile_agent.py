import json

from app.agents.llm import ask_llm

from app.agents.tools import (
    update_profile_tool
)


def profile_agent_node(state):

    user_message = state["user_message"]

    telegram_id = state["telegram_id"]

    prompt = f"""
Extract profile update info.

Allowed fields:
- name
- age
- sex
- phone_number

Return ONLY JSON.

Example:

{{
    "field": "name",
    "value": "Rahul"
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

    # HANDLE LIST RESPONSE
    if isinstance(data, list):

        data = data[0]

    field = data.get("field")

    value = data.get("value")

    success = update_profile_tool(
        telegram_id,
        field,
        value
    )

    if success:

        state["response"] = (
            f"Updated your {field} successfully."
        )

    else:

        state["response"] = (
            "Failed to update profile."
        )

    return state