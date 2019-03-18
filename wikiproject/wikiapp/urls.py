from django.views.static import serve

from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('search/', views.search, name='search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('createwiki/', views.createwiki, name='createwiki'),
    path('readwiki/<int:ID>/', views.readwiki, name='readwiki'),
    path('editwiki/<int:ID>/', views.editwiki, name='editwiki'),
    path('deletewiki/<int:ID>/', views.deletewiki, name='deletewiki'),

    path('createrelated/<int:postID>/', views.createrelated, name='createrelated'),
    path('readrelated/<int:ID>/', views.readrelated, name='readrelated'),
    path('editrelated/<int:ID>/', views.editrelated, name='editrelated'),
    path('deleterelated/<int:ID>/', views.deleterelated, name='deleterelated'),

    path('allwiki/', views.allwiki, name='allwiki'),

    path('newUser/', views.newUser, name='newUser'),
    path('userEntries/', views.userEntries, name='userEntries'),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),

]
