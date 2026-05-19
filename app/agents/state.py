from typing import TypedDict


class HealthAgentState(TypedDict):

    telegram_id: str

    user_message: str

    intent: str

    response: str