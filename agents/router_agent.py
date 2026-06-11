def router_node(state):

    query = state["user_query"].lower()

    if any(word in query for word in [
        "runs",
        "batting",
        "strike rate",
        "century",
        "kohli",
        "rohit",
        "rahul"
    ]):
        qtype = "batting"

    elif any(word in query for word in [
        "wicket",
        "economy",
        "bowling",
        "bumrah",
        "rashid"
    ]):
        qtype = "bowling"

    elif any(word in query for word in [
        "pitch",
        "stadium",
        "venue",
        "ground"
    ]):
        qtype = "venue"

    elif "vs" in query:
        qtype = "h2h"

    elif any(word in query for word in [
        "form",
        "last 5",
        "recent"
    ]):
        qtype = "form"

    else:
        qtype = "records"

    print(f"\nROUTER → {qtype}")

    return {
        "query_type": qtype
    }