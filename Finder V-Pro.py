#Made by Lincoln#4504 aka github.com/LincolnKermit
# Version 1.6
from asyncio.windows_events import NULL
from plyer import notification
from operator import index
import time, os, sys, lxml, requests, json
from selenium import webdriver
from urllib.parse import urlencode, urlunparse
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style
init()

version                          ="1.6"
dorks_selected                   =NULL
indexfonction                    ='"'
str(indexfonction)
anwser                           ="y"

os.system("cls")
notification.notify(
    title='Finder V-Pro',
    message="Le pouvoir de l'osint dans vos mains.",
    app_icon=None,
    timeout=10,
)
print("""""
███████╗██╗   ██╗██████╗ 
██╔════╝██║   ██║██╔══██╗
█████╗  ██║   ██║██████╔╝
██╔══╝  ╚██╗ ██╔╝██╔═══╝ 
██║      ╚████╔╝ ██║     
╚═╝       ╚═══╝  ╚═╝     
                                                                                                      
""""")
print(Fore.LIGHTRED_EX + "Bienvenue sur Finder V-Pro!")
print(Fore.WHITE + "https://github.com/LincolnKermit/FVP")
print(Fore.BLUE + "Discord : Lincoln#0666")
print(Fore.MAGENTA + "Version : " + version )
print(Style.RESET_ALL)
time.sleep(1)
print("")
input("Press Enter to launch Finder V-Pro...")
os.system("cls")
print("Launched!")


while anwser =="y":
   time.sleep(1)
   os.system("cls")
   print("1. Nom | 2. Username | 3. Email | 4. Dorks")
   choixversion=input("Choix(1,2,3,4) : ")
   choixname="1"
   choixusername="2"
   choixemail="3"
   choixdorks="4"
   if choixversion==choixname:
      Lastname=input(Fore.MAGENTA + "Nom de famille précis : ")
      City=input(Fore.MAGENTA + "Ville : ")
      print(Style.RESET_ALL)   
      # Performing google search using Python code
      class Gsearch_python:
         def __init__(self,name_search):
            self.name = name_search
         def Gsearch(self):
            count = 0
            try :
               from googlesearch import search
            except ImportError:
               print("No Module named 'google' Found, Please try again")
            for i in search(query=self.name,tld='fr',lang='fr',num=10,stop=3,pause=2):
               count += 1
               print (count)
               print(i + '\n')
      print(Fore.BLUE + "V-Pro " + version + " running on ",sys.version)
      print(Style.RESET_ALL)

      print(Fore.BLUE + "G" + Fore.RED + "o" + Fore.YELLOW + "o" + Fore.BLUE + "g" + Fore.GREEN + "l" + Fore.RED + "e")
      print(Style.RESET_ALL)
      if __name__=='__main__':
         gs = Gsearch_python(indexfonction+Lastname+indexfonction + City)
         gs.Gsearch()

      time.sleep(2)
      print(Fore.CYAN + "Bing")
      print("Non disponible")
      #Code I found on Wiki but im not able to add it due to compatibility and others problems.
      #Using Bing
      #querybing=Lastname + City
      #url = urlunparse(("https", "www.duckduckgo.com", "/", "", urlencode({"q": query}), ""))
      #custom_user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
      #req = Request(url, headers={"User-Agent": custom_user_agent})
      #page = urlopen(req)
      # Further code I've left unmodified
      #soup = BeautifulSoup(page.read())
      #links = soup.findAll("a")
      #for link in links:
      #    print(link["href"])
      print(Style.RESET_ALL)

      time.sleep(2)
      print(Fore.CYAN + "Yahoo")
      print("Non disponible")
      print("")
      time.sleep(2)
      print(Fore.CYAN + "DuckDuckGo")
      print("Non disponible")
      print("")
      print(Style.RESET_ALL)
      input("Appuyez sur une touche pour continuer...")
      os.system("cls")
   if choixversion==choixemail:
      email=input("Email : ")
      os.system("cls")
      print("Email : " + email )
      class Gsearch_python:
         def __init__(self,name_search):
            self.name = name_search
         def Gsearch(self):
            count = 0
            try :
               from googlesearch import search
            except ImportError:
               print("No Module named 'google' Found, Please try again")
            for i in search(query=self.name,tld='fr',lang='fr',num=10,stop=3,pause=2):
               count += 1
               print (count)
               print(i + '\n')
      print(Fore.BLUE + "V-Pro " + version + " running on ",sys.version)
      print(Style.RESET_ALL)

      print(Fore.BLUE + "G" + Fore.RED + "o" + Fore.YELLOW + "o" + Fore.BLUE + "g" + Fore.GREEN + "l" + Fore.RED + "e")
      print(Style.RESET_ALL)
      if __name__=='__main__':
         gs = Gsearch_python(indexfonction+email+indexfonction)
         gs.Gsearch()
      input("Appuyez sur une touche pour continuer...")

   if choixversion==choixusername:
      (Fore.MAGENTA + "Username")
      print(Style.RESET_ALL)
      time.sleep(0.5)
      os.system("cls")
      username=input("username : ")
      response = requests.get('https://github.com/' + username)
      if response.status_code == 200:
         print("User found on Github")
         time.sleep(1)
         print("https://github.com/" + username)
         print("")
      elif response.status_code == 404:
         print("User doesn't seems to exist.")

      response = requests.get('https://www.root-me.org/' + username)
      if response.status_code == 200:
         print("User found on root-me.org")
         time.sleep(1)
         print("https://www.root-me.org/" + username)
         print("")
      elif response.status_code == 404:
         print("User doesn't seems to exist on root-me.org ")
      print("")
      input("Appuyez sur une touche pour continuer...")




   if choixversion==choixdorks:
      (Fore.MAGENTA + "Dorks")
      print(Style.RESET_ALL)
      time.sleep(0.5)
      os.system("cls")
      dorksmodules="”powered by vbulletin” site:.edu"
      dorksmodulesaddons="site:.edu “Numéro de téléphone”"
      print("Liste disponible :")
      print("1. Education | 2. Gouvernemental | 3. Vulnerabilités")
      choixliste=input("Choix des listes (1/2/3): ")
      if choixliste=="1":
         dorks_selected="Education"
      if choixliste=="2":
         dorks_selected="Gouvernemental"
      if choixliste=="3":
         dorks_selected="Vulnérabilités"
      if choixliste=="1":
         dorks_selected="Education"
      if choixliste=="2":
         dorks_selected="Gouvernemental"
      if choixliste=="3":
         dorks_selected="Vulnérabilités"
      if choixdorks=="1":
         print(str(dorks_selected) + " selected")
      if choixdorks=="2":
         print(str(dorks_selected) + " selected")
      if choixdorks=="3":
         print(str(dorks_selected) + " selected")
      if choixdorks=="1":
         print("Grabbing de la liste")
         time.sleep(0.5)
         os.system("cls")
         print("Dorks en cours...")
      print(Fore.BLUE + "V-Pro " + version + " running on ",sys.version)
      print(Style.RESET_ALL)
      print(Fore.BLUE + "G" + Fore.RED + "o" + Fore.YELLOW + "o" + Fore.BLUE + "g" + Fore.GREEN + "l" + Fore.RED + "e")
      print(Style.RESET_ALL)
      class Gsearch_python:
         def __init__(self,name_search):
            self.name = name_search
         def Gsearch(self):
            count = 0
            try :
               from googlesearch import search
            except ImportError:
               print("No Module named 'google' Found, Please try again")
            for i in search(query=self.name,tld='fr',lang='fr',num=10,stop=5,pause=2):
               count += 1
               print (count)
               print(i + '\n')
      print("Dorks #1")
      print("")
      print("")
      if __name__=='__main__':
         gs = Gsearch_python(dorksmodules)
         gs.Gsearch()
      time.sleep(1)
      print("")
      print("")
      print("Dorks #2")
      time.sleep(1)
      if __name__=='__main__':
         gs = Gsearch_python(dorksmodulesaddons)
         gs.Gsearch()      
      input("Appuyez sur une touche pour continuer...")

   else:
      ("Mauvaise saisie")
