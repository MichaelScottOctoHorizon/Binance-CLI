#This file is responsible for connecting to the Binance Testnet

import sys
import sub_programs.helpers as helper
from binance.client import Client
from datetime import datetime

#The data was giving an error because it was trying to print data with unicode values - This fixed it
sys.stdout.reconfigure(encoding='utf-8')

api_key = "MCOMzP329zq7TwYFzy71N9VDsRxh4Jp82lMuUgMPlI9gIXkm6ORLmIoUJ40Tqb8t"
api_secret = "7NWmQaxgKBSxjY5uBSmBXTVChUBpsx8svuymJc9ziWyAd2HRnj9z9FrviwkP4pUt"


def get_client():
    client = Client(api_key, api_secret)

    return client

def get_server_time():
    client = get_client()

    server_time = client.get_server_time()["serverTime"]
    server_datetime = datetime.fromtimestamp(server_time / 1000)

    data = [
        f"Timestamp: {server_time}",
        f"Date: {server_datetime.date()}",
        f"Time: {server_datetime.time()}"
    ]

    helper.box_items(data, "Server Date and Time")