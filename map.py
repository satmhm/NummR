import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

class Angka:
    def __init__(self,Nsim) -> None:
        self.Nsim = Nsim
    
    def Simulation (self):
        daftar = []
        x = range(0,self.Nsim,1)
        for i in range(self.Nsim):
            a = np.random.randint(0,100,1)
            daftar.append(a)
        return(pd.DataFrame(daftar, x))

class date_time:
    def __init__(self, dateColumn) -> None:
        self.dateColumn = dateColumn

percobaan = Angka(Nsim= 100)
print(percobaan.Simulation())


