from django.conf.urls import url

from .views import page


urlpatterns = (
	url(r'^(?P<slug>[\./-]+)/$', page, name='page'),
	url(r'^$', page, name='homepage'),
)