from django.shortcuts import render


from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests

from django.template import RequestContext,loader


def get_links_from(url):
    web_data = requests.get(url)
    web_data.encoding = "utf-8"
    soup = BeautifulSoup(web_data.text, 'lxml' )
    items = soup.select('div.list_list ul li')

    item_list = []
    for item in items:
        short_link = item.a.get('href')[6:]
        title = item.a.get('title')
        pub_date = item.text[-10:]
        data ={
            'pub_date':pub_date,
            'title':title,
            'short_link':short_link,
        }
        item_list.append(data)
    return item_list
#print(get_links_from('http://www.hp.gov.cn/hplh/gzdt/list.shtml'))

def get_page_info_from(url,data=None):
    web_data = requests.get(url)
    if web_data.status_code == 404:
        pass
    else:
        web_data.encoding = "utf-8"
        soup_page = BeautifulSoup(web_data.text,'lxml')
        page_title = soup_page.select('div.content_title td p')[0].text
        page_tips = soup_page.select('div.content_title td')[1].text[-15:]
        contents = soup_page.select('div#zoomcon p')
        content_list = []
        for content in contents:
            content = content.text.replace('\xa0',' ')
            content_list.append(content)

        data={
            'title':page_title,
            'tip':page_tips,
            'contents':content_list,
        }
        return data

def parse_lianhejie_index(request):
    template = loader.get_template('parse_lianhejie/parse_lianhejie_index.html')
    url = 'http://www.hp.gov.cn/hplh/gzdt/list.shtml'
    get_links = get_links_from(url)
    context = {
        'get_links' : get_links
    }

    return HttpResponse(template.render(context))
    # return render(request,'parse/index.html',context)

def parse_lianhejie_page_detail(request,a1,a2,a3,a4):
    template = loader.get_template('parse_lianhejie/parse_lianhejie_page_detail.html')
    url = "http://www.hp.gov.cn/"+a1+'/'+a2+'/'+a3+'/'+a4
    page_info = get_page_info_from(url)
    context = {'page_info' : page_info}
    return HttpResponse(template.render(context))