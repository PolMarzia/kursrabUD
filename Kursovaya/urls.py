from Kursovaya import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^admin_page_main/$', views.admin_page_main, name="admin_page_main"),
    url(r'^admin_page_discipl/$', views.admin_page_discipl, name="admin_page_discipl"),
    url(r'^admin_page_prepod/$', views.admin_page_prepod, name="admin_page_prepod"),
    url(r'^admin_page_kampus/$', views.admin_page_kampus, name="admin_page_kampus"),
    url(r'^admin_page_inst/$', views.admin_page_inst, name="admin_page_inst"),
    url(r'^admin_page_kafedra/$', views.admin_page_kafedra, name="admin_page_kafedra"),
    url(r'^admin_page_aud/$', views.admin_page_aud, name="admin_page_aud"),
    url(r'^admin_page_forma_ob/$', views.admin_page_forma_ob, name="admin_page_forma_ob"),
    url(r'^admin_page_napravl/$', views.admin_page_napravl, name="admin_page_napravl"),
    url(r'^admin_page_uchplan/$', views.admin_page_uchplan, name="admin_page_uchplan"),
    url(r'^admin_page_chasi/$', views.admin_page_chasi, name="admin_page_chasi"),
    url(r'^admin_page_grouppa/$', views.admin_page_grouppa, name="admin_page_grouppa"),
    url(r'^admin_page_data/$', views.admin_page_data, name="admin_page_data"),
    url(r'^admin_redact/$', views.admin_redact, name="admin_redact"),
    url(r'^admin_add/$', views.admin_add, name="admin_add"),
    url(r'^admin_delete/$', views.admin_delete, name="admin_delete"),
]
