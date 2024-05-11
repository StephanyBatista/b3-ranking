import time
import requests


def get_all_tickers():
    """
    Get all tickers from the API and process them.

    Returns:
        None
    """

    time.sleep(1)
    response = requests.get('https://b3api.me/api/fundamentus/available', timeout=10)
    if response.ok is False:
        print('Erro ao carregar tickers')
   
    tickers = response.json()

    return tickers


def get_dividend_ticker(ticker_name):
    """
    Get dividend from api.

    Args:
        ticker_name (str): The ticker name of the company.

    Returns:
        None
    """

    time.sleep(1)
    response = requests.get(
        f'https://b3api.me/api/fundamentus/dividend?ticket={ticker_name}', timeout=10)
    if response.ok is False:
        return

    ticker = response.json()
    if ticker.get('error'):
        return None

    return ticker


def get_data_ticker(ticker_name):
    """
    Get data from the API

    Args:
        ticker_name (str): The ticker name of the company.

    Returns:
        None
    """

    time.sleep(1)
    response = requests.get(f'https://b3api.me/api/fundamentus/{ticker_name}', timeout=10)
    if response.ok is False:
        return
    
    return response.json()

    