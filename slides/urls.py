from django.conf.urls import patterns, url, include
from rest_framework import routers

from slides import views

router = routers.DefaultRouter()
router.register(r'steps', views.SlideViewSet)
router.register(r'attempts', views.AttemptViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
)