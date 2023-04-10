#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#a = np.array([1,2,3,4,5,6])
#print(type(a))
#print(a.dtype)
#print(a.size)

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)


# %%
