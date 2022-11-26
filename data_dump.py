import pymongo 
import pandas as pd 
import json

#Connection link 
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")


#Give the database name and collection name
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

Data_filepath="/config/workspace/aps_failure_training_set1.csv"
if __name__ == "__main__":
    df = pd.read_csv("/config/workspace/aps_failure_training_set1.csv")
    print(f"rows and columns:{df.shape}")


    #covert df into json format before dumping, since mongodb doesnt take in other formats 
    df.reset_index(drop=True, inplace=True)

    #convert into json 
    json_record =list(json.loads(df.T.to_json()).values())
    print(json_record[0])


    #insert the converted json record to mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)