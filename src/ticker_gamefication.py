import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def create_ticker_gamefication(ticker_name):
    """
    Create a ticker gamefication object.

    Parameters:
    ticker_name (str): The name of the ticker.

    Returns:
    dict: A dictionary representing the ticker gamefication object with the following keys:
        - name (str): The name of the ticker.
        - score (int): The score of the ticker.
        - dividend_value (int): The dividend value of the ticker.
        - reason (str): The reason for the ticker's score.

    """
    return {'name': ticker_name, 'score': 0, 'price': 0, 'dividend_value': 0, 'reason': ''}


def add_reason_and_score(ticker_gamification, reason, score):
    """
    Add reason and sum score to the ticker gamification.

    Args:
        ticker_gamification (dict): The ticker gamification.

    Returns:
        dict: The ticker gamification with reason.

    """
    ticker_gamification['reason'] += f' | {reason}'
    ticker_gamification['score'] += score


def get_value(value):
    """
    Converts a string value to a float, removing any percentage or currency symbols.

    Args:
        value (str): The string value to be converted.

    Returns:
        float: The converted float value.

    """
    if '-' in value:
        return None

    return locale.atof(value.replace('%', '').replace('R$', ''))
