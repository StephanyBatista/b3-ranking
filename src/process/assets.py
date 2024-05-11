from ticker_gamefication import add_reason_and_score, get_value


def process_assets(ticker_gamefication, ticket_data):
    """
    Process the assets for a given ticker.

    Args:
        ticker_gamefication (str): The ticker gamefication.
        ticket_data (dict): The data for the ticker.

    Returns:
        None
    """
    assets = get_value(ticket_data['ativo'])
    if assets is None:
        ticker_gamefication['reason'] = 'No assets'
        return ticker_gamefication

    if assets > 1000000000000:
        add_reason_and_score(ticker_gamefication, 'High assets +BI', 2)

    elif assets > 10000000000:
        add_reason_and_score(ticker_gamefication, 'High assets', 1)

    if assets < 1000000000:
        add_reason_and_score(ticker_gamefication, 'Low assets', -1)
