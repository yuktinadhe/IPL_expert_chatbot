import os
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings


# 1. Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# 2. Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# 3. Load the IPL PDF
loader = PyPDFLoader("data/IPL_QA_Dataset_1000.pdf")
documents = loader.load()

# 4. Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# 5. Convert to embeddings (using sentence-transformers)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 6. Store in FAISS
db = FAISS.from_documents(docs, embeddings)

# 7. Ask Question function
def ask_question(query: str) -> str:
    # Search similar chunks
    results = db.similarity_search(query, k=3)
    context = "\n".join([r.page_content for r in results])

    prompt = f"""
    You are an IPL expert chatbot.
    Answer the question based only on the given context.

    Context:
    {context}

    Question: {query}
    """

    # Call Gemini API
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    return response.text
