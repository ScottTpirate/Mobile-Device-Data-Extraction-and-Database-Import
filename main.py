import os
import subprocess

def extract_data():
    print("Extracting iOS data...")
    os.system('python data_extraction/extract_ios.py')
    
    print("Extracting Android data...")
    os.system('python data_extraction/extract_android.py')

def import_data():
    print("Importing data into SQLite database...")
    os.system('python database/import_data.py')

def setup_influxdb():
    print("Setting up InfluxDB...")
    os.system('python visualization/influxdb_setup.py')

def main():
    extract_data()
    import_data()
    setup_influxdb()
    print("All tasks completed successfully.")

if __name__ == "__main__":
    main()
