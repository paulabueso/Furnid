from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'furnid.views.home', name='home'),
    url(r'profile/$', 'furnid.views.profile', name='profile'),
    url(r'customer/$', 'furnid.views.customer', name='customer'),

        #LOGIN AND REGISTER
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'furnid.views.register', name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'add_list/$', 'furnid.views.add_list', name='add_list'),
    url(r'add_item/$', 'furnid.views.add_item', name='add_item'),
    url(r'offer/$', 'furnid.views.offer', name='offer'),
    url(r'customerinfo/$', 'furnid.views.customerinfo', name='customerinfo'),

    url(r'^admin/', include(admin.site.urls)),

    #DECORATION
    url(r'what/$', 'furnid.views.what', name='what'),
    url(r'how/$', 'furnid.views.how', name='how'),
    url(r'contact/$', 'furnid.views.contact', name='contact'),


)
