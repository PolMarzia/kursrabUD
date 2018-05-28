from Kursovaya import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^admin_page/$', views.admin_page, name="admin_page"),
    url(r'^admin_redact/$', views.admin_redact, name="admin_redact"),
    url(r'^admin_add/$', views.admin_add, name="admin_add"),
    url(r'^admin_delete/$', views.admin_delete, name="admin_delete"),
]
