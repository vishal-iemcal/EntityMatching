import chromadb
from chromadb.utils import embedding_functions


chroma_client = chromadb.Client()
collection_name = "test_collection"
default_ef = embedding_functions.DefaultEmbeddingFunction()

collection = chroma_client.get_or_create_collection(collection_name , embedding_function=default_ef)

documents = [
        {"id" : "doc1" , "text" : "Hello, world!"},
        {"id" : "doc2" , "text" : "Hello, how are you today?"},
        {"id" : "doc3" , "text" : "Hello, where are you going today!"},
        {"id" : "doc4" , "text" : "Hello, I am feeling happy today!"},
]



for doc in documents:
    collection.upsert(ids=[doc["id"]] , documents=[doc["text"]])

query_text = "Hello World , I am running this query!"

results = collection.query(query_texts=[query_text] , n_results=4)

#{'ids': [['doc1', 'doc2', 'doc3', 'doc4']], 'embeddings': None, 'documents': [['Hello, world!', 'Hello, how are you today?', 'Hello, where are you going today!', 
# 'Hello, I am feeling happy today!']], 'uris': None, 'data': None, 'metadatas': [[None, None, None, None]], 'distances':
#  [[1.002976894378662, 1.1340997219085693, 1.2206790447235107, 1.2258237600326538]], 'included': [<IncludeEnum.distances: 'distances'>, 
# <IncludeEnum.documents: 'documents'>, <IncludeEnum.metadatas: 'metadatas'>]}


for idx , document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]

    print(
        f"For the query: {query_text} , \n Found similar document {document} (ID: {doc_id} , Distance: {distance})"
    )







