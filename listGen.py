import random

def generateRandomIntList(size, min, max):
    return random.sample(range(min, max), size)