import pymongo 
import pandas as pd 
import json
from dataclasses import dataclass

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var=EnvironmentVariable()


#Connection link 
client = pymongo.MongoClient("MONGO_DB_URL")


