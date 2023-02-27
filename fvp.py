# Made by Lincoln#???? aka github.com/LincolnKermit and Manouzr#???? aka github.com/Manouzr
# Version 3.4.3
# Should I make a website? send feedback by star!
# I tried to contact Epieos for their API but no one responded.

from flask import Flask, render_template
from flask import request
from asyncio.windows_events import NULL
import cmd
import re
import pyperclip
import csv
import requests
import socket
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
version                          ="3.4.2 (Private Build)"
dorks_selected                   =NULL
indexfonction                    ='"'
anwser                           ="y"
str(indexfonction)
messageapi                       ="Yandex Image Searcher available!"
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
   print(" [1] Nom \n [2] Username \n [3] Email \n [4] Numéro de télephone \n [5] Discord \n [6] Check Mail \n [7] GeoIP\n [8] Yandex Images Searcher \n [9] Tools\n [10] AIO \n[0] Quitter")
   choixversion=input("Choix(1-10) : ")
   choixname="1"
   choixusername="2"
   choixemail="3"
   choixphone = "4"
   choixdiscord = "5"
   choixcheckmail = "6"
   choixgeoip = "7"
   choiximages = "8"
   choixtools = "9"
   choixallinone = "10"
   choixquitter = "0"
   if choixversion==choixallinone:
      os.system("cls")
      print(Fore.LIGHTCYAN_EX + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      print("All In One Search")
      print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
      nom = input(Fore.LIGHTBLACK_EX + "Nom : ")
      prenom = input("Prénom : ")
      username = input("Username : ")
      email = input("Email : ")
      phone = input("Numéro de télephone : ")
      discord = input("Discord ID : ")
      if nom == "":
         print("Nom : " + Fore.RED + "Recherche du nom ignoré!" + Style.RESET_ALL)
      if prenom == "":
         print("Prénom : " + Fore.RED + "Recherche du prénom ignoré!" + Style.RESET_ALL)
      if username == "":
         print("Username : " + Fore.RED + "Recherche du username ignoré!" + Style.RESET_ALL)
      if email == "":
         print("Email : " + Fore.RED + "Recherche de l'email ignoré!" + Style.RESET_ALL)
      if phone == "":
         print("Numéro de télephone : " + Fore.RED + "Recherche du numéro de télephone ignoré!" + Style.RESET_ALL)
      if discord == "":
         print("Discord ID : " + Fore.RED + "Recherche du discord ID ignoré!" + Style.RESET_ALL)
      print(Fore.LIGHTCYAN_EX + "++++++++++++++++++++++++++Recherche en cours...++++++++++++++++++++++++++++")
      req = requests.get('https://api.leaked.wiki/discorduser?id=' + id)
      data = req.json()
      print(Style.RESET_ALL)
      discord_user ="Nom d'utilisateur : " + data['username'] + "#" + data['discriminator']
      print(Fore.RED + discord_user)
      time.sleep(0.5)
      discord_profile =  data['avatar']
      
      print("Url du Profil : " + data['avatar'])
      time.sleep(0.5)
      print("Url Bannière : " + str(data['banner']))
      print(Style.RESET_ALL)
      if data['banner'] == None:
         print(Fore.RED + "Pas de bannière")
         banner = "Pas de bannière ❌"
      print(Style.RESET_ALL)
      print("Ouverture de l'interface web")
      time.sleep(0.5)
      @app.route('/discord/')
      def index():
         try:
            n = 2
            return render_template("discord.html",github=github,discord_user=discord_user,profile_img=data['avatar'],banner=banner,error=False)
         except:
            return render_template("discord.html",github=github,error=True)
      
      
      @app.route('/eraseit/')


      def eraseit():
         try:
            return render_template("index.html",github=github,discord_user=discord_user,profile_img=data['avatar'],banner=str(data['banner']),error=False)
         except:
            return render_template("index.html",github=github,error=True)
         


      webbrowser.open('http://127.0.0.1:5000')
      if __name__ == '__main__':
         print("Statut :" + Fore.GREEN + " OK")
         print(Style.RESET_ALL)
         app.run()

      
   if choixversion==choixtools:
      os.system("cls")
      print(" [1] Domain 2 IP \n [2] IP 2 Domain \n [3] Partial Discord Token Finder \n [0] Back")
      choixtools=input("Choix(1-4) : ")
      if choixtools=="1":
         os.system("cls")
         print(Fore.LIGHTBLUE_EX + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Domain 2 IP")
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         domain=input(Fore.LIGHTBLACK_EX + "Domain : ")

         print(f"IP de {domain} : " + socket.gethostbyname(domain))
         time.sleep(0.5)       
         pyperclip.copy(socket.gethostbyname(domain) + " : " + domain)
         print("Ip copiée dans le presse-papier!")	
         print(Style.RESET_ALL)
         input("Press Enter to continue...")
         
      if choixtools=="2":
         os.system("cls")
         print(Fore.LIGHTBLUE_EX + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("IP 2 Domain")
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         ip=input(Fore.LIGHTBLACK_EX + "IP : ")
         print("Domain de " + ip + " : " + socket.gethostbyaddr(ip)[0])
         time.sleep(0.5)
         pyperclip.copy(socket.gethostbyaddr(ip)[0] + " : " + ip)
         print("Domain copié dans le presse-papier!")
         print(Style.RESET_ALL)
         
         input("Press Enter to continue...")
      if choixtools=="3":
         os.system('cls')
         print(Fore.LIGHTBLUE_EX + "++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         print("Partial Discord Token Finder")
         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
         time.sleep(3)
         print('Retrouver une partie du token discord d\'un utilisateur en connaissant son ID')
         print(Style.RESET_ALL)
         id = input(Fore.LIGHTBLACK_EX + "ID : ")
         req = requests.get('https://leaked.wiki/discorduser?id=' + id)
         data = req.json()
         if data['success'] == False:
            print('ID invalide')
            input("Press Enter to continue...")
            os.system('cls')
         else:
            print("Cible : " + data['username'] + "#" + data['discriminator'])
            time.sleep(0.5)
            print("Recherche du token...")
            time.sleep(0.5)
            print("Token Trouvé ! : " + str(data['partial_token']))
            time.sleep(0.5)
            pyperclip.copy(str(data['partial_token']))
            print("Token copié dans le presse-papier!")
            print(Style.RESET_ALL)
            input("Press Enter to continue...")

         
      if choixtools=="0":
         os.system("cls")
         print("Retour...")
         time.sleep(0.5)
         os.system("cls")
      
      
   if choixversion==choixgeoip:
      ip=input(Fore.MAGENTA + "IP a geolocaliser: ")
      req = requests.get('http://ip-api.com/json/' + ip)
      data = req.json()
      print(Style.RESET_ALL)
      print(Fore.MAGENTA + "IP : " + data['query'])
      time.sleep(0.5)
      print("Pays : " + data['country'])
      time.sleep(0.5)
      print("Region : " + data['region'])
      time.sleep(0.5)
      print("Ville : " + data['city'])
      time.sleep(0.5)
      print("Latitude : " + str(data['lat']))
      time.sleep(0.5)
      print("Longitude : " + str(data['lon']))
      time.sleep(0.5)
      print("Code Postal : " + str(data['zip']))
      time.sleep(0.5)
      print("Fuseau horaire : " + str(data['timezone']))
      time.sleep(0.5)
      print("Opérateur : " + str(data['isp']))
      time.sleep(0.5)
      print("Organisation : " + str(data['org']))
      time.sleep(0.5)
      print("AS : " + str(data['as']))
      save = input("Sauvegarder les infos? (y/n) : ")
      if save == "y":
            f = open("ip"+ ip +".txt", "a")
            f.write("IP : " + data['query'] + "\n" + str(data['org']) + "\n" + str(data['isp']) + "\n" + str(data['timezone']) + "\n" + str(data['zip']) + "\n" + str(data['lon']) + "\n" + str(data['lat']) + "\n" + str(data['city']) + "\n" + str(data['region']) + "\n" + str(data['country']))
            f.close()
            print("Sauvegarde effectuée!")
            time.sleep(2)
            print(Style.RESET_ALL)
      else:
            print("Sauvegarde annulée!")
            time.sleep(2)
            print(Style.RESET_ALL)
      time.sleep(5)
      
   if choixversion==choixcheckmail:
      mail_check=input(Fore.MAGENTA + "Email to check: ")
      print(Style.RESET_ALL)
      Check_mail_dns = requests.get('https://api.leaked.wiki/checkemail?email=' + mail_check)
      data = Check_mail_dns.json()
      if data['valid'] == "true":
         print(Fore.GREEN + "Email valide!")
         time.sleep(2)
         print(Style.RESET_ALL)
      else:
         print(Fore.RED + "Email invalide!")
         time.sleep(2)
         print(Style.RESET_ALL)

   if choixversion==choixquitter:
      print("Merci d'avoir utilisé Finder V-Pro!")
      time.sleep(2)
      sys.exit()
   if choixversion==choiximages:
      echo=[]
      textstring=[]
      imageslink = input("Coller le lien de l'image : ")
      url = ('https://yandex.ru/images/search?rpt=imageview&url=' + imageslink)
      response = requests.get(url)
      print(response)
      html = response.content
      soup = BeautifulSoup(html, "html.parser")
      for data in soup.find_all("div", {"class": "CbirSites-ItemTitle"}):
         for a in data.find_all('a'):
            print(a.get('href'))
            print(a.text)
            print('----------------------------------------------------')
      time.sleep(40) 
      
      
   if choixversion==choixdiscord:
      id = input(Fore.MAGENTA + "ID Discord : ")
      req = requests.get('https://api.leaked.wiki/discorduser?id=' + id)
      data = req.json()
      print(Style.RESET_ALL)
      discord_user ="Nom d'utilisateur : " + data['username'] + "#" + data['discriminator']
      print(Fore.RED + discord_user)
      time.sleep(0.5)
      discord_profile =  data['avatar']
      
      print("Url du Profil : " + data['avatar'])
      time.sleep(0.5)
      print("Url Bannière : " + str(data['banner']))
      print(Style.RESET_ALL)
      if data['banner'] == None:
         print(Fore.RED + "Pas de bannière")
         none = "Pas de bannière ❌"



      
      print("Ouverture de l'interface web")
      @app.route('/')
      def index():
         try:
            n = 2
            return render_template("discord.html",github=github,discord_user=discord_user,profile_img=data['avatar'],banner=str(data['banner']),error=False)
         except:
            return render_template("discord.html",github=github,error=True)
      
      
      @app.route('/eraseit/')


      def eraseit():
         try:
            return render_template("index.html",github=github,discord_user=discord_user,profile_img=data['avatar'],banner=str(data['banner']),error=False)
         except:
            return render_template("index.html",github=github,error=True)
         


      webbrowser.open('http://127.0.0.1:5000')
      if __name__ == '__main__':
         print("Statut :" + Fore.GREEN + " OK")
         print(Style.RESET_ALL)
         app.run()


      

   if choixversion==choixname:
      Lastname=input(Fore.MAGENTA + "Nom de famille précis : ")
      Firstname=input(Fore.MAGENTA + "Prénom précis : ")
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
 

      Nb_tel=len(Telephones)
      tel1 = Telephones[0]
      if Nb_tel > 1:
         tel2 = Telephones[1]
         if Nb_tel > 2:
            tel3 = Telephones[2]
            if Nb_tel > 3:
               tel4 = Telephones[3]

      Nb_adresse=len(Adresses)
      adresses1 = Adresses[0]
      if Nb_adresse > 1:
         adresses2 = Adresses[1]
         if Nb_adresse > 2:
            adresses3 = Adresses[2]
      #async def webmii():
         #time.sleep(10)
         #reqs = requests.get('https://webmii.com/people?n=%22'+ Firstname + '%20' + Lastname + '%22#gsc.tab=0&gsc.q=%22' + Firstname + '%20' + Lastname + '%22&gsc.sort=date')
         #pagemii = reqs.content
         #bs = BeautifulSoup(pagemii,features="html.parser")
         #webmii_scrap = soup.find('div', {'class': 'resultdate-box'})
         #print(webmii_scrap) 



      elapsed = end - start
      print(f'Temps d\'exécution : {elapsed:.2}ms')
      print("Ouverture de l'interface web")

      @app.route('/')

      def index():
         try:
            os.system("ipconfig /flushdns")
            time.sleep(2)
            os.system("cls")
            n = 2
            return render_template("index.html",github=github,street1=adresses1,lastname1=bloc_nom1["title"],phone1=tel1,error=False)
         except:
            return render_template("index.html",github=github,error=True)
      
      
      @app.route('/eraseit/')


      def eraseit():
         try:
            return render_template("index.html",github=github,street=adresses2,lastname=bloc_nom2["title"],phone=tel2,error=False)
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
    tel = soup.find_all('div', {'class': 'tel'})
    telephone=[]
    for e in tel:
        e=e.text
        telephone.append(e)
        e = e.replace('\n', '')
        res = [str(sub.split('\n')[1]) for sub in telephone]
        StrNum = "".join(res)
        print("Numero de telephone :" + str(StrNum).lstrip())
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
    os.system("ipconfig /flushdns")
    time.sleep(2)
    os.system("cls")

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
