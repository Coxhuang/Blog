from django.conf.urls import url,include
from django.contrib import admin
from BlogApp import views
from BlogApp.views import FIRST



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^home/', views.home),
    url(r'^timeline/', views.timeline),
    url(r'^messageboard/', views.messageboard),
    url(r'^msgajax/', views.msgajax),
    url(r'^content-data-(\d+)/', views.content, name="content_url"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
