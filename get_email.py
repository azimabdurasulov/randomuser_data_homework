import email
import get_data
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    sum = []
    for email in data["results"]:
        sum += [email["email"]]
    return sum