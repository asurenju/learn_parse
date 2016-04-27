from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.parse_lianhejie_index,name='parse_lianhejie_index'),
    #url(r'^(\w+).htm/page/$',views.page_detail,name='parse_lianhejie_page'),
    # url(r'^(\w+)/(\w+)-(w+)/page/$',views.page_detail,name='page'),
    url(r'^([^/]+)/([^/]+)/([^/]+)/([^/]+)/page/$',views.parse_lianhejie_page_detail,name='parse_lianhejie_page_detail'),
]