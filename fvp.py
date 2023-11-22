from googlesearch import search
from flask import Flask, render_template, request
from colorama import Fore, Back, Style, init
import time, os, requests
from bs4 import BeautifulSoup
from selenium import webdriver
init()
start = time.time()
blank = " "
github = "https://github.com/LincolnKermit/FVP"
app = Flask(__name__, static_folder='static')
keywordfr                        ="fr"
version                          ="3.5 (Public Build)"
indexfonction                    ='"'
anwser                           ="y"
str(indexfonction)
messageapi                       ="Fix de l'API sur 118712.fr"



def clear():
   if os.name == 'nt':
      os.system("cls")
   else:
      os.system("clear")

def username_finder():
   (Fore.MAGENTA + "Username")
   print(Style.RESET_ALL)
   username=input("username : ")
   response = requests.get('https://root-me.org/' + username)
   if response.status_code == 200:
      print("User found on Root-Me")
      print("https://root-me.org/" + username + "\n")
   elif response.status_code == 404:
      print("User doesn't seems to exist on Root-Me")


   response = requests.get('https://github.com/' + username)
   if response.status_code == 200:
      print("User found on Github")
      print("https://github.com/" + username + "\n")
   elif response.status_code == 404:
      print("User doesn't seems to exist on Github")
   input("...")
   
def namefinder_api():
   # not fonctionnal 118712.fr added antibot JS protection.
   # Help me by pull requests if you know solutions ( which excludes headless browser )
   lastname = input("Last name : ")
   city = input("City : ")
   url = ("https://www.118712.fr/recherche/auto/"+city+"/"+lastname)
   print(url)
   response = requests.get(url)
   html_content = response.content

   # Charger le contenu HTML avec BeautifulSoup
   soup = BeautifulSoup(html_content, 'html.parser')
   print(soup)

   # Trouver l'élément <a> avec l'ID "tel_7_ab_test"
   telephone_element = soup.find('a', {'id': 'tel_7_ab_test'})

   if telephone_element:
      # Accéder à la balise <span> pour obtenir le numéro de téléphone
      numero_telephone = telephone_element.find('span', {'class': 'value'}).text.strip()
      print("Numéro de téléphone trouvé :", numero_telephone)
   else:
      print("Élément non trouvé")


def googlesearch_api():
   try:
      from googlesearch import search
   except ImportError: 
      print("No module named 'google' found")
   
   query = input("Name to search : ")
   
   for result in search(query, tld="fr", num=10, stop=10, pause=2):
      print(result + "\n")


clear()
print("""
███████╗██╗   ██╗██████╗ 
██╔════╝██║   ██║██╔══██╗
█████╗  ██║   ██║██████╔╝
██╔══╝  ╚██╗ ██╔╝██╔═══╝ 
██║      ╚████╔╝ ██║     
╚═╝       ╚═══╝  ╚═╝     
                                                                                                      
""""")
print(Fore.LIGHTRED_EX + "Bienvenue sur Finder V-Pro Enhanced!")
print(Fore.WHITE + "https://github.com/LincolnKermit/FVP")
print(Fore.BLUE + "Discord : Lincoln#????")
print(Fore.MAGENTA + "Version : " + version )
print(Fore.LIGHTRED_EX + "Message des developpeurs : " + messageapi)
print(Style.RESET_ALL)
print("")
input("Press Enter to launch Finder V-Pro...")
clear()
print("Launched!")

print("1. Google Search \n 2. Name Finder \n 3. Phone searcher")
choix = input(Fore.MAGENTA + "Choix de valeur?")

if choix == "1":
   googlesearch_api()
if choix == "2":
   username_finder()
if choix == "3":
   namefinder_api()