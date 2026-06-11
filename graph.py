from langgraph.graph import StateGraph, END

from state import IPLState

from agents.router_agent import router_node
from agents.batting_agent import batting_node
from agents.bowling_agent import bowling_node
from agents.venue_agent import venue_node
from agents.h2h_agent import h2h_node
from agents.form_agent import form_node
from agents.records_agent import records_node


def batting_node(state):

    return {
        "final_answer":
        f"[BATTING NODE] Query classified as batting"
    }


def bowling_node(state):

    return {
        "final_answer":
        f"[BOWLING NODE] Query classified as bowling"
    }


def venue_node(state):

    return {
        "final_answer":
        f"[VENUE NODE] Query classified as venue"
    }


def h2h_node(state):

    return {
        "final_answer":
        f"[H2H NODE] Query classified as h2h"
    }


def form_node(state):

    return {
        "final_answer":
        f"[FORM NODE] Query classified as form"
    }


def records_node(state):

    return {
        "final_answer":
        f"[RECORDS NODE] Query classified as records"
    }


def route_query(state):

    return state["query_type"]


def build_graph():

    graph = StateGraph(IPLState)

    graph.add_node("router", router_node)

    graph.add_node("batting", batting_node)

    graph.add_node("bowling", bowling_node)

    graph.add_node("venue", venue_node)

    graph.add_node("h2h", h2h_node)

    graph.add_node("form", form_node)

    graph.add_node("records", records_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges(
        "router",
        route_query,
        {
            "batting": "batting",
            "bowling": "bowling",
            "venue": "venue",
            "h2h": "h2h",
            "form": "form",
            "records": "records"
        }
    )

    graph.add_edge("batting", END)
    graph.add_edge("bowling", END)
    graph.add_edge("venue", END)
    graph.add_edge("h2h", END)
    graph.add_edge("form", END)
    graph.add_edge("records", END)

    return graph.compile()