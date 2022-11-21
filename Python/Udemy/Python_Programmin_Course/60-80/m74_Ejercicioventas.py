from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("m74_datos.csv")
print("Dataframe start")
print(data.head(5))
print("Dataframe end")
print(data.tail(5))

print(data.info())
print(data.columns)
print(data.index)

     
grouped_data = data.groupby('TIENDA').TOTAL.sum()

plt.pie(grouped_data, labels=grouped_data.index)
plt.show()