from typing import TypedDict


class IPLState(TypedDict):
    user_query: str

    query_type: str

    retrieved_context: str

    final_answer: str