from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PDF_PATH = "data/IPL_LangGraph_RAG_Dataset.pdf"
CHROMA_PATH = "chroma_db"


def build_vector_db():
    print("Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating ChromaDB...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    print("Vector DB created successfully")
    print(f"Total Chunks Stored: {len(chunks)}")


if __name__ == "__main__":
    build_vector_db()