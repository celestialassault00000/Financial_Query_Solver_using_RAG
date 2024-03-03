import os
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone
pinecone_api_key = os.getenv("pinecone_api_key")
pc = Pinecone(api_key = pinecone_api_key)
index = pc.Index("finance")
