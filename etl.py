import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def extract():
    api_url = "https://official-joke-api.appspot.com/random_joke"
    data = requests.get(api_url).json()
    return data

def transform(data):
    transform_data = {
        "id": [data["id"]],
        "type": [data["type"]],
        "setup": [data["setup"]],
        "punchline": [data["punchline"]]
    }

    df = pd.DataFrame(transform_data)
    return df

def load(df):
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
    df.to_sql("jokes", engine, if_exists="append", index=False)

    print("Data successfully loaded into Postgresql!!")

raw_data = extract()
df = transform(raw_data)
print(df)
load(df)
