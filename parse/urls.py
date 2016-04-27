from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^(\w+).htm/page/$',views.page_detail,name='page'),
    # url(r'^(\w+)/(\w+)-(w+)/page/$',views.page_detail,name='page'),
    url(r'^([^/]+)/([^/]+)/([^/]+)/([^/]+)/page/$',views.page_detail,name='page_detail'),
]