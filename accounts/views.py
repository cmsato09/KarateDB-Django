from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def logged_in_dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})
    