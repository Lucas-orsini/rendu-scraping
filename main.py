
import requests
from bs4 import BeautifulSoup

# page = r'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
#page = requests.get(page)

#page = page.text

#soup = BeautifulSoup(page, 'html.parser')＃

#tbody = soup.find('tbody', class_='lister-list')

#rows = tbody.find_all('tr')

#for row in rows:
    #title = row.find('td', class_='titleColumn').text
    #rating = row.find('td', class_='ratingColumn imdbRating').text
    #print(title, rating)

#page = r'https://www.nike.com/fr/w/chaussures-y7ok?cp=25116780465_search_%7Csneakers%7C10583502915%7C104926141416%7Ce%7Cc%7CFR%7Cproducts%7C452748965429&gclsrc=aw.ds&ds_rl=1252249&gclid=CjwKCAjwxOCRBhA8EiwA0X8hi6TIJ8BAkcbGp2Hbho2dwQniCypg5My_MIrZ0X6bIEG-qgltgffM8hoClbgQAvD_BwE'
#page = requests.get(page)

#page = page.text

#soup = BeautifulSoup(page, 'html.parser')

#articles = soup.find('div' , class_='product-grid')
#div = articles.find_all('div', class_='product-card')


#for row in div :
    #price = row.find('div', class_='product-price').text
    #title= row.find('div', class_='product-card__title').text
    #nb_color = row.find('div', class_='product-card__product-count').text
    #print(price, title, nb_color)

#for i in range(1, 25):
    #r = requests.get('http://www.scrapethissite.com/pages/forms/?page_num=' + str(i))

    #soup = BeautifulSoup(r.text, 'html.parser')

    #results = soup.find('table', attrs={'class': 'table'})
    #rows = results.find_all('tr', attrs={'class': 'team'})

    #records = []
    #for row in rows:
        #name = row.find('td', attrs={'class': 'name'}).text.strip()
        #year = row.find('td', attrs={'class': 'year'}).text.strip()
        #wins = row.find('td', attrs={'class': 'wins'}).text.strip()
        #losses = row.find('td', attrs={'class': 'losses'}).text.strip()
        #ot_losses = row.find('td', attrs={'class': 'ot-losses'}).text.strip()
        #gf = row.find('td', attrs={'class': 'gf'}).text.strip()
        #ga = row.find('td', attrs={'class': 'ga'}).text.strip()
        #records.append((name, year, wins, losses, ot_losses, gf, ga))

    #print(records)


import requests_cache
requests_cache = requests_cache.install_cache('cache')

page = r'https://leagueoflegends.fandom.com/wiki/List_of_champions'


class IMDBScraper():
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')
  
    def get_header(self):

        title= self.soup.find('h1', class_='page-header__title').text
        print(title)
        desc = self.soup.find('div', class_='mw-parser-output')
        para = desc.find('p').text
        print(para)

    def get_champions(self):
        sub_row = self.soup.find('table', class_='article-table').find('tbody').find_all('tr')
        del sub_row[0]
        for row in sub_row:
            if(row.find_all('td')[4].find('span') != None and row.find_all('td')[5].find('span') != None):
                champion = {
                    'Champion_name': row.find_all('td')[0]['data-sort-value'],
                    'Classes': row.find_all('td')[1]['data-sort-value'],
                    'Release date': row.find_all('td')[2].text.replace('\n',''),
                    'Patch number': row.find_all('td')[3].find('a')['title'],
                    'Blue essence': row.find_all('td')[4].find('span').text,
                    'Riot': row.find_all('td')[5].find('span').text,
                }
                print(champion)

    def get_reduc(self):
        title_reduc = self.soup.find('h3').find('span', class_=('mw-headline')).text
        exerpt_reduc = self.soup.find('dd').find('div', class_=('dablink')).text
        price_reduc = self.soup.dl.find_next('ul').find('li').text
        
        print(title_reduc,exerpt_reduc,price_reduc)

    def get_list_scrap (self):
        scrapped = self.soup.find('span', {"id": "List_of_Scrapped_Champions"}).text
       
        print(scrapped)

    def get_scraped_Champion(self):
        ul= self.soup.find("div",class_="columntemplate").find("ul").find_all("li")
        for row in ul:
            title = row.find('a')["title"]
            print(title)

    def get_trivia(self):
        trivia = self.soup.find('span', {"id": "Trivia"}).text
        print(trivia)

    def get_urf(self):
        urf = self.soup.find('div', class_=('columntemplate')).find_next('h2').find_next('ul').find_all("li")
        for row in urf:
            subtitle = row.find('a')["title"]
            print(subtitle)
        

scraper_header = IMDBScraper(page).get_header()

scraper_champion = IMDBScraper(page).get_champions()
scraper_reduct= IMDBScraper(page).get_reduc()
scraper_list= IMDBScraper(page).get_list_scrap()
scraper_scraped_champion= IMDBScraper(page).get_scraped_Champion()
scraper__trivia= IMDBScraper(page).get_trivia()
scraper_bottom= IMDBScraper(page).get_urf()

print(scraper_header , scraper_champion, scraper_reduct,scraper_list,scraper_scraped_champion,scraper__trivia,scraper_bottom)