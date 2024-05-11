from ticker_gamefication import add_reason_and_score, get_value


def process_roe(ticker_gamefication, ticket_data):
    """
    Process the Return on Equity (ROE) for a given ticker.

    Args:
        ticker_gamefication (str): The ticker gamefication.
        ticket_data (dict): The data for the ticker.

    Returns:
        None
    """
    roe = get_value(ticket_data['roe'])
    if roe is None or roe < 15:
        add_reason_and_score(ticker_gamefication, '**Low ROE**', 0)

    elif roe > 50:
        add_reason_and_score(ticker_gamefication, 'Good ROE > 50%', 2)

    elif roe > 35:
        add_reason_and_score(ticker_gamefication, 'Good ROE > 35%', 1)

    elif roe > 20:
        add_reason_and_score(ticker_gamefication, 'Good ROE > 20%', 1)
