# load_data
import pandas as pd 
from dotenv import load_dotenv
import os 
load_dotenv() # Load .env variables 
DATA_PATH = os.getenv("DATA_PATH","data/raw/Clean_Dataset.csv")

def load_data(path=DATA_PATH):
    df=pd.read_csv(path)
    df.columns = df.columns.str.lower().str.strip()
    df.drop_duplicates(inplace=True)
    return df