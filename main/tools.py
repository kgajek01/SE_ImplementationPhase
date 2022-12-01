import datetime

def valid_events(date, phone_number):

    current_date=datetime.datetime.now().date()
    delta = date - current_date

    if delta.days<7:
        return False

    phone = phone_number.split("-")

    if len(phone) != 3:
        return False
    for i, part in enumerate(phone):
        if not part.isnumeric():
            return False
        if not ((i <= 1 and len(part) == 3) or (i == 2 and len(part) == 4)):
            return False

    return True
