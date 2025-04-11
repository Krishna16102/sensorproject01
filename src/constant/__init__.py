import os

# MongoDB configurations
MONGO_DB_URL = "mongodb+srv://krish:krish@cluster0.sytyfdb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DATABASE_NAME = "pwskills"
MONGO_COLLECTION_NAME = "waferfault"

# AWS S3 bucket name
AWS_S3_BUCKET_NAME = "wafer-fault"

# Target column for model
TARGET_COLUMN = "quality"

# Model file configurations
MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"  # Corrected from ".pk1" to ".pkl" assuming it's a pickle file

artifact_folder = "artifacts"