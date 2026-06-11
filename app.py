from graph import build_graph


graph = build_graph()

print("IPL LangGraph Router Ready\n")

while True:

    query = input("Question: ")

    if query.lower() == "exit":
        break

    result = graph.invoke(
        {
            "user_query": query
        }
    )

    print()
    print(result["final_answer"])
    print()