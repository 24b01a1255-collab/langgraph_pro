from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma_db"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

query = input("Ask a question: ")

results = db.similarity_search(query, k=3)

print("\nTop Results:\n")

for i, doc in enumerate(results, start=1):
    print("=" * 70)
    print(f"Result {i}")
    print("=" * 70)
    print(doc.page_content[:700])
    print()