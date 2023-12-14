"""cq_djangoBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from crimsonquest_django.views import crimson, about, myadmin, delete_user, map, Acampus, collegesA, facilitiesA, facilityMaps, primary, primaryMap, Bcampus, collegesB, facilitiesB, collegesMap, collegesMaps, facilityMap, highschoolMap, login, register, adminLogin, search_college, accSettings, regSuccess, errorPass, errorUname, errorSearch, errorLogin, errorUpdatePass, updateSuccess



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crimson),
    path('about', about),
    path('crimson/admin', myadmin),
    path('crimson/map', map),

    #========campus a=========
    path('crimson/map/Acampus', Acampus),
    path('crimson/map/Acampus/collegesA', collegesA, name='collegesA'),
    path('crimson/map/Acampus/collegesA/collegesMaps/<int:college_id>', collegesMaps, name='collegesMaps'),

    path('crimson/map/Acampus/facilitiesA', facilitiesA),
    path('crimson/map/Acampus/facilitiesA/facilityMaps/<int:facility_id>', facilityMaps, name='facilityMaps'),

    path('crimson/map/Acampus/primary', primary),
    path('crimson/map/Acampus/primary/primaryMap/<int:elem_id>', primaryMap, name='primaryMap'),


    #========campus b=========
    path('crimson/map/Bcampus', Bcampus),
    path('crimson/map/Bcampus/collegesB', collegesB, name='collegesB'),  # Add name to this URL pattern
    path('crimson/map/Bcampus/collegesB/collegesMap/<int:college_id>', collegesMap, name='collegesMap'),  # Add dynamic path parameter

    path('crimson/map/Bcampus/facilitiesB', facilitiesB, name='facilitiesB'),
    path('crimson/map/Bcampus/facilitiesB/facilityMap/<int:facility_id>', facilityMap, name='facilityMap'),

    path('crimson/map/Bcampus/highschoolMap/<int:hs_id>', highschoolMap, name='highschoolMap'),


    path('login', login),
    path('register', register),
    path('regSuccess', regSuccess),
    path('errorPass', errorPass),
    path('errorUname', errorUname),
    path('errorLogin', errorLogin),
    

    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('adminLog', adminLogin, name='admin_login'),

    path('crimson/map/search_college', search_college, name='search_college'),
    path('errorSearch', errorSearch),

    path('crimson/map/accSettings', accSettings, name='acc_settings'),
    path('crimson/map/accSettings/errorUpdatePass', errorUpdatePass),
    path('crimson/map/accSettings/updateSuccess', updateSuccess),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)