from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as template
from todoapp import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index.as_view(), name='index'),
    path('login/', views.Mylogin.as_view(), name='login'),
    path('logout/', views.MyLogout.as_view(), name='logout'),
    path('home/',views.Homeadd, name='home'),
    path('dashboard/',views.dashboard.as_view(), name='dashboard'),
    path('signUp/', views.UserSignUp, name='signup'),
    path('about/', views.aboutSec, name='about'),
    path('yourNotes/', views.ViewNotes, name='yourNotes'),
    path('delete/<int:id>', views.deleteNotes, name='delete'),
    path('edit/<int:id>', views.editNotes, name='edit'),
    path('contactUs/', views.contactUs, name='contactUs'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

