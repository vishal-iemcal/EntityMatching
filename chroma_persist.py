import chromadb
from chromadb.utils import embedding_functions
import csv

collection_name = "test_collection"

chroma_client  = chromadb.PersistentClient(path = "./db/chroma_persist")
default_ef = embedding_functions.DefaultEmbeddingFunction()


collection = chroma_client.get_or_create_collection(collection_name , embedding_function=default_ef)

#read documents from csv file

with open('./DataSpreadsheet.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

documents = [
        {"id" : "doc1" , "text" : "Hello, world!"},
        {"id" : "doc2" , "text" : "Hello, how are you today?"},
        {"id" : "doc3" , "text" : "Hello, where are you going today!"},
        {"id" : "doc4" , "text" : "Hello, I am feeling happy today!"},
        {
            "id" : "doc5" , "text" : "Its a technology company that builds computers"
        },
]

for doc in documents:
    collection.upsert(ids=[doc["id"]] , documents=[doc["text"]])

    query_text = "Age of the Earth"

    results = collection.query(query_texts=[query_text] , n_results=4)

    for idx , document in enumerate(results["documents"][0]):
        doc_id = results["ids"][0][idx]
        distance = results["distances"][0][idx]

    print(
        f"For the query: {query_text} , \n Found similar document {document} (ID: {doc_id} , Distance: {distance})"
    )