import urllib.request
import time
import json
import random

'''client'''
'''code'''

QUERY = "http://localhost:8080/query?id={}"


N = 500


def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    """ Also create some unit tests for this function in client_test.py """
    if(price_b == 0):
        return
    return price_a/price_b


if __name__ == "__main__":
    # price every n seconds
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(
            QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" %
                  (stock, bid_price, ask_price, price))

        print("Ratio %s" % getRatio(prices['ABC'], prices['DEF']))
