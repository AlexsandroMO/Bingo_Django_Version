from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
#from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm, LdProjForm
from django.contrib import messages
##from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, LdProj

from django.utils.formats import localize
from django.db.models import Q

import Progpy as prog
#import delete_itens
import pandas as pd
import numpy as np
import random

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')


#@login_required
def home(request):

    #MyProjects = MyProject.objects.all().order_by('-project_name')
    #Employees = Employee.objects.all()

    return render(request, 'canto/home.html')

#@login_required
def index(request):

    def rad(df_cantada):
        status = False
        lista = []
        Lista = pd.read_csv('static/excel/Lista.csv')

        for i in Lista['LIS']:
            lista.append(i)

        if len(df_cantada['CANTADOS'] <= 99):
            canto = random.choice(lista)
            test = df_cantada[df_cantada['CANTADOS'] == canto ]

            if len(test['CANTADOS']) == 0:
                prog.actualy_list(canto)
                return canto

            else:
                status = True
                while status is True:
                    canto = random.choice(lista)
                    
                    if len(test['CANTADOS']) == 0:
                        status = False
                        prog.actualy_list(canto)
                        return canto

                    else:
                        status = True
                    
                    status = False

        else:
            return '-'
    #-----------------------------------

    df_cantada = pd.read_csv('static/excel/BINGO.csv')
    num = rad(df_cantada)

    if num != None:
        falta = 0

        if num == '-':
            falta = 'Acabou!'
            var_list = prog.singed()
            return render(request, 'canto/index.html', {'var_list':var_list,'num':num, 'falta':falta})

        else:
            falta = 99 - len(df_cantada['CANTADOS'])
            var_list = prog.list_bingo(num)
            var_list = sorted(var_list)

        if len(df_cantada['CANTADOS']) == 100:
            falta = 'Acabou!'
            return render(request, 'canto/index.html', {'var_list':var_list,'num':num, 'falta':falta})

        else:
            return render(request, 'canto/index.html', {'var_list':var_list,'num':num, 'falta':falta})

    else:
        falta = 99 - len(df_cantada['CANTADOS'])
        var_list = sorted(df_cantada['CANTADOS'])

        if len(df_cantada['CANTADOS']) == 100:
            falta = 'Acabou!'
            return render(request, 'canto/index.html', {'var_list':var_list,'num':num, 'falta':falta})
        else:
            return render(request, 'canto/index.html', {'var_list':var_list,'num':num, 'falta':falta})


def table(request):

    df_cantada = prog.singed()
  
    var_list = df_cantada['CANTADOS']
    var_list = sorted(var_list)
    
    total = len(var_list)

    return render(request, 'canto/table-list.html', {'var_list':var_list, 'total':total})


def clear_all(request):
    prog.clear_List()
    prog.clear_df()
    return redirect("/")

