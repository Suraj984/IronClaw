import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from collections import OrderedDict

file1 = open('cities.pkl', 'rb')
cities = pickle.load(file1)
file2 = open("world.pkl", "rb")
world = pickle.load(file2)

def sampling(data, size):
    sample_set = pd.DataFrame({"city": list(data.keys())})
    sample_set = sample_set.city.sample(size)
    sample = []
    for city in sample_set:
        sample.append((pd.DataFrame({"time": list(data[city][0].keys())[130:], "temp": list(
            data[city][0].values())[130:]}), data[city][1]))
    return sample


def correlation(sample):
    coeff = OrderedDict()
    for i in sample:
        if i[1] not in coeff:
            coeff[i[1]] = []
        coeff[i[1]].append(i[0]["time"].corr(i[0]["temp"]))
    for j in coeff:
        coeff[j] = np.mean(coeff[j])
    return OrderedDict(sorted(coeff.items()))


def corerelation_plot(data, size):
    sample = sampling(data, size)
    coeff = correlation(sample)
    plt.plot(list(coeff.keys()), list(coeff.values()))
    plt.xlabel('Latitude')
    plt.ylabel('Temperature Correlation')
    plt.title(' Temperature Correlation vs Latitude')
    plt.show()
    plt.figure()


corerelation_plot(cities, 3448)
data = pd.DataFrame({"time": list(world.keys())[130:], "temp": list(world.values())[130:]})
print("The correlation between between global yearly temperatures and time is",data["time"].corr(data["temp"]))