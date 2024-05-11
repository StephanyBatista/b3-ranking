from ticker_gamefication import add_reason_and_score, get_value


def process_profit_last_12months(ticker_gamefication, ticket_data):
    """
    Process the profit last 12 months for a given ticker.

    Args:
        ticker_gamefication (str): The ticker gamefication.
        ticket_data (dict): The data for the ticker.

    Returns:
        None
    """
    profit_last_12months = get_value(ticket_data['lucro_liquido_12_meses'])
    if profit_last_12months is None:
        ticker_gamefication['reason'] = 'No protif data'
        return ticker_gamefication

    if profit_last_12months > 1000000000:
        add_reason_and_score(ticker_gamefication, 'High profit last 12 months', 2)

    elif profit_last_12months < 100000000:
        add_reason_and_score(ticker_gamefication, '**Low profit last 12 months**', 0)
