import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017")

DATABASE_NAME = 'APS'
COLLECTION_NAME = 'SENSORS'

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__":

    #Read the dataframe (.csv file)
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and Columns : {df.shape}')

    #Convert dataframe into json format so that we can dump it into mongodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Insert Converted json record into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

