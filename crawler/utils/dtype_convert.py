"""
To convert possible string to other data type
"""


def get_int(text):
    if text.isdigit():
        return int(text)
    return text


def get_float(text):
    try:
        float(text)
        return float(text)
    except ValueError:
        return text
