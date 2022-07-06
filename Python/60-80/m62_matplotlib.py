import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def separador():
    print("")
    print("-" * 80)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("")


def proceso():
    separador()
    x = np.linspace(1, 150, 200)
    y = x + x**2
    print(f"Datos eje x :\n{x}")
    print(f"Datos eje y :\n{y}")

    plt.plot(x,y, 'blue')
    plt.title("My graphics")
    plt.xlabel("X Values ")
    plt.ylabel("Y Values ")
    plt.show()
    plt.subplot(1,2,1)
    plt.plot(x,y,'g')
    plt.subplot(1,2,2)
    plt.plot(x,y,'red')
    plt.show()
  

proceso()
