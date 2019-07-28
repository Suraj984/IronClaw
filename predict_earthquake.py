import numpy as np
import pandas as pd
from subprocess import check_output
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from sklearn.model_selection import train_test_split
import time
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from numpy import newaxis
from geopy.geocoders import Nominatim

#matplotlib inline
import warnings
warnings.filterwarnings('ignore')
#%config InlineBackend.figure_format = 'retina'

from subprocess import check_output
#print(check_output(["ls", "../input"]).decode("utf8"))


eq_dataset = pd.read_csv("database.csv.txt", header=0)
#print(eq_dataset.head())

#print(len(eq_dataset[["Latitude","Longitude","Magnitude"]]))
#print(eq_dataset[["Latitude","Longitude","Magnitude"]][1:2])

final_dataset = eq_dataset[['Latitude', 'Longitude', 'Magnitude']]
#print(np.array(final_dataset[0:1]))

train_size = int(len(final_dataset) * 0.80)
test_size = len(final_dataset) - train_size
train, test = final_dataset[0:train_size], final_dataset[train_size:len(final_dataset)]
#print(len(train), len(test))


### To convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []

	for i in range(len(dataset) - look_back - 1):
		a = dataset[i:(i+look_back)]
		dataX.append(np.array(a))
		dataY.append(np.array(dataset[i + look_back:i+look_back+1]))

	return np.array(dataX), np.array(dataY)


look_back = 50
trainX, trainY = create_dataset(train, look_back)

#print(trainX.shape)
#print(trainY.shape)


### To build the model
model = Sequential()
model.reset_states()

model.add(LSTM(
    input_dim=3,
    output_dim=100,
    return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(
    100,
    return_sequences=True))
model.add(Dropout(0.2))

model.add(Dense(
    output_dim=3))
model.add(Activation('linear'))

start = time.time()
model.compile(loss='mse', optimizer='adam')
#print ('compilation time : ', time.time() - start)

model.fit(
    trainX,
    trainY,
    batch_size=500,
    nb_epoch=1,
    validation_split=0.05)

test.shape
testX, testY = create_dataset(test, look_back)

test1 = np.array(testX[0:1])
#print(test1[0:1][0:1])

#print(model.predict(test1))
print(test1)