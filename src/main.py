from pathlib import Path
import json

from process.ticket import process_ticket


def load_tickers():
    """
    Loads tickers from the B3 API and processes each ticker.

    This function sends a GET request to the B3 API to retrieve a list of available tickers.
    It then processes each ticker by calling the `process_ticker` function with the ticker's symbol and name.

    Note: This function assumes that the `process_ticker` function is defined elsewhere.

    Returns:
        None
    """

    content = Path('./tickers.json').read_text(encoding='utf-8')
    tickers = json.loads(content)

    for ticker in tickers:
        data = process_ticket(ticker)
        print(data)

if __name__ == '__main__':
    load_tickers()
