def validation_node(state):

    query = state["user_query"].lower()

    out_of_scope_keywords = [
        "bcci",
        "world cup",
        "football",
        "nba",
        "ipl 2027",
        "ipl 2028"
    ]

    for keyword in out_of_scope_keywords:

        if keyword in query:

            return {
                "final_answer":
                "This question is outside the IPL dataset scope."
            }

    return {}