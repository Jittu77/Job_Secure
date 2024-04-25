import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("./DataSetFinal.csv")

x_train = data.drop(columns=['Result', 'Experience','job_description'])
y_train = data['Result']
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)


model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train_scaled.shape[1]))
model.add(Dropout(0.2))
model.add(Dense(units=32, activation='relu'))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=2, activation='sigmoid'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train, epochs=25, batch_size=32, validation_split=0.1)
# pickle.dump(model, open('model3.pkl','wb'))
model.save('model3.h5')