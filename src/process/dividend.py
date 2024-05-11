from ticker_gamefication import add_reason_and_score, get_value


def process_dividend(ticker_gamefication, dividend_data):
    """
    Process dividend data for a given ticker.

    Args:
        ticker_gamefication (dict): A dictionary containing ticker gamefication data.
        dividend_data (dict): A dictionary containing dividend data.

    Returns:
        dict: The updated ticker gamefication dictionary.

    """
    if dividend_data is None:
        ticker_gamefication['reason'] = 'No dividend data'
        return ticker_gamefication

    porcentage = get_value(dividend_data['dividendYield']['porcentage'])
    if porcentage is None or porcentage < 6:
        ticker_gamefication['reason'] = 'Low dividend yield'
        return ticker_gamefication

    ticker_gamefication['dividend_value'] = dividend_data['dividendYield']['value12month']

    if porcentage > 10:
        add_reason_and_score(ticker_gamefication, 'High DY > 10%', 2)

    elif porcentage > 8:
        add_reason_and_score(ticker_gamefication, 'Good DY > 8%', 1)

    else:
        add_reason_and_score(ticker_gamefication, 'Good DY > 6%', 1)
