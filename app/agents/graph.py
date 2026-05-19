from langgraph.graph import StateGraph, END

from app.agents.state import (
    HealthAgentState
)

from app.agents.nodes.router import (
    router_node
)

from app.agents.nodes.profile_agent import (
    profile_agent_node
)

from app.agents.nodes.health_agent import (
    health_agent_node
)


# ---------------- ROUTER ---------------- #

def route_decision(state):

    intent = state["intent"]

    if intent == "update_profile":

        return "profile_agent"

    return "health_agent"


# ---------------- BUILD GRAPH ---------------- #

graph = StateGraph(
    HealthAgentState
)

graph.add_node(
    "router",
    router_node
)

graph.add_node(
    "profile_agent",
    profile_agent_node
)

graph.add_node(
    "health_agent",
    health_agent_node
)

graph.set_entry_point(
    "router"
)

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "profile_agent": "profile_agent",
        "health_agent": "health_agent"
    }
)

graph.add_edge(
    "profile_agent",
    END
)

graph.add_edge(
    "health_agent",
    END
)

app_graph = graph.compile()


# ---------------- RUN AGENT ---------------- #

def run_health_agent(
    telegram_id,
    user_message
):

    result = app_graph.invoke({

        "telegram_id": str(telegram_id),

        "user_message": user_message

    })

    return result["response"]