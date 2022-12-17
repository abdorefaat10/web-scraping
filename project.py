import requests
import bs4

page = requests.get('https://www.awfarlak.com/ar/c/laptops/gaming-laptops')
page2 = requests.get('https://www.awfarlak.com/ar/c/laptops/gaming-laptops/page/2')

soucre = page.content + page2.content

soup = bs4.BeautifulSoup(soucre, 'html.parser')

prices = soup.find_all('span', {'class': 'price'})
labs = soup.find_all('h3', {'class': 'wd-entities-title'})

price_lab = []
labs_list = []
links = []

for i in range(len(prices)):
    price_lab.append(prices[i].text)
    labs_list.append(labs[i].text)
    links.append(labs[i].find('a').get('href'))

for i in range(len(labs_list)):
    print(labs_list[i], '--------- ', price_lab[i], '--------- ', links[i])
