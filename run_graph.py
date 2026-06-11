from graph import build_graph

graph = build_graph()


def ask_question(question: str):

    result = graph.invoke(
        {
            "user_query": question
        }
    )

    return result["final_answer"]