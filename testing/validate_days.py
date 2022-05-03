def deletetime(days=None):
    if days is None:
        days = 7
        return days
    if days is not None and days not in range(7, 31, 1):
        return days
    else:
        return "good"

time = deletetime()
print(time)