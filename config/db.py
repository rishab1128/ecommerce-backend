from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

load_dotenv()

MONGO_TEST_URI = os.getenv("MONGO_URI")

connection = MongoClient(MONGO_TEST_URI, tlsCAFile=certifi.where())

