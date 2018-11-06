from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.mptt_list, name='mptt_list'),
    url(r'^(?P<pk>\d+)/$', views.group_detail, name='group_detail'),
    url(r'^el=(?P<pk>\d+)$', views.element_detail, name='element_detail'),
    url(r'^create_el(?P<pk>\d+)$', views.create_el, name='create_el'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
