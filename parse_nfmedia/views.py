from django.shortcuts import render


from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests

from django.template import RequestContext,loader


def get_links_from(url):
    web_data = requests.get(url)
    web_data.encoding = "utf-8"
    soup = BeautifulSoup(web_data.text, 'lxml' )
    items = soup.select('div.sub_content ul li')

    item_list = []
    for item in items:
        short_link = item.a.get('href')[2:]
        title = item.a.text
        pub_date = item.text[-11:-1]
        data ={
            'pub_date':pub_date,
            'title':title,
            'short_link':short_link,
        }
        item_list.append(data)
    return item_list


def get_page_info_from(url,data=None):
    web_data = requests.get(url)
    if web_data.status_code == 404:
        pass
    else:
        web_data.encoding = "utf-8"
        soup_page = BeautifulSoup(web_data.text,'lxml')
        page_tips = soup_page.select('div.left div.info span')
        page_title = soup_page.select('div.left #title')[0].text




get_page_info_from('http://www.nfmedia.com/jtdt/201604/t20160401_368868.htm')
