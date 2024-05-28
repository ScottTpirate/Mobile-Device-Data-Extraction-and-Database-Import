import pandas as pd
from sqlalchemy import create_engine
import json

def import_data():
    with open('data_extraction/ios_data.json', 'r') as file:
        ios_data = json.load(file)

    with open('data_extraction/android_data.json', 'r') as file:
        android_data = json.load(file)

    data = {'device': ['iPhone', 'Samsung'], 'info': [ios_data, android_data]}
    df = pd.DataFrame(data)

    engine = create_engine('sqlite:///devices.db')
    df.to_sql('device_data', con=engine, if_exists='replace', index=False)

if __name__ == "__main__":
    import_data()
