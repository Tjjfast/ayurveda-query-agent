from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.vectordb.lancedb import LanceDb
import os

from dotenv import load_dotenv

load_dotenv()

vector_db = LanceDb(
    table_name="paper_info",
    uri=r"C:\Codes\Ayurveda\knowledge",  
    embedder=GeminiEmbedder(api_key=os.getenv('GOOGLE_API_KEY')),
)

knowledge_base = PDFKnowledgeBase(
    path=r"C:\Codes\Ayurveda\pdf\AyurvedaForEpilepsy.pdf",  
    vector_db=vector_db,
    reader=PDFReader(chunk=True),
)
knowledge_base.load(recreate=False)
