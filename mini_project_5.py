import statistics

def squares(*args):
    mean = statistics.mean(args)
    for value in args:
        yield (value - mean) ** 2


for result in squares(3, 4, 5):
    print(result)