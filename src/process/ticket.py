from process import process_assets, process_price, process_dividend, \
    process_profit_last_12months, process_pvp, process_roe
import infra.b3api as b3api
from ticker_gamefication import create_ticker_gamefication


def process_ticket(ticker_name):
    """
    Process the ticker information and calculate a score based on certain criteria.

    Args:
        ticker_name (str): The ticker name of the company.

    Returns:
        Dict: A dictionary containing the ticker name, score, and reason for the score.

    Raises:
        None
    """

    ticker_gamefication = create_ticker_gamefication(ticker_name)
    dividend_data = b3api.get_dividend_ticker(ticker_gamefication['name'])
    process_dividend(ticker_gamefication, dividend_data)

    ticket_data = b3api.get_data_ticker(ticker_name)
    process_price(ticker_gamefication, ticket_data)
    process_roe(ticker_gamefication, ticket_data)
    process_pvp(ticker_gamefication, ticket_data)
    process_assets(ticker_gamefication, ticket_data)
    process_profit_last_12months(ticker_gamefication, ticket_data)

    return ticker_gamefication
