from django.shortcuts import render

def spoilage_dashboard(request):
    return render(request, 'spoilage_dashboard.html')