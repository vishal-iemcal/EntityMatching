from flask import Flask, jsonify , request

import chromadb
import os
from dotenv import load_dotenv
import csv
import pandas as pd
from flask_cors import CORS


import chromadb.utils.embedding_functions as embedding_functions

collection_name = "test_collection"

load_dotenv()
penai_api_key = os.getenv("OPENAI_API_KEY")

default_ef = embedding_functions.DefaultEmbeddingFunction()
chroma_client  = chromadb.PersistentClient(path = "./db/chroma_persist")
collection = chroma_client.get_or_create_collection(collection_name , embedding_function=default_ef)


app = Flask(__name__)
CORS(app)

@app.route("/getMatchList/")
def getMatches():
    #query_text = "ETB ENDTIMEBLESSING LLC LLC PA"
    #get the query parameters
    name = request.args.get("name")
    address = request.args.get("address")

    matchString = name + ' ' + address

    results = collection.query(query_texts=[name] , n_results=3)

    returnResults = []

    class matchedEntitities:
        def __init__(self, id , query_text, documentText , documentId , distance):
            self.query_text = query_text
            self.documentText = documentText
            self.documentId = documentId
            self.distance = distance

    for idx , document in enumerate(results["documents"][0]):
        doc_id = results["ids"][0][idx]
        distance = results["distances"][0][idx]
        #returnResults.append(f"For the query: {query_text} , \n Found similar document {document} (ID: {doc_id} , Distance: {distance})")
        matchedResult = {}
        matchedResult['id'] = idx
        matchedResult['document'] = document
        matchedResult['doc_id'] = doc_id
        matchedResult['distance'] = distance
        returnResults.append(matchedResult)
    return jsonify(returnResults), 200


if __name__ == "__main__":
    app.run(debug = True)