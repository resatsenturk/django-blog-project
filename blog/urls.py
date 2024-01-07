from django.urls import path
from blog.views import iletisim,anasayfa,kategori,yazilarim,detay,yazi_ekle,yazi_guncelle,yazi_sil,yorum_sil
from django.views.generic import TemplateView,RedirectView


urlpatterns = [
    path('',anasayfa,name='anasayfa'),
    path('hakkimda',TemplateView.as_view(
        template_name='pages/hakkimda.html'
        ),name='hakkimda'),
    path('yonlendir',RedirectView.as_view(
        url='https://www.google.com'
        ),name='iletisim'),
    path('iletisim',iletisim,name='iletisim'),
    path('kategori/<slug:kategoriSlug>',kategori,name='kategori'),
    path('yazilarim',yazilarim,name='yazilarim'),
    path('detay/<slug:slug>',detay,name='detay'),
    path('yazi-sil/<slug:slug>',yazi_sil,name='yazi-sil'),
    path('yazi-ekle',yazi_ekle,name='yazi-ekle'),
    path('yazi-guncelle/<slug:slug>',yazi_guncelle,name='yazi-guncelle'),
    path('yorum-sil/<int:id>',yorum_sil,name='yorum-sil'),
]
