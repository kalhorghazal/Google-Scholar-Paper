users_to_get_start = 0
users_to_get_end = 40 * 1000

import pandas as pd
import time
import random
import os
from datetime import datetime
from google.colab import drive

drive.mount('drive')

data_path = 'drive/My Drive/scholar_paper/crawled_data/'

import requests
from bs4 import BeautifulSoup

class UserPageCrawler:
    def __init__(self):
        self.all_users = {}

    def get_page_text(self, url):
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        if r.status_code==200:
            return r.text
        return False
    
    def get_user_csv_fields(self, soup, user_url):
        upper_part_div = soup.find('div', attrs={'class':'gsc_lcl'})
        name = upper_part_div.find('div', attrs={'id': 'gsc_prf_in'}).text.replace(',', ' ')
        try:
            title = upper_part_div.find('div', attrs={'class':'gsc_prf_il'}).text.replace(',', ' ')
        except Exception as e:
            title = '-'
        try:
            uni_name = upper_part_div.find('div', attrs={'class':'gsc_prf_il'}).find('a').text.replace(',', ' ')
        except Exception as e:
            uni_name = '-'
        try:
            uni_url = upper_part_div.find('div', attrs={'class':'gsc_prf_il'}).find('a').get('href')
        except Exception as e:
            uni_url = '-'
        try:
            website = upper_part_div.find('div', attrs={'class':'gsc_prf_il'}).find('a').get('href')
        except Exception as e:
            website = '-'       

        all_info = soup.find('div', attrs={'id':'gsc_prf_i'}).text.replace('\n', '\t').replace('\t', ' ').replace(',', ' ')

        this_button = soup.find('button', attrs={'id':'gsc_coauth_opn'})
        if not this_button == None:
            has_view_all_button = 'True'
        else:
            has_view_all_button = 'False'

        info_to_write = user_url+','+name+','+title+','+uni_name+','+uni_url+','+website+','+has_view_all_button+','+all_info+'\n'
        with open(data_path + 'users.csv', 'a') as fp:
            fp.write(info_to_write)
    
    def get_user_related_fields(self, soup, user_url):
        field_div_part = soup.find('div', attrs={'id': 'gsc_prf_int'})
        field_as = field_div_part.find_all('a')
        for field_a in field_as:
            field_name = field_a.text
            field_url = field_a.get('href') 
            info_to_write = user_url+','+field_name+','+field_url+'\n'
            with open(data_path + 'user_fields.csv', 'a') as fp:
                fp.write(info_to_write)
    
    def get_citation_table(self, soup, user_url):
        citation_table_part = soup.find('table', attrs={'id':'gsc_rsb_st'}).find('tbody')
        table_trs = citation_table_part.find_all('tr')
        citation_all = table_trs[0].find_all('td')[1].text
        citation_2014 = table_trs[0].find_all('td')[2].text
        h_all = table_trs[1].find_all('td')[1].text
        h_2014 = table_trs[1].find_all('td')[2].text
        i_all = table_trs[2].find_all('td')[1].text
        i_2014 = table_trs[2].find_all('td')[2].text
        info_to_write = user_url+','+citation_all+','+citation_2014+','+h_all+','+h_2014+','+i_all+','+i_2014+'\n'
        with open(data_path + 'citation_table.csv', 'a') as fp:
            fp.write(info_to_write)
    
    def get_citation_by_year(self, soup, user_url):
        table_part = soup.find('div', attrs={'id': 'gsc_rsb_cit'}).find('div', attrs={'class': 'gsc_md_hist_b'})
        
        span_texts = [s.text for s in table_part.find_all('span')]
        a_texts = [a.text for a in table_part.find_all('a')]
        for i in range(len(a_texts)):
            info_to_write = user_url+','+span_texts[i]+','+a_texts[i]+'\n'
            with open(data_path + 'citation_by_year.csv', 'a') as fp:
                fp.write(info_to_write)

    def find_coauthors(self, soup, user_url):
        try:
            coauthors_part = soup.find('div', attrs={'id': 'gsc_rsb_co'})
            all_lis = coauthors_part.find('ul', attrs={'class':'gsc_rsb_a'}).find_all('li')
            for li in all_lis:
                target_name = li.find('a').text.replace(',', ' ')
                target_url = li.find('a').get('href')
                info_to_write = user_url+','+target_name+','+target_url+'\n'
                with open(data_path + 'added_coauthors.csv', 'a') as fp:
                    fp.write(info_to_write)
        except Exception as e:
            print('User did not have coauthors')
    
    def get_all_papers(self, soup, user_url):
        papers_table = soup.find('tbody', attrs={'id': 'gsc_a_b'})
        all_trs = papers_table.find_all('tr')
        for tr in all_trs:
            Paper_Name = tr.find_all('td')[0].find('a').text.replace(',', '')
            Paper_URL = tr.find_all('td')[0].find('a').get('data-href')
            Authors = tr.find_all('td')[0].find_all('div')[0].text.replace(',', ' |')
            Cited_by_count = tr.find_all('td')[1].find('a').text
            Cited_by_URL = tr.find_all('td')[1].find('a').get('href').replace(',', '@#&')
            Year = tr.find_all('td')[2].text
            info_to_write = user_url+','+Paper_Name+','+Paper_URL+','+Authors+','+Cited_by_count+','+Cited_by_URL+','+Year+'\n'
            with open(data_path + 'papers.csv', 'a') as fp:
                fp.write(info_to_write)

    def crawl_journals(self, soup, user_url):
        content_div = soup.find('div', attrs={'id':'gs_bdy_ccl'})
        grays = soup.find_all("div", attrs={"class": "gs_gray"})
        with open(data_path + 'user_journals.csv', 'a') as fp:
            for i in range(len(grays)):
                if(i%2 == 1):
                    info_to_write = user_url+','+grays[i].text.split(',')[0]+'\n'
                    fp.write(info_to_write)

    def crawl_this_users_page(self, user_url):
        page_text = self.get_page_text(user_url)
        soup = BeautifulSoup(page_text, 'html.parser')
        content_div = soup.find('div', attrs={'id':'gs_bdy_ccl'})
        self.get_user_csv_fields(content_div, user_url)
        self.get_user_related_fields(content_div, user_url)
        self.get_citation_table(content_div, user_url)
        self.get_citation_by_year(content_div, user_url)
        self.find_coauthors(content_div, user_url)
        self.get_all_papers(content_div, user_url)
        self.crawl_journals(content_div, user_url)

with open('drive/My Drive/scholar_paper/new_users_url.txt', 'r') as fp:
    user_urls_to_crawl  = fp.read().split('\n')
user_urls_to_crawl = user_urls_to_crawl[users_to_get_start:users_to_get_end]

seen_user_urls = pd.read_csv(data_path + 'users.csv')['URL'].values.tolist()
print('total users crawled:', len(seen_user_urls), '\n')
print('now crawling users:', users_to_get_start, 'to', users_to_get_end, '\n')
now = datetime.now()
print('start time:', now.strftime("%d/%m/%Y %H:%M:%S"), '\n')

upc = UserPageCrawler()
i = len(seen_user_urls) + 1
for url in user_urls_to_crawl:
    this_users_url = url
    if not this_users_url in seen_user_urls:
        print('crawling user number:', i, '---> URL:', this_users_url)
        i += 1
        if i%698==1:
            time.sleep(random.randint(20, 50))
        try:
            upc.crawl_this_users_page(this_users_url)
            seen_user_urls.append(this_users_url)
#             time.sleep(random.randint(0, 10))
        except Exception as e:
            print('error:', e)
            
now = datetime.now()
print('\nfinish time:', now.strftime("%d/%m/%Y %H:%M:%S"))

