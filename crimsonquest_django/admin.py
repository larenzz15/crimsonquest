# admin.py

from django.contrib import admin
from .models import Campus
from .models import locationCategory
from .models import College
from .models import Facilities
from .models import Highschool
from .models import Elementary
from .models import Course



class CampusAdmin(admin.ModelAdmin):
    list_display = ('campusID', 'campusName', 'campusInfo')
    
admin.site.register(Campus)


class locationCategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryID', 'categoryName')
    
admin.site.register(locationCategory)

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('collegeID', 'colegeName', 'collegeMap', 'collegePic1', 'collegePic2', 'collegePic3', 'collegeInfo', 'campusID')
    
admin.site.register(College)


class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facilityID', 'facilityName', 'facilityMap', 'facilityPic1', 'facilityPic2', 'facilityPic3', 'facilityInfo', 'campusID')
    
admin.site.register(Facilities)


class HighschoolAdmin(admin.ModelAdmin):
    list_display = ('hsID', 'hsName', 'hsMap', 'hsPic1', 'hsPic2', 'hsPic3', 'hsInfo', 'campusID')
    
admin.site.register(Highschool)


class ElementaryAdmin(admin.ModelAdmin):
    list_display = ('elemID', 'elemName', 'elemMap', 'elemPic1', 'elemPic2', 'elemPic3', 'elemInfo', 'campusID')
    
admin.site.register(Elementary)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('courseID', 'courseName', 'courseInfo', 'coursePic', 'collegeID')
    
admin.site.register(Course)