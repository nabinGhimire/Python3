#import lxml.html
from lxml import html
from lxml.etree import XPath as xpath
# from lxml import etree
import requests


#page = "http://www.nrb.org.np/fxmexchangerate.php"
#response = lxml.html.parse(page)

page = requests.get('http://www.nrb.org.np/fxmexchangerate.php')
html_content = html.fromstring(page.content)

# = html_content.xpath('//h3[@data-analytics]/a/span/text()')
currencies = html_content.xpath('//tr//td//font/text()')

#print(currencies)

# for currency in currencies:
#     print(currency)

#for i in range(1,(len(currencies))):
#    #print(i)
#    print(currencies[i][1])
print("Currency Indian Rupees")
print('-----')
print("Unit", currencies[8].strip())
print("Buyiing", currencies[9].strip())
print("Selling", currencies[10].strip())
print('-----')

for i in range(18,len(currencies)-8,4):
    print("Currency", currencies[i].strip())
    print('-----')
    print("Unit", currencies[i+1].strip())
    print("Buyiing", currencies[i+2].strip())
    print("Selling",currencies[i+3].strip())
    print('-----')

#print("Currency", currencies[23].strip())
#print('-----')
# print("Unit", currencies[24].strip())
# print("Buyiing", currencies[25].strip())
# print("Selling",currencies[26].strip())

from lxml import html
from lxml.etree import XPath as xpath
import requests


page = requests.get('http://www.nrb.org.np/fxmexchangerate.php')
html_content = html.fromstring(page.content)

currencies = html_content.xpath('//tr//td//font/text()')

print("Currency Indian Rupees")
print('-----')
print("Unit", currencies[8].strip())
print("Buyiing", currencies[9].strip())
print("Selling", currencies[10].strip())
print('-----')

for i in range(18,len(currencies)-8,4):
    print("Currency", currencies[i].strip())
    print('-----')
    print("Unit", currencies[i+1].strip())
    print("Buyiing", currencies[i+2].strip())
    print("Selling",currencies[i+3].strip())
    print("-----")
