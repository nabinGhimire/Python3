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
