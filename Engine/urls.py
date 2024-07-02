"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import re_path, include

urlpatterns = [
    re_path(r'^', include('Apps.data.urls')),
    # re_path(r'^', include('Apps.project.urls')),
    # re_path(r'^', include('Apps.category.urls')),
    # re_path(r'^', include('Apps.recyclebin.urls')),
    # re_path(r'^', include('Apps.Notification.urls'))
    # re_path(r'^', include('Apps.meter.urls')),
    # re_path(r'^', include('Apps.location.urls')),
    # re_path(r'^', include('Apps.graph.urls')),
    # re_path(r'^', include('Apps.notification.urls'))
]

