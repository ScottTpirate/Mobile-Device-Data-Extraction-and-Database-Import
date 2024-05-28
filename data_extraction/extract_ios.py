import imobiledevice
import json

def extract_ios_data():
    idevice = imobiledevice.iDevice()
    device_info = idevice.get_info()
    with open('ios_data.json', 'w') as file:
        json.dump(device_info, file)

if __name__ == "__main__":
    extract_ios_data()
