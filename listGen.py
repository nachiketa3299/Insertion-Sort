import random

def generateRandomIntList(size, min_max):
    return [random.randrange(min_max[0], min_max[1]) for _ in range(0, size)] 