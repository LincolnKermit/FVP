max_num = 10
import time
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

try:
    from googlesearch import search
    from flask import Flask, render_template, request
    from colorama import Fore, Back, Style, init
except ImportError as e:
    print(f"Error importing module: {e}")
    print("Please install the required modules using:\n pip install -r requirements.txt")



options = FirefoxOptions()
options.add_argument("--headless")
try:
    driver = webdriver.Firefox(options=options)
except WebDriverException as e:
    print("Driver webdriver.Firefox not found. Please make sure you have Firefox installed.")
    driver_path = input("Enter the path to the Firefox driver (geckodriver): ")
    try:
        driver = webdriver.Firefox(executable_path=driver_path, options=options)
        print("Firefox driver initialized successfully using the provided path.")
    except WebDriverException as e:
        print("Error initializing Firefox driver with the provided path. Error:", e)

init()
start = time.time()
blank = " "
github = "https://github.com/LincolnKermit/FVP"
app = Flask(__name__, static_folder='static')
keywordfr                        ="fr"
version                          ="3.6 (Public Build)"
indexfonction                    ='"'
anwser                           ="y"
str(indexfonction)
messageapi                       ="Fix de l'API sur 118712.fr + Fix des bugs sur le driver firefox ( windows plateform )"



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
    lastname = input("Last name: ")
    city = input("City: ")
    # Assuming you have initialized your webdriver (driver) before calling this function
    # driver = webdriver.Chrome()  # Example: Initializing a Chrome webdriver

    driver.get(f"https://www.118712.fr/recherche/auto/{city}/{lastname}")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('article')  # Trouver tous les éléments 'article'
    clear()
    if not articles:
        print("No articles found for the given search criteria.")
        return

    for article in articles:
        address_element = article.find('address', class_='bi_adress txt_md')

        if address_element:
            address_elements = address_element.find_all('p')
            telephone_element = article.find('a', class_='button primary ab_test')
            name_element = article.find('h2', class_='h4')

            if telephone_element and name_element:
                address = ' '.join([line.get_text(strip=True) for line in address_elements])
                numero_telephone = telephone_element.find('span', {'class': 'value'}).text.strip()
                full_name = name_element.text.strip()
                print("\n")
                article_id = article.get('id', 'No ID found')
                print(f"Details for {article_id}:")
                print(f"Full Name: {full_name}")
                print(f"Phone number: {numero_telephone}")
                print(f"Address: {address}")
                print("\n")
            else:
                print(f"No details found for this article.")
                print("\n")



def googlesearch_api():

   try:
      from googlesearch import search
   except ImportError: 
      print("No module named 'google' found")
   
   query = input("Name to search : ")
   
   for result in search(query, num=10, stop=10, pause=2):
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

print("1. Google Search \n 2. Username Finder \n 3. Name searcher")
choix = input(Fore.MAGENTA + "Choix de valeur : ")

if choix == "1":
   clear()
   googlesearch_api()
if choix == "2":
   clear()
   username_finder()
if choix == "3":
   clear()
   namefinder_api()



