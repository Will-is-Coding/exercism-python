def slices(toSlice, length):
    toSlice = list(map(int, toSlice))
    if length and len(toSlice) >= length:
        return [
            toSlice[i: i + length]
            for i in range(len(toSlice))
            if i + length <= len(toSlice)
        ]
    else:
        raise ValueError
