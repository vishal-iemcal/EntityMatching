import chromadb
import os
from dotenv import load_dotenv
import csv
import pandas as pd

import chromadb.utils.embedding_functions as embedding_functions

collection_name = "test_collection"

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

default_ef = embedding_functions.DefaultEmbeddingFunction()
#openai_ef = embedding_functions.OpenAIEmbeddingFunction(api_key=openai_api_key , model_name="text-embedding-3-small")

chroma_client  = chromadb.PersistentClient(path = "./db/chroma_persist")

collection = chroma_client.get_or_create_collection(collection_name , embedding_function=default_ef)

documents = []

#read documents from csv file

with open('./us-businesses_master_50k_processed.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        documents.append(row)

for doc in documents:
    collection.upsert(ids=[doc["id"]] , documents=[doc["text"]])

print('##################The seed data embeddings successfully created in chroma database###################')

print('##################Running a test search to validate ##################################################')

query_text = "ETB ENDTIMEBLESSING LLC LLC PA"
results = collection.query(query_texts=[query_text] , n_results=4)

print(results)

for idx , document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]

    print(
        f"For the query: {query_text} , \n Found similar document {document} (ID: {doc_id} , Distance: {distance})"
    )



