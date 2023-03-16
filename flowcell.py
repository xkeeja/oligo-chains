import numpy as np


def oligo(fc):
    count = 0
    for i in range(1, len(fc)-1):
        for j in range(1, len(fc[0])-1):
            c = fc[i,j]
            d = np.array([max(i) for i in [fc[:i,j], fc[i+1:,j], fc[i,:j], fc[i,j+1:]]])
            if all(c <= d):
                count += 1
    return count



flowcell = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0]
]


print(oligo(np.array(flowcell)))
