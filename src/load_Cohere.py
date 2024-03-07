import cohere
from dotenv import load_dotenv
import os
load_dotenv()
cohere_api_key= os.getenv("cohere_api_key")
co = cohere.Client(cohere_api_key)