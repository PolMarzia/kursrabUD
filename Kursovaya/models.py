from django.db import models

# Create your models here.

#Дисциплина
class Disciplina(models.Model):
    id_discipl=models.AutoField(primary_key=models.ProtectedError)
    name_discipl=models.CharField(max_length=100)
    def __str__(self):
        return self.name_discipl


#Преподаватель
class Prepod(models.Model):
    id_prepod=models.AutoField(primary_key=models.ProtectedError)
    FIO_prepod=models.CharField(max_length=100)
    discipl=models.ForeignKey(Disciplina, on_delete=models.CASCADE, default='')
    stavka_prepod=models.FloatField(default=0)
    def __str__(self):
        return self.FIO_prepod

#Кампус
class Kampus(models.Model):
    id_kampus=models.AutoField(primary_key=models.ProtectedError)
    adress_kampus=models.CharField(max_length=100)
    name_kampus=models.CharField(max_length=50)
    def __str__(self):
     return self.name_kampus

#Институт
class Institute(models.Model):
    id_inst=models.AutoField(primary_key=models.ProtectedError)
    name_inst=models.CharField(max_length=50)
    kampus_inst=models.ForeignKey(Kampus, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.name_inst


#Кафедра
class Kafedra(models.Model):
    id_kaf=models.AutoField(primary_key=models.ProtectedError)
    name_kaf=models.CharField(max_length=100)
    inst=models.ForeignKey(Institute, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.name_kaf

#Аудитория
class Auditoria(models.Model):
    id_aud=models.AutoField(primary_key=models.ProtectedError)
    number_aud=models.IntegerField(default=0)
    kampus_aud=models.ForeignKey(Kampus, on_delete=models.CASCADE, default='')
    mesta=models.IntegerField(default=0)
    def __str__(self):
        return "{0}".format(self.number_aud)

#Форма обучения
class Forma_ob(models.Model):
    id_forma=models.AutoField(primary_key=models.ProtectedError)
    name_forma=models.CharField(max_length=50)
    def __str__(self):
        return self.name_forma

#Направление подготовки
class Napravlenie(models.Model):
    id_napr=models.AutoField(primary_key=models.ProtectedError)
    nazv_napr=models.CharField(max_length=50)
    def __str__(self):
        return self.nazv_napr

#Учебный план
class Uch_plan(models.Model):
    id_uch=models.AutoField(primary_key=models.ProtectedError)
    profil=models.CharField(max_length=20)
    srok_ob=models.IntegerField
    vidi_deyat=models.CharField(max_length=100)
    progr_podg=models.ForeignKey(Napravlenie, on_delete=models.CASCADE, default='')
    date_nach=models.DateField
    obr_std=models.CharField(max_length=20)
    def __str__(self):
        return "{0}".format(self.id_uch)

#Часы
class Chasi(models.Model):
    id_chasi=models.AutoField(primary_key=models.ProtectedError)
    kod_discipl=models.ForeignKey(Disciplina, on_delete=models.CASCADE, default='')
    semestr=models.IntegerField
    kod_uch_plan=models.ForeignKey(Uch_plan, on_delete=models.CASCADE, default='')
    kol_vo_chas=models.IntegerField
    discipl_chasi=models.ForeignKey(Napravlenie, on_delete=models.CASCADE, default='')
    def __str__(self):
        return "{0}".format(self.id_chasi)

#Группа
class Grouppa(models.Model):
    id_group = models.AutoField(primary_key=models.ProtectedError)
    name_group=models.CharField(max_length=10)
    chisl=models.IntegerField(default=0)
    form_ob=models.ForeignKey(Forma_ob)
    napravl=models.ForeignKey(Napravlenie)
    kaf=models.ForeignKey(Kafedra)
    def __str__(self):
        return self.name_group


#Дата занятия
class Data(models.Model):
    id_data=models.AutoField(primary_key=models.ProtectedError)
    chislo=models.DateField(blank=True)
    num_para=models.IntegerField(default=1)
    num_group=models.ForeignKey(Grouppa)
    def __str__(self):
        return "{0}".format(self.chislo)
