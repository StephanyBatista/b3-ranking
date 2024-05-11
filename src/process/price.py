from ticker_gamefication import add_reason_and_score, get_value


def process_price(ticker_gamefication, ticket_data):
    """
    Process the price of a stock and update the ticker_gamefication dictionary with relevant information.

    Args:
        ticker_gamefication (dict): The dictionary containing gamefication data for a stock ticker.
        ticket_data (dict): The dictionary containing data for a stock ticker.

    Returns:
        dict: The updated ticker_gamefication dictionary.

    """
    if ticket_data is None:
        add_reason_and_score(ticker_gamefication, 'No data', 0)
        return ticker_gamefication

    value = get_value(ticket_data['cotacao'])
    ticker_gamefication['price'] = value
    dy_value = get_value(ticker_gamefication['dividend_value'])
    price_max = dy_value/0.06
    if(value > price_max):
        add_reason_and_score(ticker_gamefication, '**Price is too high**', -1)

    good_price = price_max - (price_max * 0.40)
    if good_price >= value:
        add_reason_and_score(ticker_gamefication, 'Price very cheap', 2)
