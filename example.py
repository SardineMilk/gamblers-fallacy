import api
import time

# Only set this to True if you want new data
# Dont spam run if True
FETCH_DATA = False

# ID NOT NAME
users = [
    "0x63ce342161250d705dc0b16df89036c8e5f9ba9a"  # Crypto bot making consistent money
    ]

for user_id in users:
    if FETCH_DATA:
        data = api.getUserTrades(user_id)
        api.saveUserTrades(user_id, data)
        print(f"Fetched data for user {user_id}")
        time.sleep(1)

    data = api.prettifyUserTrades(user_id)
    print(data[0])