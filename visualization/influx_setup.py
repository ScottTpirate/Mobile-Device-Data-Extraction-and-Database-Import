from influxdb import InfluxDBClient
import json

def setup_influxdb():
    client = InfluxDBClient(host='localhost', port=8086)
    client.create_database('device_data')
    client.switch_database('device_data')

    with open('data_extraction/ios_data.json', 'r') as file:
        ios_data = json.load(file)

    with open('data_extraction/android_data.json', 'r') as file:
        android_data = json.load(file)

    data = [
        {
            "measurement": "device_info",
            "tags": {
                "device": ios_data["device"]
            },
            "fields": {
                "info": str(ios_data["info"])
            }
        },
        {
            "measurement": "device_info",
            "tags": {
                "device": android_data["device"]
            },
            "fields": {
                "info": str(android_data["info"])
            }
        }
    ]
    client.write_points(data)

if __name__ == "__main__":
    setup_influxdb()
