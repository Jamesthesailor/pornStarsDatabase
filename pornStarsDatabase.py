from __future__ import print_function
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 50000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import lxml.html as LH
from string import ascii_lowercase
import numpy as np

name = []
measurements = []
dateOfBirth = []
hairColor = []
height = []
weight = []

for a in ascii_lowercase:
	url = 'http://www.slutsinc.com/browse-'
	url += (a+ '.php')
	r = requests.get(url)
	root = LH.fromstring(r.content)
	soup = BeautifulSoup(r.text,'html.parser')
	print (url)
		
	table = soup.find_all('table')[2]
	for row in table.find_all('tr')[2:]:
	    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
	    col = row.find_all('td')

	    column_1 = col[0].string
	    name.append(column_1)
	    
	    column_2 = col[4].string
	    measurements.append(column_2)

	    column_3 = col[1].string
	    dateOfBirth.append(column_3)

	    column_4 = col[3].string
	    hairColor.append(column_4)

	    column_5 = col[5].string
	    height.append(column_5)

	    column_6 = col[6].string
	    weight.append(column_6)

df = pd.DataFrame({
	"Name": name,
	"Measurements": measurements,
	"Date of Birth": dateOfBirth,
	"Hair color": hairColor,
	"Height": height,
	"Weight": weight
		})

columnsTitles = ['Name', 'Measurements', 'Date of Birth', 'Hair color', 'Height', 'Weight']
rearrangedDf = df.reindex(columns=columnsTitles)
filename = 'psDatabase.csv'
rearrangedDf.to_csv(filename, index=False, encoding='utf-8')