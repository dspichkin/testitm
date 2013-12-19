from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers

from slides import views

router = routers.DefaultRouter()
router.register(r'steps', views.SlideViewSet)
router.register(r'attempts', views.AttemptViewSet)


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'itm.views.home', name='home'),
    # url(r'^itm/', include('itm.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/steps/$', user_list, name='user-list'),
    #url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
)
