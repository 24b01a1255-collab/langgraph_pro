from utils.retriever import retriever
from utils.llm import get_llm

llm = get_llm()


def records_node(state):

    query = state["user_query"]

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an IPL records expert.

Answer using only the context.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }
