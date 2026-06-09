from langgraph.graph import StateGraph, START, END
from app.state.call_state import CallState

from langgraph.graph import StateGraph
from langgraph.graph import START, END

from app.state.call_state import CallState

from app.graph.nodes import (
    extract_information_node,
    router_node,
    execute_tool_node,
    response_node
)

graph = StateGraph(CallState)

graph.add_node(
    "extract_information",
    extract_information_node
)

graph.add_node(
    "router",
    router_node
)

graph.add_node(
    "response",
    response_node
)

graph.add_node(
    "execute_tool",
    execute_tool_node
)

graph.add_edge(
    START,
    "extract_information"
)

graph.add_edge(
    "extract_information",
    "router"
)

graph.add_edge(
    "router",
    "execute_tool"
)

graph.add_edge(
    "execute_tool",
    "response"
)

graph.add_edge(
    "response",
    END
)

travel_graph = graph.compile()