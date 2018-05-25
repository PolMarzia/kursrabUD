from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html', locals())

def admin_page(request):
    return render(request, 'admin_page.html', locals())