def distance(strand1, strand2):
    if len(strand1) == len(strand2):
        dist = [nucleo for nucleo in range(len(strand1)) if strand1[nucleo] != strand2[nucleo]]
        dist = len(dist)
        return dist
    else:
        raise ValueError
