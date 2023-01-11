import requests
from flask import Flask, render_template
import webbrowser
import os
import csv
from bs4 import BeautifulSoup
import re
from colorama import Fore, Back, Style
from colorama import init
import time

#Annuaire de 118712.fr fait par LincolnKermit et Inj3ctor

start = time.time()
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
  print("Nom : " + bloc_nom["title"])
  results_phone = blocinfo.find_all("span", {"class": "button_wording nomobile"})
  for phone in results_phone:
    print("Téléphone : " + phone.string)
  results_adress = blocinfo.find_all("span", {"class": "address-content"})
  for adress in results_adress:
    for addr in adress.find_all("span"):
      adresse_home = addr.string
      print("Adresse : " + addr.string)
      break
  print("------------------------------------------")
  n = n + 1
end = time.time()
elapsed = end - start

print(f'Temps d\'exécution : {elapsed:.2}ms')

@app.route('/')
def index():
  try:
    return render_template("index.html",github=github,street=adresse_home,lastname=bloc_nom["title"],phone=phone.string,error=False)
  except:
    return render_template("index.html",github=github,error=True)



webbrowser.open('http://127.0.0.1:5000')


if __name__ == '__main__':
  print("Statut :" + Fore.GREEN + " OK")
  print(Style.RESET_ALL)
  app.run()

