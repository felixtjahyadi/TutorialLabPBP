import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from wishlist.forms import WishListForm

@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Felix Tjahyadi',
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "wishlist.html", context)

def show_wishlist_ajax(request):
    context = {
    'nama': 'Felix Tjahyadi',
    }
    return render(request, "wishlist_ajax.html", context)

def wishlist_form(request):
    if request.method == "POST":
        form = WishListForm(request.POST)
        if form.is_valid():
            nama_barang = request.POST.get('nama_barang')
            harga_barang = request.POST.get('harga_barang')
            deskripsi = request.POST.get('deskripsi')
            wishlist = BarangWishlist(nama_barang = nama_barang, harga_barang = harga_barang, deskripsi= deskripsi)
            wishlist.save()
            response = HttpResponseRedirect(reverse("wishlist:wishlist_form")) 
            return response
    else:
        form = WishListForm()
    
    return render(request, 'wishlist_form.html', {'form':form})

def xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def json_id(request, id):
    data_id = BarangWishlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_id), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response