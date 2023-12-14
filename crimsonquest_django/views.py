from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.models import User as AuthUser
from django.shortcuts import redirect, get_object_or_404
from .models import Campus
from .models import locationCategory
from .models import College
from .models import Facilities
from .models import Highschool
from .models import Elementary
from .models import Course
from django.contrib import messages







# =====home=======
def crimson(request):
    return render(request, 'crimsonquest/crimson.html')

# =====about=======
def about(request):
    return render(request, 'crimsonquest/aboutt.html')


#======admin===========

def myadmin(request):
    # Retrieve total users
    total_users = User.objects.all().count()

    # Retrieve total colleges
    total_colleges = College.objects.all().count()

    total_facilities = Facilities.objects.all().count()

    total_courses = Course.objects.all().count()

    # Retrieve user data from auth_user
    users_data = AuthUser.objects.values('id', 'first_name', 'last_name', 'email')

    recent_users = AuthUser.objects.all().order_by('-date_joined')[:4]

    return render(request, 'crimsonquest/admin.html', {'total_users': total_users, 'total_colleges': total_colleges, 'total_facilities': total_facilities, 'users_data': users_data, 'total_courses': total_courses, 'recent_users': recent_users})



def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using email
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            # Login the user
            auth_login(request, user)
            return redirect('../crimson/admin')  # Assuming the URL pattern name for your admin page is 'admin'
        else:
            # Authentication failed, handle the error (e.g., display an error message)
            messages.error(request, 'Invalid credentials or insufficient permissions')

    return render(request, 'crimsonquest/adminLog.html')


def delete_user(request, user_id):
    user = get_object_or_404(AuthUser, id=user_id)
    user.delete()

    # Redirect to the 'crimson/admin' page
    return redirect('../../crimson/admin')

#====================================================================


#=========== account settings ==============

def accSettings(request):
    user = request.user  # Assuming the user is logged in

    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmNewPassword')

        # Update user information
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if new_password:
            if new_password == confirm_password:
                user.set_password(new_password)
            else:
                messages.error(request, 'New password and confirmation do not match.')
                return redirect('accSettings/errorUpdatePass')

        user.save()

        # Redirect to the account settings page or any other page
        messages.success(request, 'Your information has been updated successfully.')
        return redirect('accSettings/updateSuccess')

    return render(request, 'crimsonquest/accountSettings.html', {'user': user})


def errorUpdatePass(request):
    return render(request, 'crimsonquest/errorUpdatePass.html')

def updateSuccess(request):
    return render(request, 'crimsonquest/updateSuccess.html')


# =====map category=======
def map(request):
    campus_a = Campus.objects.get(campusID=1)
    campus_b = Campus.objects.get(campusID=2)

    context = {
        'campus_a': campus_a,
        'campus_b': campus_b,
    }
    return render(request, 'crimsonquest/map.html', context)



#=====campuss===============
def Acampus(request):
    colleges = locationCategory.objects.get(categoryID=1)
    facilities = locationCategory.objects.get(categoryID=2)
    primary = locationCategory.objects.get(categoryID=3)

    context = {
        'colleges': colleges,
        'facilities': facilities,
        'primary': primary,
    }

    return render(request, 'crimsonquest/Acampus.html', context)

def Bcampus(request):
    colleges = locationCategory.objects.get(categoryID=1)
    facilities = locationCategory.objects.get(categoryID=2)
    secondary = locationCategory.objects.get(categoryID=4)
    hs = Highschool.objects.get(hsID=1)

    context = {
        'colleges': colleges,
        'facilities': facilities,
        'secondary': secondary,
        'hs': hs,
    }
    return render(request, 'crimsonquest/Bcampus.html', context)
#==================================


# =====colleges A=========
def collegesA(request):
    carch = College.objects.get(collegeID=7)
    che = College.objects.get(collegeID=8)
    cla = College.objects.get(collegeID=9)
    claw = College.objects.get(collegeID=10)
    cn = College.objects.get(collegeID=11)
    coe = College.objects.get(collegeID=12)
    cte = College.objects.get(collegeID=13)
    cpads = College.objects.get(collegeID=14)
    csspe = College.objects.get(collegeID=15)

    context = {
        'carch': carch,
        'che': che,
        'cla': cla,
        'claw': claw,
        'cn': cn,
        'coe': coe,
        'cte': cte,
        'cpads': cpads,
        'csspe': csspe,
    }
    return render(request, 'crimsonquest/collegesA.html', context)

def get_college_courses(college_id):
    # Retrieve the courses for the given college
    return Course.objects.filter(collegeID=college_id)


def collegesMaps(request, college_id):
    college = College.objects.get(collegeID=college_id)
    courses = get_college_courses(college_id)

    context = {
        'college': college,
        'courses': courses,
    }

    return render(request, 'crimsonquest/collegesMaps.html', context)




#=========colleges B=================


def collegesB(request):
    cais = College.objects.get(collegeID=1)
    ccje = College.objects.get(collegeID=2)
    ccs = College.objects.get(collegeID=3)
    cswcd = College.objects.get(collegeID=4)
    csm = College.objects.get(collegeID=5)
    cm = College.objects.get(collegeID=6)

    context = {
        'cais': cais,
        'ccje': ccje,
        'ccs': ccs,
        'cswcd': cswcd,
        'csm': csm,
        'cm': cm,
    }
    return render(request, 'crimsonquest/collegesB.html', context)


def collegesMap(request, college_id):
    college = College.objects.get(collegeID=college_id)
    courses = get_college_courses(college_id)

    context = {
        'college': college,
        'courses': courses,
    }

    return render(request, 'crimsonquest/collegesMap.html', context)





#==============================================

#==========search function==============
def search_college(request):
    if request.method == 'GET':
        search_query = request.GET.get('search', '')

        try:
            # Try to find a College with the given name
            college = College.objects.get(collegeName__iexact=search_query)

            # Determine the campus and redirect
            if college.campusID_id == 1:
                return redirect('collegesMap', college_id=college.pk)
            elif college.campusID_id == 2:
                return redirect('collegesMaps', college_id=college.pk)

        except College.DoesNotExist:
            try:
                # If a College is not found, try to find a Facility with the facilityName
                facility = Facilities.objects.get(facilityName__iexact=search_query)

                # Determine the facility type and redirect accordingly
                if facility.facilityID == 1:
                    return redirect('facilityMap', facility_id=facility.pk)
                elif facility.facilityID in range(2, 19): 
                    return redirect('facilityMaps', facility_id=facility.pk)

            except Facilities.DoesNotExist:
                try:
                    # If a Facility is not found, try to find a Highschool with the given name
                    highschool = Highschool.objects.get(hsName__iexact=search_query)
                    return redirect('highschoolMap', hs_id=highschool.pk)

                except Highschool.DoesNotExist:
                    try:
                        # If a Highschool is not found, try to find an Elementary with the given name
                        elementary = Elementary.objects.get(elemName__iexact=search_query)
                        return redirect('primaryMap', elem_id=elementary.pk)

                    except Elementary.DoesNotExist:
                        # Handle the case when neither a College, Facility, Highschool, nor Elementary is found
                        return render(request, 'crimsonquest/errorSearch.html')

    # Handle other cases or render an appropriate template
    return render(request, 'crimsonquest/errorSearch.html')


def errorSearch(request):
    return render(request, 'crimsonquest/errorSearch.html')
#===========================================




# =====facilities=======

def facilitiesA(request):
    adblg = Facilities.objects.get(facilityID=5)
    ao = Facilities.objects.get(facilityID=6)
    cmm = Facilities.objects.get(facilityID=7)
    exe = Facilities.objects.get(facilityID=8)
    gym = Facilities.objects.get(facilityID=9)
    hhs = Facilities.objects.get(facilityID=10)
    lib = Facilities.objects.get(facilityID=11)
    osa = Facilities.objects.get(facilityID=12)
    regis = Facilities.objects.get(facilityID=13)
    rcc = Facilities.objects.get(facilityID=14)
    spec = Facilities.objects.get(facilityID=15)
    usa = Facilities.objects.get(facilityID=16)
    upress = Facilities.objects.get(facilityID=17)
    hostel = Facilities.objects.get(facilityID=18)

    context = {
        'adblg': adblg,
        'ao': ao,
        'cmm': cmm,
        'exe': exe,
        'gym': gym,
        'hhs': hhs,
        'lib': lib,
        'osa': osa,
        'regis': regis, 
        'rcc': rcc,
        'spec': spec,
        'usa': usa,
        'upress': upress,
        'hostel': hostel,

    }
    return render(request, 'crimsonquest/facilitiesA.html', context)


def facilityMaps(request, facility_id):
    facilities = Facilities.objects.get(facilityID=facility_id)
    context = {'facilities': facilities}
    return render(request, 'crimsonquest/facilityMaps.html', context)




def facilitiesB(request):
    clinic = Facilities.objects.get(facilityID=1)
    cafeteria = Facilities.objects.get(facilityID=2)
    tc = Facilities.objects.get(facilityID=3)
    msa = Facilities.objects.get(facilityID=4)

    context = {
        'clinic': clinic,
        'cafeteria': cafeteria,
        'tc': tc,
        'msa': msa,
    }
    return render(request, 'crimsonquest/facilitiesB.html', context)

def facilityMap(request, facility_id):
    facilities = Facilities.objects.get(facilityID=facility_id)
    context = {'facilities': facilities}
    return render(request, 'crimsonquest/facilityMap.html', context)

#================================

# =====elementary/highschool=======
def highschoolMap(request, hs_id):
    highschool = Highschool.objects.get(hsID=hs_id)
    context = {'highschool': highschool}

    return render(request, 'crimsonquest/highschoolMap.html', context)


def primary(request):
    g1 = Elementary.objects.get(elemID=1)
    g2 = Elementary.objects.get(elemID=2)
    g3 = Elementary.objects.get(elemID=3)
    g4_6 = Elementary.objects.get(elemID=4)
    ps = Elementary.objects.get(elemID=5)

    context = {
        'g1': g1,
        'g2': g2,
        'g3': g3,
        'g4_6': g4_6,
        'ps': ps
    }

    return render(request, 'crimsonquest/primary.html', context)


def primaryMap(request, elem_id):
    elementary = Elementary.objects.get(elemID=elem_id)
    context = {'elementary': elementary}

    return render(request, 'crimsonquest/primaryMap.html', context)


# =====login=======


def register(request):
    if request.method == 'POST':
        User = get_user_model()
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                # Check if the username already exists
                existing_user = User.objects.get(username=username)
                return redirect('../errorUname')
            except User.DoesNotExist:
                # If the username doesn't exist, create a new user
                User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                )
                return redirect('../regSuccess')
        else:
            return redirect('../errorPass')

    return render(request, 'crimsonquest/register.html')



def regSuccess(request):
    return render(request, 'crimsonquest/successRegister.html')


def errorPass(request):
    return render(request, 'crimsonquest/errorPass.html')

def errorUname(request):
    return render(request, 'crimsonquest/errorUname.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using email
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            auth_login(request, user)
            return redirect('../crimson/map')  # Adjust the URL pattern name if needed
        else:
            # Authentication failed, handle the error (e.g., display an error message)
            return render(request, 'crimsonquest/errorLogin.html')

    # Render the login page
    return render(request, 'crimsonquest/login.html')

def errorLogin(request):
    return render(request, 'crimsonquest/errorLogin.html')

#===map=====

