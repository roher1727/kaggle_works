import tensorflow as tf
import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# Leyendo datos
data = pd.read_csv('who-suicide-statistics.csv')

model = keras.Sequential()

model.add(Dense=32,)
