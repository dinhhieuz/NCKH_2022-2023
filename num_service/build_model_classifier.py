from sklearn.ensemble import GradientBoostingClassifier 

from joblib import dump
import pandas as pd 
import numpy as np 

train_df = pd.read_csv('train.csv')

x = train_df.drop('label', axis = 1).values / 255
y = train_df['label'].values

knn = GradientBoostingClassifier()
knn.fit(x, y)

dump(knn, 'tree_classifier_model.pkl')