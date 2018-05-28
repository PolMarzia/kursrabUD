from django.forms import ModelForm
from Kursovaya.models import *

class disciplina_form(ModelForm):
    class Meta:
        model = Disciplina
        fields = ['name']
        labels = {
            'name' : 'Название'
        }

class prepod_form(ModelForm):
    class Meta:
        model = Prepod
        fields = ['FIO_prepod', 'discipl', 'stavka_prepod']
        labels = {
            'FIO_prepod' : 'ФИО преподавателя',
            'discipl' : 'Дисциплина',
            'stavka_prepod' : 'Ставка преподавателя'
        }

class kampus_form(ModelForm):
    class Meta:
        model = Kampus
        fields = ['adress_kampus', 'name_kampus']
        labels = {
            'adress_kampus' : 'Адрес кампуса',
            'name_kampus' : 'Название кампуса',

        }

class institute_form(ModelForm):
    class Meta:
        model = Institute
        fields = ['name_inst', 'kampus_inst']
        labels = {
            'name_inst' : 'Название института',
            'kampus_inst' : 'Кампус, к которому принадлежит'
        }

class kafedra_form(ModelForm):
    class Meta:
        model = Kafedra
        fields = ['name_kaf', 'inst']
        labels = {
            'name_kaf' : 'Название кафедры',
            'inst' : 'Институт, к которому принадлежит'
        }

class auditoria_form(ModelForm):
    class Meta:
        model = Auditoria
        fields = ['number_aud', 'kampus_aud', 'mesta']
        labels = {
            'number_aud' : 'Номер аудитории',
            'kampus_aud' : 'Кампус',
            'mesta' : 'Количество мест'
        }

class forma_ob_form(ModelForm):
    class Meta:
        model = Forma_ob
        fields = ['name_forma']
        labels = {
            'name_forma' : 'Форма обучения'
        }

class napravlenie_form(ModelForm):
    class Meta:
        model = Napravlenie
        fields = ['nazv_napr']
        labels = {
            'nazv_napr' : 'Название направления'
        }

class uch_plan_form(ModelForm):
    class Meta:
        model = Uch_plan
        fields = ['profil', 'srok_ob', 'vidi_deyat', 'progr_podg', 'date_nach', 'obr_std', 'napr_podg_plan']
        labels = {
            'profil' : 'Профиль подготовки',
            'srok_ob' : 'Срок обучения',
            'vidi_deyat' : 'Виды деятельности',
            'progr_podg' : 'Направление подготовки',
            'date_nach' : 'Дата начала обучения',
            'obr_std' : 'Образовательный стандарт',
        }

class chasi_form(ModelForm):
    class Meta:
        model = Chasi
        fields = ['kod_discipl', 'semestr', 'kod_uch_plan', 'kol_vo_chas', 'discipl_chasi']
        labels = {
            'kod_discipl' : 'Код дисциплины',
            'semestr' : 'Семестр',
            'kod_uch_plan' : 'Код учебного плана',
            'kol_vo_chas' : 'Количество часов',
            'discipl_chasi' : 'Направление подготовки',
        }


class grouppa_form(ModelForm):
    class Meta:
        model = Grouppa
        fields = ['name_group', 'chisl', 'form_ob', 'napravl', 'kaf']
        labels = {
            'name_group' : 'Номер группы',
            'chisl' : 'Часы',
            'form_ob' : 'Форма обучения',
            'napravl' : 'Направление подготовки',
            'kaf' : 'Кафедра',
        }


class data_form(ModelForm):
    class Meta:
        model = Data
        fields = ['chislo', 'num_para', 'num_group']
        labels = {
            'chislo' : 'Число',
            'num_para' : 'Номер пары',
            'num_group' : 'Номер группы',
        }


