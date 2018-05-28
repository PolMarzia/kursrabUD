from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html', locals())

def admin_page(request):
    return render(request, 'admin_page.html', locals())

def admin_redact(request):
    return render(request, 'admin_redact.html', locals())

def admin_add(request):
    return render(request, 'admin_add.html', locals())

def admin_delete(request):
    return render(request, 'admin_delete.html', locals())