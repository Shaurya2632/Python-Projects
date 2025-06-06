from numpy import *
from random import *

def b(sampSize=5):
    avg = []

    for i in range(1, sampSize+1):
        data = array([randint(1, 6) for _ in range(5)])
        avg.append(float(data.mean()))

    return float(array(avg).mean())

print(b(3324234))
