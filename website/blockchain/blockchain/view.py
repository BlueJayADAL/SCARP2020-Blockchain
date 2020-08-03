import xml

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile
from easyrbac import Role, User, AccessControlList

FILE_TYPES = ['txt', 'xml']


everyone_role = Role('everyone')
admin_role = Role('admin')

everyone_user = User(roles=[everyone_role])
admin_user = User(roles=[admin_role, everyone_role])

acl = AccessControlList()

acl.resource_read_rule(everyone_role, 'GET', '/api/v1/employee/1/info')
acl.resource_delete_rule(admin_role, 'DELETE', '/api/v1/employee/1/')

# checking READ operation on resource for user `everyone_user`
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_read_allowed(user_role, 'GET', '/api/v1/employee/1/info') == True

# checking WRITE operation on resource for user `everyone_user`
# Since you have not defined the rule for the particular, it will disallow any such operation by default.
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_write_allowed(user_role, 'WRITE', '/api/v1/employee/1/info') == False

# checking WRITE operation on resource for user `admin_user`
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    if user_role == 'admin':  # as a user can have more than one role assigned to them
        assert acl.is_delete_allowed(user_role, 'DELETE', '/api/v1/employee/1/') == True
    else:
        assert acl.is_delete_allowed(user_role, 'DELETE', '/api/v1/employee/1/') == False


def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form}
    return render(request, 'profile_maker/create.html', context)


def index(request):
    # return HttpResponse("Hello World")
    return render(request, "index.html", {})


def homepage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        tree = ET.parse("blockchain/static/dataset/SearchResults.xml")

        all_studies = []

        for search_results_xml in tree.iter("search_results"):
            for study_xml in search_results_xml.iter("study"):
                study_json = {}
                study_json["id"] = study_xml.find("url").text.replace("https://ClinicalTrials.gov/show/", "")

                for data in study_xml:
                    if not data.text:
                        study_json[data.tag] = data.text
                    else:
                        study_json[data.tag] = data.text.strip()

                all_studies.append(study_json)
        return render(request=request, template_name="homepage.html", context={'all_studies': all_studies})
    else:
        # Return invalid login error message
        return HttpResponse("Login Error")


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def study(request):
    id = request.GET['id']
    tree = ET.parse("blockchain/static/dataset/" + id + ".xml")
    content = tree.tostring()
    return render(request=request, template_name="study.html", context={"content": content})


def study(request, id):
    tree = ET.parse("blockchain/static/dataset/search_result/" + id + ".xml")
    content = tree.find("brief_summary").find("textblock").text

    return render(request=request, template_name="study.html", context={'content': content})


def data_center(request):
    return render(request, "data_center.html", {})

