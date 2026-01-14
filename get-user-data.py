import requests
import time
import os

def getUserData(user_id):
    try:
        response = requests.get(f"https://data-api.polymarket.com/trades?user={user_id}")
    except:
        print(f"Error: Failed getting data for user {user_id} with unknown error")

    if response.status_code != 200:
        print(f"Error: Failed getting data for user {user_id} with error code {response.status_code}")
        raise

    data = response.text
    return data


def saveUserData(user_id, data):
    try:
        os.mkdir("gamblers-fallacy/raw_users") #prayers and hopes
        print("Directory raw_users created.")
    except FileExistsError:
        print("Directory raw_users already exists.")
    except PermissionError:
        print("Permission to make dicrectory was denied.")
    except:
        print("error? error! error? error!") 

    try:
        with open(f"raw_users/{user_id}.txt", "w") as file:
            file.write(data)
    except:
        print(f"Error: Failed saving data for user {user_id}")

# ID NOT NAME
users = [
    "0x63ce342161250d705dc0b16df89036c8e5f9ba9a"  # Crypto bot making consistent money
    ]

for user_id in users:
    data = getUserData(user_id)
    saveUserData(user_id, data)
    print(f"Fetched data for user {user_id}")
    time.sleep(1)