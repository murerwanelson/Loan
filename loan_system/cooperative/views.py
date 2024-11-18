from django.shortcuts import render
from .models import Member, Loan

def dashboard(request):
    members = Member.objects.all()
    loans = Loan.objects.all()
    return render(request, 'cooperative/dashboard.html', {'members': members, 'loans': loans})
