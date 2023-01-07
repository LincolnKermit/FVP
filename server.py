import requests
from flask import Flask, render_template
import webbrowser
import os
import csv
from bs4 import BeautifulSoup
import re

#Annuaire de 118712.fr fait par LincolnKermit et Inj3ctor


blank = " "
github = "https://github.com/LincolnKermit/FVP"
app = Flask(__name__, static_folder='static')

os.system("cls")
lastname = input("Nom : ")
city = input("Ville : ")
link=("https://annuaire.118712.fr/?s=" + lastname +"+"+ city)
requete = requests.get(link)
page = requete.content
soup = BeautifulSoup(page)
os.system("cls")
results = soup.find_all("div", {"class": "item-info"})
n = 1
adresse_home = ""
for blocinfo in results:
  bloc_nom = soup.find(id="result_" + str(n))
  print(bloc_nom["title"])
  results_phone = blocinfo.find_all("span", {"class": "button_wording nomobile"})
  for phone in results_phone:
    print(phone.string)
  results_adress = blocinfo.find_all("span", {"class": "address-content"})
  for adress in results_adress:
    for addr in adress.find_all("span"):
      adresse_home = addr.string
      break
  print("------------------------------------------")
  n = n + 1

@app.route('/')
def index():
  try:
    return render_template("index.html",github=github,street=adresse_home,lastname=bloc_nom["title"],phone=phone.string,error=False)
  except:
    return render_template("index.html",error=True)

webbrowser.open('http://127.0.0.1:5000')

if __name__ == '__main__':
  app.run()

