from django.shortcuts import render
def anasayfa(request):
    context={
        'isim':'Reşat Şentürk'
    }
    return render(request,'pages/anasayfa.html',context=context)