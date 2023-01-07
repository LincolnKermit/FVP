from __future__ import print_function
from re import sub
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
urlpage=urlopen("https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui=Founchot&ou=Plaisir&univers=pagesblanches&idOu=").read()
bswebpage=BeautifulSoup(urlpage)
results=bswebpage.findAll("div",{'class':"pj-lb pj-link"})
for result in results:
    print("\nQuotes\n")
    print(sub("&ldquo;|.&rdquo;","","".join(result.contents[0:1]).strip()))
