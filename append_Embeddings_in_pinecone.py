import dotenv
from dotenv import load_dotenv
load_dotenv()
from pinecone import Pinecone
import time
pc = Pinecone()
index = pc.Index("finance")

def upsert_data_in_pinecone(dict, index = index):
    time.sleep(2)
    """Takes input a dict contain {"id": str(id), "values":[], "metadata":{"text": text of chunk}}"""
    index.upsert(vectors=[dict], namespace="set1")