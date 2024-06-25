def groundhog_day(a):
    for d, (previous, current) in enumerate(zip(a, a[1:]), 1):
        res = [d for d, (x, y) in enumerate(zip(previous, current)) if x != y]
        if len(res) > 2:
            return (d,) + tuple(res)
        return (0, 0)


data = ["Groundhog Festival in Punxsutawney.",
        "Groundhog Festival in Punksutawney.",
        "Groundhog Festivel in Punxsutowney."]

print(groundhog_day(data))
