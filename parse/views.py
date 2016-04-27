from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests

from django.template import RequestContext,loader
# 413龙华新闻

def get_links_from(url):
    web_data = requests.get(url)
    web_data.encoding = "utf-8"
    soup = BeautifulSoup(web_data.text, 'lxml' )

    #link1 = soup.select('div.left  ul li a')[0].get('href')
    items = soup.select('div.left  ul li ')

    item_list = []
    for item in items:
        pub_date = item.span.get_text()
        title = item.a.get_text()
        short_link = item.a.get('href')
        #lastword = short_link.split('/')[-1]
        link = "http://ilonghua.sznews.com/"+short_link
        #page_data = get_page_info_from(link)
        data ={
            'pub_date':pub_date,
            'link':link,
            'title':title,
            'short_link':short_link,
            #'lastword':lastword,
            #'page_data':page_data,

        }
        if title=='':
            pass
        else:
            item_list.append(data)
    return item_list


def get_page_info_from(url,data=None):
    web_data = requests.get(url)
    if web_data.status_code == 404:
        pass
    else:
        web_data.encoding = "utf-8"
        soup_page = BeautifulSoup(web_data.text,'lxml')
        page_tips = soup_page.select('div.newstop span')
        page_title = soup_page.select('div.newstop h2')[0].text
        page_contents= soup_page.select('div.lhnewcon p')
        page_imgs = soup_page.select('div.lhnewcon img')
        #content = ''
        tip = ''
        content_list = []
        imgs = []
        for page_content in page_contents:
            # content += page_content.get_text()+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            content_list.append(page_content.get_text())
        for page_tip in page_tips:
            tip += page_tip.get_text()+' '
        for page_img in page_imgs:
            templink = page_img.get('src')
            templink = templink.replace('../../..','http://ilonghua.sznews.com')
            imgs.append(templink)
        data ={
            'title':page_title.strip(),
            # 'content':content,
            'tip':tip,
            'contents':content_list,
            'imgs':imgs,
            #'url':url
        }
        return data


def index(request):
    template = loader.get_template('parse/index.html')
    url = 'http://ilonghua.sznews.com/node_126826.htm'
    get_links = get_links_from(url)
    context = {
        'get_links' : get_links
    }

    return HttpResponse(template.render(context))
    # return render(request,'parse/index.html',context)

def page_detail(request,a1,a2,a3,a4):
    template = loader.get_template('parse/page_detail.html')
    url = "http://ilonghua.sznews.com/"+a1+'/'+a2+'/'+a3+'/'+a4
    page_info = get_page_info_from(url)
    context = {'page_info' : page_info}
    return HttpResponse(template.render(context))
