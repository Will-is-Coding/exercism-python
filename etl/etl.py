def transform(old):
    return {key.lower(): item[0] for item in old.items() for key in list(item[1])}
