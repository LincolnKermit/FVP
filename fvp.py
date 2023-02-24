# Made by Lincoln#???? aka github.com/LincolnKermit
# Version 3.3
# Should I make a website? send feedback by star!
# I tried to contact Epieos for their API but no one responded.
# Number Lookup soon


from flask import Flask, render_template
from asyncio.windows_events import NULL
import cmd
import re
import csv
import requests
from plyer import notification
from operator import index
import time, os, sys, lxml, requests, json
from selenium import webdriver
import urllib.request
from urllib.parse import urlencode, urlunparse
from bs4 import BeautifulSoup
from colorama import init
import webbrowser
from colorama import Fore, Back, Style
init()

start = time.time()
blank = " "
github = "https://github.com/LincolnKermit/FVP"
app = Flask(__name__, static_folder='static')
keywordfr                        ="fr"
version                          ="3.4.1"
dorks_selected                   =NULL
indexfonction                    ='"'
anwser                           ="y"
str(indexfonction)
messageapi                       ="Ajout du bouton erase sur l'affichage web!"
count = 0

os.system("cls")
notification.notify(
    title='Finder V-Pro',
    message="Le pouvoir de l'osint dans vos mains.",
    app_icon=None,
    timeout=10,
)
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
os.system("cls")
print("Launched!")


while anwser =="y":
   os.system("cls")
   print("1. Nom | 2. Username | 3. Email | 4. Numéro de télephone | 5. Discord | 6. Quitter")
   choixversion=input("Choix(1-6) : ")
   choixname="1"
   choixusername="2"
   choixemail="3"
   choixphone = "4"
   choixdiscord = "5"
   choixquitter = "6"  
   if choixversion==choixquitter:
      print("Merci d'avoir utilisé Finder V-Pro!")
      time.sleep(2)
      sys.exit()
   if choixversion==choixdiscord:
      id = input(Fore.MAGENTA + "ID Discord : ")
      req = requests.get('https://api.leaked.wiki/discorduser?id=' + id)
      data = req.json()
      print(Style.RESET_ALL)

      print(Fore.RED + "Nom d'utilisateur : " + data['username'] + "#" + data['discriminator'])
      time.sleep(0.5)
      print("Url du Profil : " + data['avatar'])
      time.sleep(0.5)
      print("Url Bannière : " + str(data['banner']))
      time.sleep(1)
      print("Les infos apparaitrons dans la console pendant 30 secondes.")
      time.sleep(30)
      print(Style.RESET_ALL)
      

   if choixversion==choixname:
      Lastname=input(Fore.MAGENTA + "Nom de famille précis : ")
      City=input(Fore.MAGENTA + "Code Postal : ")
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
         time.sleep(3)
      link=("https://annuaire.118712.fr/?s=" + Lastname +"+"+ City)
      requete = requests.get(link)
      page = requete.content
      soup = BeautifulSoup(page)
      
      print(Fore.BLUE + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print("Recherche dans l'annuaire 118712.fr")
      print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print(Style.RESET_ALL)
      time.sleep(3)
      results = soup.find_all("div", {"class": "item-info"})
      n = 1
      adresse_home = ""
      Telephones=[]
      Adresses=[]
      for blocinfo in results:
         bloc_nom1 = soup.find(id="result_1")
         bloc_nom2 = soup.find(id="result_2")
         bloc_nom = soup.find(id="result_" + str(n))
         print("Nom : " + bloc_nom["title"])

         results_phone = blocinfo.find_all("span", {"class": "button_wording nomobile"})
         for phone in results_phone:
            print("Téléphone : " + phone.string)
            Telephones.append(phone.string)
            phone1 = phone.string
         results_adress = blocinfo.find_all("span", {"class": "address-content"})
         for adress in results_adress:
            for addr in adress.find_all("span"):
               adresse_home = addr.string
               print("Adresse : " + addr.string)
               Adresses.append(addr.string)
               break
            

         print("------------------------------------------")
         n = n + 1
      end = time.time()
 

      #Nb_tel=len(Telephones)
      #tel1 = Telephones[0]
      #if Nb_tel > 1:
         #tel2 = Telephones[1]

      Nb_adresse=len(Adresses)
      adresses1 = Adresses[0]
      if Nb_adresse > 1:
         adresses2 = Adresses[1]   
      


      elapsed = end - start
      print(f'Temps d\'exécution : {elapsed:.2}ms')
      print("Ouverture de l'interface web")

      @app.route('/')



      def index():
         try:
            n = 2
            return render_template("index.html",github=github,street=adresses1,lastname=bloc_nom1["title"],phone="None",error=False)
         except:
            return render_template("index.html",github=github,error=True)
      
      
      @app.route('/eraseit/')


      def eraseit():
         try:
            return render_template("index.html",github=github,street=adresses2,lastname=bloc_nom2["title"],phone='None',error=False)
         except:
            return render_template("index.html",github=github,error=True)




      webbrowser.open('http://127.0.0.1:5000')
      if __name__ == '__main__':
         print("Statut :" + Fore.GREEN + " OK")
         print(Style.RESET_ALL)
         app.run()



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
      input("Appuyez sur entrer pour continuer...")
      os.system("cls")
   if choixversion==choixphone:
    num = input("Entrez le numero de télephone : ")
    url = 'http://annuaire.freebox.fr/annuaire/?tel=' + num +'&submit_inv=Rechercher'
    page = urllib.request.urlopen(url, timeout=20)
    soup = BeautifulSoup(page,features="html.parser")
    tel = soup.find_all('div', {'class': 'tel'}) #va chercher la classe tel dans le site de l'annuaire free
    telephone=[]
    for e in tel:
        e=e.text #prend le bout du code html avec le num
        telephone.append(e)
        e = e.replace('\n', '')
        res = [str(sub.split('\n')[1]) for sub in telephone]#convertion pip
        StrNum = "".join(res)#convertie en str
        print("Numero de telephone :" + str(StrNum).lstrip())#affiche et supprime les espaces de devant dans la liste
    #PS:la tout est ok pas de verif
    nom = soup.find_all('span',{'class': 'bold'})
    NomDeFamille = []
    for x in nom:
        x = x.text
        NomDeFamille.append(x)
        x = x.replace('[<span class="bold">', '   </span>, <span class="bold">Free, la société</span>, <span class="bold">Free recrute</span>, <span class="bold">Nous contact')#choisi entre les espace la valeur
        res1 = [str(sub.split('\n')[1]) for sub in NomDeFamille]#convertion pour extraire les str
        res2 = [str(sub.split('\n')[2]) for sub in NomDeFamille]
        StrNomdeFamille = "".join(NomDeFamille)#convertis les str trouvé
        NomDeFamille_final = str(StrNomdeFamille).strip()
        
        break
    adress = soup.find('div',{'class': 'rue'})
    List_adress = []
    adress_text = adress.text
    List_adress.append(adress_text)
    adress = adress_text.replace('<div class="rue"> ', ' </div>')
    adress_final = str(adress).strip()


    city = soup.find('div',{'class': 'ville'})
    List_city = []
    city_text = city.text
    List_city.append(city_text)
    city = city_text.replace('<div class="rue"> ', ' </div>')
    postal_code = re.sub(r'[^\d]+', '', city) 
    city = re.sub(r'[^\D]+', '', city) 
    postal_code_final = str(postal_code).strip()
    city_final = str(city).strip()
    print(Fore.BLUE + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Recherche dans l'annuaire free.fr")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(Style.RESET_ALL)
    print("Ouverture de l'interface web")

    @app.route('/')



    def index():
       try:
          n = 2
          return render_template("index.html",github=github,street=postal_code_final + " " + city_final + ",\n" + adress_final,lastname=NomDeFamille_final,phone=num,error=False)
       except:
          return render_template("index.html",github=github,error=True)
      
      
    @app.route('/eraseit/')


    def eraseit():
       try:
          return render_template("index.html",github=github,street=adresses2,lastname=bloc_nom2["title"],phone='None',error=False)
       except:
          return render_template("index.html",github=github,error=True)




    webbrowser.open('http://127.0.0.1:5000')
    if __name__ == '__main__':
       print("Statut :" + Fore.GREEN + " OK")
       print(Style.RESET_ALL)
       app.run()




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
      input("Appuyez sur entrer pour continuer...")

   if choixversion==choixusername:
      (Fore.MAGENTA + "Username")
      print(Style.RESET_ALL)
      time.sleep(0.5)
      os.system("cls")
      username=input("username : ")
      os.system("cls")
      response = requests.get('https://root-me.org/' + username)
      if response.status_code == 200:
         print("User found on Root-Me")
         print("https://root-me.org/" + username)
         print("")
      elif response.status_code == 404:
         print("User doesn't seems to exist on Root-Me")

      response = requests.get('https://tiktok.com/@' + username)
      if response.status_code == 200:
         print("User found on TikTok")
         print("https://tiktok.com/@" + username)
         print("")
      else:
         print("User doesn't seems to exist on TikTok")


      response = requests.get('https://github.com/' + username)
      if response.status_code == 200:
         print("User found on Github")
         time.sleep(1)
         print("https://github.com/" + username)
         print("")
      elif response.status_code == 404:
         print("User doesn't seems to exist on Github")
      print("")
      input("Appuyez sur entrer pour continuer...")
   else:
      ("Mauvaise saisie")
