
from bs4 import BeautifulSoup4

soup = BeautifulSoup(html_doc, 'html.parser')

soup.prettify()
