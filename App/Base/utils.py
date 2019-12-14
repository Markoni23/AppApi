from random import sample

def random_api():
    s = "something for API"
    return ''.join(sample(s,10))