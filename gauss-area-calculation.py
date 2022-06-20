import numpy as np


coordinates = np.array([[301.36,116.71],[348.19,125.22],[335.62,139.43],[328.43,134.56],[312.66,103.54]])

coords = np.array([[0,0],[-16.40,16.18],[-22.16,38.17],[0,51.63],[21.04,39.42],[15.95,16.37]])


def area (array):
    ar = []
    array = np.append(array,[array[0]],axis=0)
    array = np.append(array, [array[1]], axis=0)
    for i in range(len(array)-2):
        ar.append((array[i+2][0]-array[i][0])*array[i+1][1])

    return (sum(ar))/2

area(coordinates)
area(coords)