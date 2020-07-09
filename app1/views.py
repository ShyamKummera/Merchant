from django.contrib import messages
from django.shortcuts import render, redirect

from app1.forms import StockerForm, AddDispatcherForm
from app1.models import AdminLoginModel, StockerModel, AddDispatcherModel


def adminone(request):
    return render(request,'admin.html')


def loginpage(request):
    return render(request,'loginpage.html')


def afterlogin(request):
    u_name = request.POST.get('t1')
    pwd = request.POST.get('t2')
    try:
        alm = AdminLoginModel.objects.get(username=u_name,password=pwd)
        return render(request,'optionspage.html')
    except AdminLoginModel.DoesNotExist:
        return render(request,'loginpage.html',{"message":"Login Details Wrong"})


def stockerone(request):
    sf = StockerForm()
    view_stock = StockerModel.objects.all()
    return render(request,'stockerone.html',{"form":sf,"data":view_stock})


def savestocker(request):
    s_id = request.POST.get('idno')
    s_name = request.POST.get('name')
    s_cont = request.POST.get('contact_no')
    s_psw = request.POST.get('password')
    StockerModel(idno=s_id,name=s_name,contact_no=s_cont,password=s_psw).save()
    return redirect('stockerone')


def deletestocker(request):
    enter_del_id = request.POST.get('d1')
    sm = StockerModel.objects.values("idno")
    print(sm)
    l = []
    for x in sm:
        l.append(x["idno"])
    print(l)
    print(enter_del_id)
    if int(enter_del_id) in l:      # entered deleted id in string formate so we converted into 'int'
        print("i am if")
        StockerModel.objects.filter(idno=enter_del_id).delete()
        return redirect('stockerone')

    else:
        sf = StockerForm()
        print("i am else")
        view_stock = StockerModel.objects.all()
        messages.error(request, "Entered Idno not Found ")
        return render(request, 'stockerone.html', {"form": sf, "data": view_stock})

# ==========================add dispatcher=======================
def add_dispatcher(request):
    df = AddDispatcherForm()
    view_add_Disp = AddDispatcherModel.objects.all()
    return render(request,'add_dispatcher.html',{"form":df,"data":view_add_Disp})


def save_add_dispatcher(request):
    d_id = request.POST.get('idno')
    d_name = request.POST.get('name')
    d_cont = request.POST.get('contact_no')
    d_psw = request.POST.get('password')
    AddDispatcherModel(idno=d_id, name=d_name, contact_no=d_cont, password=d_psw).save()
    return redirect('add_dispatcher')


def delete_add_dispatch(request):
    enter_del_id = request.POST.get('d1')
    dm = AddDispatcherModel.objects.values("idno")
    print(dm)
    l = []
    for x in dm:
        l.append(x["idno"])
    print(l)
    print(enter_del_id)
    if int(enter_del_id) in l:  # entered deleted id in string formate so we converted into 'int'
        print("i am if")
        AddDispatcherModel.objects.filter(idno=enter_del_id).delete()
        return redirect('add_dispatcher')

    else:
        df = AddDispatcherForm()
        print("i am else")
        view_add_disp = AddDispatcherModel.objects.all()
        messages.error(request, "Entered Idno not Found ")
        return render(request, 'add_dispatcher.html', {"form": df, "data": view_add_disp})
