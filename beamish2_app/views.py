from django.shortcuts import render
from beamish2_app.models import *
from beamish2_app.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse



# View Pages

def Home(request):
    '''
    url(r'^$', views.Home, name='Home'),
    '''
    return render(request, 'beamish2_app/index.html')

def listMines(request):
    '''
    url(r'^list[m,M]ines/?$', views.listMines, name='listMines'),
    '''
    results = Minesite.objects.all()
    context_data = {'mine_list': results}
    return render(request, 'beamish2_app/mine_list.html', context_data)

def listCompany(request):
    '''
    url(r'^list[c,C]ompany/?$', views.listCompany, name='listCompany'),
    '''
    results = Company.objects.all()
    context_data = {'company_list': results}
    return render(request, 'beamish2_app/company_list.html', context_data)

def listMineral(request):
    '''
    url(r'^list[m,M]ineral/?$', views.listMineral, name='listMineral'),
    '''
    results = Minerals.objects.all()
    context_data = {'mineral_list': results}
    return render(request, 'beamish2_app/mineral_list.html', context_data)

def addMineral(request):
    '''
    url(r'^add[m,M]ineral/?$', views.addMineral, name='addMineral'),
    '''
    context_data = {'mineral_form': MineralForm()}
    return render(request, 'beamish2_app/mineral_add.html', context_data)

def addCompany(request):
    '''
    url(r'^add[c,C]ompany/?$', views.addCompany, name='addCompany'),
    '''
    context_data = {'company_form': CompanyForm()}
    return render(request, 'beamish2_app/company_add.html', context_data)

def addMines(request):
    '''
    url(r'^add[m,M]ines/?$', views.addMines, name='addMines'),
    '''
    context_data = {'mine_form': MinesiteForm()}
    return render(request, 'beamish2_app/mine_add.html', context_data)


#Submit Form Functions

def submitMineral(request):
    '''
    url(r'^submit[m,M]ineral/?$', views.submitMineral, name='submitMineral'),
    '''
    if request.method != 'POST':
        context_data = {'mineral_form' : MineralForm()}
    else:
        form = MineralForm(request.POST)
        if form.is_valid() != True:
            context_data = {'mineral_form' : form}
        else:
            data = form.cleaned_data
            new_auth_object = form.save()
            return HttpResponseRedirect(reverse('listMineral'))
    return render(request, 'beamish2_app/mineral_add.html', context_data)

def submitMines(request):
    '''
    url(r'^submit[m,M]ines/?$', views.submitMines, name='submitMines'),
    '''
    if request.method != 'POST':
        context_data = {'mine_form' : MinesiteForm()}
    else:
        form = MinesiteForm(request.POST)
        if form.is_valid() != True:
            context_data = {'mine_form' : form}
        else:
            data = form.cleaned_data
            new_auth_object = form.save()
            return HttpResponseRedirect(reverse('listMines'))
    return render(request, 'beamish2_app/mine_add.html', context_data)

def submitCompany(request):
    '''
    url(r'^submit[c,C]ompany/?$', views.submitCompany, name='submitCompany'),
    '''
    if request.method != 'POST':
        context_data = {'company_form' : CompanyForm()}
    else:
        form = CompanyForm(request.POST)
        if form.is_valid() != True:
            context_data = {'company_form' : form}
        else:
            data = form.cleaned_data
            new_auth_object = form.save()
            return HttpResponseRedirect(reverse('listCompany'))
    return render(request, 'beamish2_app/company_add.html', context_data)


#Update Entry Functions

def updateMineral(request, id):
    '''
    url(r'^update[m,M]ineral/(\d+)/?$', views.updateMineral, name='updateMineral'),
    '''
    mineral = Minerals.objects.get(pk=id)
    if request.method == 'POST':
        form = MineralForm(request.POST, instance = mineral)
        if form.is_valid() != True:
            context_data = {'update_form' : form}
        else:
            form.save()
            return HttpResponseRedirect(reverse('listMineral'))
    else:
        form = MineralForm(instance = mineral)
        context_data = {'update_form' : form}
    return render(request, 'beamish2_app/entry_update.html', context_data)

def updateMines(request, id):
    '''
    url(r'^update[m,M]ines/(\d+)/?$', views.updateMines, name='updateMines'),
    '''
    minesite = Minesite.objects.get(pk=id)
    if request.method == 'POST':
        form = MinesiteForm(request.POST, instance = minesite)
        if form.is_valid() != True:
            context_data = {'update_form' : form}
        else:
            form.save()
            return HttpResponseRedirect(reverse('listMines'))
    else:
        form = MinesiteForm(instance = minesite)
        context_data = {'update_form' : form}
    return render(request, 'beamish2_app/entry_update.html', context_data)

def updateCompany(request, id):
    '''
    url(r'^update[c,C]ompany/(\d+)/?$', views.updateCompany, name='updateCompany'),
    '''
    company = Company.objects.get(pk=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance = company)
        if form.is_valid() != True:
            context_data = {'update_form' : form}
        else:
            form.save()
            return HttpResponseRedirect(reverse('listCompany'))
    else:
        form = CompanyForm(instance = company)
        context_data = {'update_form' : form}
    return render(request, 'beamish2_app/entry_update.html', context_data)


#Delete Entry Functions

def deleteMineral(request, id):
    '''
    url(r'^delete[m,M]ineral/(\d+)/?$', views.deleteMineral, name='deleteMineral'),
    '''
    mineral = Minerals.objects.get(pk=id)
    if request.method != "POST":
        context_data = {'delete_form' : MineralForm(instance = mineral)}
        return render(request,'beamish2_app/entry_delete.html', context_data)
    else:
        name = MineralForm(instance = mineral)
        mineral.delete()
        return HttpResponseRedirect(reverse('listMineral'))

def deleteMines(request, id):
    '''
    url(r'^delete[m,M]ines/(\d+)/?$', views.deleteMines, name='deleteMines'),
    '''
    mine = Minesite.objects.get(pk=id)
    if request.method != "POST":
        context_data = {'delete_form' : MinesiteForm(instance = mine)}
        return render(request,'beamish2_app/entry_delete.html', context_data)
    else:
        name = MineralForm(instance = mine)
        mine.delete()
        return HttpResponseRedirect(reverse('listMines'))

def deleteCompany(request, id):
    '''
    url(r'^delete[c,C]ompany/(\d+)/?$', views.deleteCompany, name='deleteCompany'),
    '''
    company = Company.objects.get(pk=id)
    if request.method != "POST":
        context_data = {'delete_form' : CompanyForm(instance = company)}
        return render(request,'beamish2_app/entry_delete.html', context_data)
    else:
        name = CompanyForm(instance = company)
        company.delete()
        return HttpResponseRedirect(reverse('listCompany'))


#Individual views

def viewMineral(request, id):
    '''
    url(r'^view[m,M]ineral/(\d+)/?$', views.viewMineral, name='viewMineral'),
    '''
    mineral_id = int(id)
    mineral = Minerals.objects.get(pk=mineral_id)
    print(mineral)
    context_data = {'mineral' : mineral}
    return render(request, 'beamish2_app/mineral_view.html', context_data)

def viewMines(request, id):
    '''
    url(r'^view[m,M]ines/(\d+)/?$', views.viewMines, name='viewMines'),
    '''
    mine_id = int(id)
    mine = Minesite.objects.get(pk=mine_id)
    context_data = {'mine' : mine}
    return render(request, 'beamish2_app/mine_view.html', context_data)

def viewCompany(request, id):
    '''
    url(r'^view[c,C]ompany/(\d+)/?$', views.viewCompany, name='viewCompany'),
    '''
    company_id = int(id)
    company = Company.objects.get(pk=company_id)
    context_data = {'company' : company}
    return render(request, 'beamish2_app/company_view.html', context_data)
