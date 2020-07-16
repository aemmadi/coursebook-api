from pymongo import MongoClient
import os

from dotenv import load_dotenv
load_dotenv()

db = MongoClient(os.environ.get("DB_KEY"))
info_db = db.inf

