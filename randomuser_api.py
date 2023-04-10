#%%
import randomuser
import requests
import numpy as np
import os 
from PIL import Image
from IPython.display import IFrame

#request method and base URL
url = 'https://randomuser.me/api/?results=5&inc=name'
r = requests.get(url)
# Create a generator object with the number of users to generate
print(r.text)
clean_data = ["name"
              "title"
              "first"
              "last"
              ]
r.drop(clean_data, inplace=True, axis=1)
# %%
