from ticker_gamefication import add_reason_and_score, get_value


def process_pvp(ticker_gamefication, ticket_data):
    """
    Process the P/VP (Price-to-Value Ratio) for a given ticker.

    Args:
        ticker_gamefication (str): The ticker for the gamefication.
        ticket_data (dict): The data for the ticker.

    Returns:
        None
    """
    pvp = get_value(ticket_data['p_vp'])
    if pvp is None or pvp > 5:
        add_reason_and_score(ticker_gamefication, '**High P/VP**', -2)

    if pvp < 1:
        add_reason_and_score(ticker_gamefication, 'Good P/VP < 1', 1)
