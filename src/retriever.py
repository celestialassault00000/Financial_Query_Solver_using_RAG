from src.load_pinecone_index import index
from src.embedding import embeddings
from src.load_Cohere import co 
def retriever(query, index = index, embeddings= embeddings):
    embed_query = embeddings(query)
    pc = index.query(vector = embed_query,top_k=10, include_values = False, include_metadata = True, namespace="Fianl_set1")
    id_from_docs =[]
    text_retrieved =[]
    for i in pc["matches"]:
        id_from_docs.append(i["id"])
    for i in pc["matches"]:
        text_retrieved.append(i["metadata"]["text"])
    rerank_docs = co.rerank(query=query, documents=text_retrieved, top_n=5, model="rerank-english-v2.0")
    text =""
    text = text +"\n"+  rerank_docs[0].document["text"]
    text = text + "\n"+  rerank_docs[1].document["text"]
    text = text + "\n"+  rerank_docs[2].document["text"]
    text = text +"\n"+  rerank_docs[3].document["text"]
    text = text +"\n"+  rerank_docs[4].document["text"]
    response = co.summarize(
    text=text,
    model='command',
    length='long',
    extractiveness='high')
    return response.summary