from typing import TypedDict


class IPLState(TypedDict):
    user_query: str

    query_type: str

    final_answer: str