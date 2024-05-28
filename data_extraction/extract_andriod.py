import subprocess
import json

def run_adb_command(command):
    result = subprocess.run(['adb', 'shell', command], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def extract_android_data():
    data = run_adb_command('cat /proc/meminfo')
    with open('android_data.json', 'w') as file:
        json.dump({"meminfo": data}, file)

if __name__ == "__main__":
    extract_android_data()
