import numpy as np
import pandas as pd
import pickle

from sklearn.ensemble import GradientBoostingClassifier

# fetch the data from data/processed
train_data = pd.read_csv('simple_demo_to_use_dvc_pipeline/data/features/train_bow.csv')


X_train = train_data.iloc[:,0:-1].values
y_train = train_data.iloc[:,-1].values

# Define and train the XGBoost model

clf = GradientBoostingClassifier(n_estimators=50)
clf.fit(X_train, y_train)

# save
import os
os.makedirs("simple_demo_to_use_dvc_pipeline/model", exist_ok=True)
pickle.dump(clf, open('simple_demo_to_use_dvc_pipeline/model/model.pkl', 'wb'))

