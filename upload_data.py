from pymongo import MongoClient
import pandas as pd
import json
# uri 

url = "mongodb+srv://krish:krish@cluster0.sytyfdb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server
client = MongoClient(url)

# create database and collection name
DATA_BASE_NAME = "pwskills"
COLLECTION_NAME = 'waferfault'

df = pd.read_csv("C:\Users\LENOVO\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop('Unnamed: 0',axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATA_BASE_NAME][COLLECTION_NAME].insert_many(json_record)

