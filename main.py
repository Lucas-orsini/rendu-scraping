
import requests
from bs4 import BeautifulSoup
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
