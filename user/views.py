from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
#from django.contrib import messages
# from django.utils import timezone
from .models import User
# from .forms import MessageForm, SearchForm, StudentForm
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.contrib.auth.decorators import login_required
#from django_datatables_view.base_datatable_view import BaseDatatableView
#from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField
	
# Create your views here.
	
def home(request):
    return render(request,'base.html')

def user_dashboard(request):
    return render(request,'user/user_dashboard.html')
