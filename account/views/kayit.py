from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login,authenticate
from django import forms

def kayit(request):
        if request.method == 'POST':
            form=KayitFormu(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password1')
                email=form.cleaned_data.get('email')
                user=authenticate(username=username,password=password)
                login(request,user)
                return redirect('anasayfa')
        else:
            form=KayitFormu()
        return render(request,'pages/kayit.html',context={
            'form':form
        })
