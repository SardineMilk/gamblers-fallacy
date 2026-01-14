import requests
import os
import json



class Market:
    """
    A class describing a single Market    
    """
    # TODO - complete class


class Trade:
    """
    A class describing a single Trade made by a user
    (contains all data from a trade returned by prettifyUserTrades)
    """



def getUserTrades(user_id):
    # TODO - write docstrings in this style (Google Style Docstrings) for every function
    """
    Get the raw trade data for a single user
    
    Args:
        user_id (string): id of the user to get data for. NOT the name
    
    Returns:
        string: raw text data of user trades
    """
    try:
        response = requests.get(f"https://data-api.polymarket.com/trades?user={user_id}")
    except:
        print(f"Error: Failed getting data for user {user_id} with unknown error")

    if response.status_code != 200:
        print(f"Error: Failed getting data for user {user_id} with error code {response.status_code}")
        raise

    data = response.text
    return data


def saveUserTrades(user_id, data):
    """
    TODO - write docstring
    """
    # TODO - write this using control flow (if statements), not except
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


# TODO - do this in a smarter way
all_parameters = ["proxyWallet", "side", "asset", "conditionId", "size", "price", "timestamp", "title", "slug", "icon", "eventSlug", "outcome", "outcomeIndex", "name", "pseudonym", "bio", "profileImage", "profileImageOptimized", "transactionHash"]
desired_parameters = ["proxyWallet", "side", "asset", "conditionId", "size", "price", "timestamp", "title", "slug", "eventSlug", "outcome", "outcomeIndex", "transactionHash"]
def prettifyUserTrades(user_id):
    """
    TODO - write docstring
    """
    # Load raw data
    try:
        with open(f"raw_users/{user_id}.txt") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Data for user {user_id} not found")

    data = json.loads(data)

    # Generate a list containing desired parameters of each trade
    trades = []
    for trade in data:
        pretty_trade = []
        for parameter in trade:
            if parameter in desired_parameters:
                pretty_trade.append((parameter, trade[parameter]))
        trades.append(pretty_trade)
    return trades


def listMarkets(filters):
    """
    List all markets matching the filters
    
    Args:
        filters (list): A list of filters to use. E.g. active/closed/resolved, minVolume, outcomeCount etc

    Returns:
        list: A list of market IDs matching the filters

    """

    return


def getMarket(marketId):
    """
    Get the market data for a single market ID

    Args:
        marketId (string):  The ID of the market to fetch
    Returns:
        Market: Data for the market
    """

    return


# TODO - come up with a smart system to control which wallet is active 
    # This should be able to use a fake wallet to trade virtual money
def buyYes(marketId, amount, maxPrice):    
    pass

def sellYes(marketId, amount, minPrice):
    pass

def buyNo(marketId, amount, maxPrice):
    pass

def sellNo(marketId, amount, minPrice):
    pass


def getAllPositions():
    return

def getPosition(marketId):
    """
    Get current position for a single market

    Args:
        marketId: The ID of the market to fetch position for
    Return:
        : Number of current shares, outcome of shares, current price of shares
    
    """
    return


def getBalance():
    """
    Fetch the balance of the current wallet

    Returns:
        (int): Balance in cents(?)
    """
    return
