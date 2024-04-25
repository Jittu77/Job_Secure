import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("./DataSetFinal.csv")

x_train = data.drop(columns=['Result', 'Experience','job_description'])
y_train = data['Result']

log_reg_model = LogisticRegression(solver='sag')
log_reg_model.fit(x_train, y_train)
pickle.dump(log_reg_model, open('model1.pkl','wb'))