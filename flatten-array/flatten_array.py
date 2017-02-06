def flatten(itm):
    flat = []
    for x in itm:
        if isinstance(x, list):
            flat += flatten(x)
        elif isinstance(x, tuple):
            flat += flatten(list(x))
        elif x is not None:
            flat += [x]
    return flat
