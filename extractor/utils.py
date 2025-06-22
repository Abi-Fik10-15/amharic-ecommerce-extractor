import re

def is_amharic(text):
    return bool(re.search(r"[\u1200-\u137F]+", text))