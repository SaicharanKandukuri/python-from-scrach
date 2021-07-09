import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("LSM1.csv")

x = df.iloc[:,0].values
y = df.iloc[:,1].values

