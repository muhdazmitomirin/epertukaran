from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
# from django.utils import timezone
from .models import Bahagian
from .forms import BahagianForm
# from .forms import MessageForm, SearchForm, StudentForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.contrib.auth.decorators import login_required
#from django_datatables_view.base_datatable_view import BaseDatatableView
#from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField
	
# Create your views here.

def senarai_bhg(request):
    bhgs = Bahagian.objects.all().order_by('created_date')
    return render(request,'pentadbiran/senarai_bahagian.html',{'bhgs': bhgs})

def del_bhg(request,pk):
    
    bhg = get_object_or_404(Bahagian, pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            nama = bhg.nama
            bhg.delete()
            messages.success(request, "Bahagian " + str(nama) + " telah dihapuskan! ")
            return redirect(reverse_lazy('senarai_bahagian'))
        
    return render(request, 'pentadbiran/hapus_bahagian.html', {'bahagian': bhg, 'pk':pk})

def add_bhg(request):

    if request.method == "POST":
        form = BahagianForm(request.POST)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.createdby = request.user
            bahagian.save()
            messages.success(request, "Bahagian dengan rekod ID: " + str(bahagian.pk) + " telah berjaya ditambah! ")
            return redirect(reverse_lazy('senarai_bahagian'))
    else:
        form = BahagianForm()
    print(request.user)
    return render(request, 'pentadbiran/tambah_bahagian.html', {'form': form})

def edit_bhg(request,pk):

    bahagian = get_object_or_404(Bahagian, pk=pk)
    if request.method == "POST":
        form = BahagianForm(request.POST,instance=bahagian)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.createdby = request.user
            bahagian.save()

            messages.success(request, "Bahagian dengan rekod ID : " + str(bahagian.pk) + " telah berjaya dikemaskini! ")
            return redirect(reverse_lazy('senarai_bahagian'))
    else:
        form = BahagianForm(instance=bahagian)
    
    return render(request, 'pentadbiran/kemaskini_bahagian.html', {'form': form})