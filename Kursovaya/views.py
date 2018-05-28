from django.shortcuts import render
from Kursovaya.models import *

# Create your views here.

def main(request):
    return render(request, 'index.html', locals())

def admin_page_main(request):
    return render(request, 'admin_page_main.html', locals())

def admin_page_discipl(request):
    Disciplina_list = Disciplina.objects.all()
    return render(request, 'admin_page_discipl.html', locals())

def admin_page_prepod(request):
    Prepod_list = Prepod.objects.all()
    return render(request, 'admin_page_prepod.html', locals())

def admin_page_kampus(request):
    Kampus_list = Kampus.objects.all()
    return render(request, 'admin_page_kampus.html', locals())

def admin_page_inst(request):
    Institute_list = Institute.objects.all()
    return render(request, 'admin_page_inst.html', locals())

def admin_page_kafedra(request):
    Kafedra_list = Kafedra.objects.all()
    return render(request, 'admin_page_kafedra.html', locals())

def admin_page_aud(request):
    Auditoria_list = Auditoria.objects.all()
    return render(request, 'admin_page_aud.html', locals())

def admin_page_forma_ob(request):
    Forma_ob_list = Forma_ob.objects.all()
    return render(request, 'admin_page_forma_ob.html', locals())

def admin_page_napravl(request):
    Napravlenie_list = Napravlenie.objects.all()
    return render(request, 'admin_page_napravl.html', locals())

def admin_page_uchplan(request):
    Uch_plan_list = Uch_plan.objects.all()
    return render(request, 'admin_page_uchplan.html', locals())

def admin_page_chasi(request):
    Chasi_list = Chasi.objects.all()
    return render(request, 'admin_page_chasi.html', locals())

def admin_page_grouppa(request):
    Grouppa_list = Grouppa.objects.all()
    return render(request, 'admin_page_grouppa.html', locals())

def admin_page_data(request):
    Data_list = Data.objects.all()
    return render(request, 'admin_page_data.html', locals())

def admin_redact(request):
    return render(request, 'admin_redact.html', locals())

def admin_add(request):
    return render(request, 'admin_add.html', locals())

def admin_delete(request):
    return render(request, 'admin_delete.html', locals())