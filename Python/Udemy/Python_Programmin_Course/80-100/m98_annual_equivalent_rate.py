def aer(interest, periods) :
     interest = interest / 100
     tae = ((1+(interest/periods))**periods)-1
     tae = tae * 100
     return tae


if __name__ == '__main__':
     print(round (aer (8, 1), 2))
     print(round (aer (8, 12), 2))
