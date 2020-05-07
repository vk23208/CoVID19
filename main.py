# -*- coding: utf-8 -*-

from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup
import re

url = ['https://www.worldometers.info/coronavirus/#countries','https://www.worldometers.info/coronavirus/country/india/']
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}

worldata = []
       
for i in url:
    page = requests.get(i, headers = headers)    
    soup = BeautifulSoup(page.content, 'html.parser')
    numbers = soup.find_all( "div" , attrs = { "id" : "maincounter-wrap" })
    for j in numbers:
        a = j.get_text().strip().replace("\n"," ")
        worldata.append(a)
            
worldcases = ''.join(re.findall('\d+', worldata[0:3][0].replace(",","")))
worldeaths = ''.join(re.findall('\d+', worldata[0:3][1].replace(",","")))
worldrecovered = ''.join(re.findall('\d+', worldata[0:3][2].replace(",","")))

indiacases = ''.join(re.findall('\d+', worldata[3:6][0].replace(",","")))
indiadeaths = ''.join(re.findall('\d+', worldata[3:6][1].replace(",","")))
indiarecovered = ''.join(re.findall('\d+', worldata[3:6][2].replace(",","")))

worldcases = int(worldcases)-int(worldeaths)-int(worldrecovered)
indiacases = int(indiacases)- int(indiadeaths)-int(indiarecovered)

#worldfinaldata = str(worldata[0]) + '  ' + str(worldata[1]) +  '  ' + str(worldata[2])
#indiadata = str(worldata[3]) + '  ' + str(worldata[4]) +  '  ' + str(worldata[5])

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', worldcases = worldcases,worldeaths = worldeaths,worldrecovered = worldrecovered,indiacases= indiacases, indiadeaths= indiadeaths,indiarecovered = indiarecovered)
app.run(debug = True) 
