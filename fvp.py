import os, requests, time
from googlesearch import search
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


# api root-me dead
# api github changed their endpoint to /users/ instead of /
api_endpoint = ["https://api.github.com/users/"]


def username_finder(username):
   for endpoint in api_endpoint:
      endpoint = endpoint+username
      response = requests.get(endpoint)
      if response.status_code == 200:
         print("User found on " + endpoint)
         print(endpoint + "\n")
      elif response.status_code == 404:
         print("User doesn't seem to exist on " + endpoint)

"""
# TO FIX
def namefinder_api():
    lastname = input("Last name: ")
    city = input("City: ")
   from selenium import webdriver
    driver.get(f"https://www.118712.fr/recherche/auto/{city}/{lastname}")
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find_all('article')  # Trouver tous les éléments 'article'
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
"""


def googlesearch_api(query):
   for result in search(query):
      print(result + "\n")




while True:
   choix = None
   print("1. Google Search \n 2. Username Finder \n 3. Name searcher")
   choix = input(Fore.MAGENTA + "Choix de valeur : ")
   if choix == "1":
      query = input("Query : ")
      googlesearch_api(query)
   if choix == "2":
      temp_user_value = input("Username : ")
      username_finder(temp_user_value)
   """if choix == "3":
      namefinder_api()"""



