from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from utils.llm import get_llm

CHROMA_PATH = "chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 4})

llm = get_llm()

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an IPL expert assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find that information in the IPL dataset."

Context:
{context}

Question:
{question}

Answer:
"""
)

print("\nIPL RAG Chatbot Started")
print("Type 'exit' to quit\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)

    print("\nAnswer:")
    print(response.content)
    print("\n" + "=" * 80 + "\n")