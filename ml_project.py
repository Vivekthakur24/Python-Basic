import numbers as np
import pandas as pd
import matplotlib.pyplot as plt
from learn.model_selection import train_test_split # type: ignore
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


df=pd.read_csv("/content/sme_data.csv")
X=df[{}]
y=df[{}]