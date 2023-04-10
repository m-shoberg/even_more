#%%
#URL compatible library
import requests
#additional libraries
import os 
from PIL import Image
from IPython.display import IFrame

#request method and base URL
url = 'https://www.ibm.com/'
r = requests.get(url)
#return status of URL request (200) ok
print('Status Code:',r.status_code)
# Header includes key:value pairs for User-Agent, Accept-Encoding, Accept, Connetion, and Cookie
print('Header:',r.request.headers)
print("RequestBody:", r.request.body)
#returns a python dictionary of HTTP response headers.
header = r.headers
print(r.headers)

#print specific key:value pairs from header data
print('Date:',header['Date'])
print('Content-Type:',header['Content-Type'])
print('Encoding:',r.encoding)
print('Body Text Preview:',r.text[:100])

# define URL string
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r = requests.get(url)
print(r.headers)
#retrieve type of content
print('Content Type:',r.headers['Content-Type'])
#before content can be viewd, content must be saved as image variable
path=os.path.join(os.getcwd(),'image.png')
path

#file 'path' is opened in wb -> 'write binary'
with open(path,'wb') as f:
    f.write(r.content)
#display image from url variable
Image.open(path)
# %%
