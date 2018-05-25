from Kursovaya import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^admin_page/$', views.admin_page, name="admin_page")
]
