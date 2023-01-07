from lxml import html
import requests

page = requests.get('https://www.goodreads.com/author/quotes/9810.Albert_Einstein')
tree = html.fromstring(page.content)

quotes = tree.xpath('//div[@class="quoteText"]/text()')


print quotes
