Database = []


class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password


def wrong_register(email, password):
    # executes the check in this function
    if not str(email).__contains__("@"):
        raise ValueError("Email is not an email!")
    user = User(email, password)
    Database.append(user)


def good_register(email, password):
    # executes the check in a different function
    if not validate_email(email):
        raise ValueError("Email is not an email!")
    user = User(email, password)
    Database.append(user)


def validate_email(email):
    return str(email).__contains__("@")
