from django.urls import reverse
from .models import Bahagian,Tatatertib 
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .forms import BahagianForm
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField
from django.db import connection
# Create your views here.
def home2(request):
    return render(request,'pentadbiran/home.html')

# ----------------------------- Bahagian ------------------------------------------------------------------------------
# Senarai Bahagian
def home_bahagian(request):
    # return render(request, 'pentadbiran/bahagian_json2.html')
    return render(request, 'pentadbiran/bahagian_json.html')

# Tambah Bahagian
def bahagian_new(request):

    if request.method == "POST":
        form = BahagianForm(request.POST)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.save()
            messages.success(request, "Bahagian " + str(bahagian.NamaBahagian) + " telah dicipta ! ")
            return redirect(reverse_lazy('bahagian_home_json'))
    else:
        form = BahagianForm()
    print(request.user)
    return render(request, 'pentadbiran/bahagian_new.html', {'form': form})

# Kemaskini Bahagian
def bahagian_edit(request,pk):

    bahagian = get_object_or_404(Bahagian, pk=pk)
    if request.method == "POST":
        form = BahagianForm(request.POST,instance=bahagian)
        if form.is_valid():
            bahagian = form.save(commit=False)
            bahagian.save()
            # return redirect('post_detail', pk=post.pk)
            messages.success(request, "Bahagian " + str(bahagian.NamaBahagian) + " telah dikemaskini! ")
            return redirect(reverse_lazy('bahagian_home_json'))
    else:
        form = BahagianForm(instance=bahagian)
    
    return render(request, 'pentadbiran/bahagian_edit.html', {'form': form})

# Delete Bahagian
def bahagian_remove(request,pk):

    bahagian = get_object_or_404(Bahagian, pk=pk)
    # if request.method == "POST":
    namaBahagian = bahagian.NamaBahagian
    bahagian.delete()
    messages.success(request, "Bahagian : " + str(namaBahagian) + " telah dihapus! ")
    return redirect(reverse_lazy('bahagian_home_json'))

# Bahagian Detail
# def bahagian_detail(request,pk):
#     bahagian = get_object_or_404(Bahagian, pk=pk)
#     return render(request, 'pentadbiran/bahagian_detail.html', {'bahagian': bahagian})



# Bahagian JSON list filtering
class bahagian_list_json(BaseDatatableView):
    # order_columns = ['bil','namaBahagian','editLink', 'deletelink','pk']
    # order_columns = ['id','NamaBahagian','BUOrgChart','editLink','deletelink']
    order_columns = ['id','NamaBahagian','BUOrgChart','editLink','deletelink','pk']

    def get_initial_queryset(self):
        # icnum = self.request.GET.get(u'icnum', '')
        # return Student.objects.filter(icnum=icnum)
        return Bahagian.objects.all().order_by('BUOrgChart')

    def filter_queryset(self, qs):

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc
        
        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'NamaBahagian'
        elif iSortCol_0 == '2':
           sortcol = 'BUOrgChart'
        else:
           sortcol = 'NamaBahagian'


        # Choose which sorting direction : asc or desc
        if sSortDir_0 == 'asc':
          sortdir = ''
        else:
          sortdir = '-'

        # Filtering if search value is key-in
        if search:
          # Initial Q parameter value
          qs_params = None

          # Filtering other fields
          q = Q(BUOrgChart__icontains=search)|Q(NamaBahagian__icontains=search)
          qs_params = qs_params | q if qs_params else q
   
          # Completed Q queryset
          # print qs_params
          qs = qs.filter(qs_params)
          # print 'qs :' + str(qs)
          # print 'qs :'

        # print 'sortdir + sortcol : ' + sortdir + sortcol
        return qs.order_by(sortdir + sortcol)
        # return qs

    def prepare_results(self, qs):
        # prepare list with output column data
        # queryset is already paginated here
        # json_data = {}
        json_data = []

        for i in range(len(qs)):
            json_data.append([
                i+1,
                qs[i].NamaBahagian,
                qs[i].BUOrgChart,
                reverse_lazy('bahagian_edit',kwargs={'pk':qs[i].pk}),
                reverse_lazy('bahagian_remove',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('bahagian_detail',kwargs={'pk':qs[i].pk}),
                # reverse_lazy('urusetia_home'),
                str(qs[i].pk),
                
            ])
            # print(json_data)
        return json_data

# ----------------------------- Tatatertib ------------------------------------------------------------------------------

def datadb(request):
    import pyodbc
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=10.101.1.100;"
                      "Database=MCDB;"
                      "Trusted_Connection=yes;")

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MCDB.dbo.TblPersonel where ICNo='890211025433'")

    for row in cursor:
        print(row)
    return HttpResponse(row)


def my_acc(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT ICNo,Nama,NamaJawatan FROM dbo.TblPersonel WHERE ICNO='890211025433';")
        if cursor.rowcount == 0:
            html = "<html><body>There is no Course with number %s.</body></html>" 
        else:
            row = cursor.fetchone()
            output = 'Registration failed'
            #return render(request, 'personel.html',{"output": 'test'})
            return render(request, 'personel.html',context={'ICNo' :  row[0], 'Nama' : row[1],'NamaJawatan' : row[2]} )