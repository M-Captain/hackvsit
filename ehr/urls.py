"""
URL configuration for ehr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.index, name='home'),
    path('dashboard/', views.case, name='dashboard'),
    path('', views.landing, name='landing'),
    path('addevidence', views.addevidence, name='addevidence'),
    path('case', views.case, name='case'),
    path('history', views.history, name='history'),
    path("evidence/<int:id>/", views.evidence, name="evidence"),
    path('camera', views.camera, name='camera'),
    path('report', views.report, name='report'),
    path('addreport', views.addreport, name='addreport'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)