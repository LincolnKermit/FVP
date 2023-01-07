import os
import csv
import requests
from bs4 import BeautifulSoup
import re


os.system("cls")
lastname = input("Name : ")
city = input("Ville : ")
link=("https://annuaire.118712.fr/?s=" + lastname +"+"+ city)
requete = requests.get(link)
page = requete.content
soup = BeautifulSoup(page)
os.system("cls")
results = soup.find_all("div", {"class": "item-info"})
n = 1
for blocinfo in results:
  bloc_nom = soup.find(id="result_" + str(n))
  print(bloc_nom["title"])

  results_phone = blocinfo.find_all("span", {"class": "button_wording nomobile"})
  for phone in results_phone:
    print(phone.string)
  results_adress = blocinfo.find_all("span", {"class": "address-content"})
  for adress in results_adress:
    for addr in adress.find_all("span"):
      print(addr.string)
  print("------------------------------------------")
  n = n + 1
if len(results) == 0:
  print("Pas de résultats trouvés")