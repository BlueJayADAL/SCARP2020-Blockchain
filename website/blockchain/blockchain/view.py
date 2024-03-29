import os
import xml

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET
from django.shortcuts import render

from .settings import BASE_DIR
from .decorators import unauthenticated_user, allowed_users
from .forms import Display_Form
from .models import Display_File, Request_File

FILE_TYPES = ['txt', 'xml']


@login_required
def upload(request):
    form = Display_Form()
    if request.method == 'POST':
        form = Display_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_file = request.FILES['display_file']
            file_type = user_pr.display_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form}
    return render(request, 'profile_maker/create.html', context)


def index(request):
    # return render(request, "index.html", {})
    return render(request, "registration/login.html", {})


@login_required
@allowed_users(allowed_roles=['admin', 'patient', 'researcher'])
def homepage(request):
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



@login_required
@allowed_users(allowed_roles=['admin', 'patient', 'researcher'])
def study(request):
    id = request.GET['id']
    tree = ET.parse("blockchain/static/dataset/" + id + ".xml")
    content = tree.tostring()
    return render(request=request, template_name="study.html", context={"content": content})


@login_required(login_url='login')
def study(request, id):
    tree = ET.parse("blockchain/static/dataset/search_result/" + id + ".xml")
    content = tree.find("brief_summary").find("textblock").text

    return render(request=request, template_name="study.html", context={'content': content})


@login_required
@allowed_users(allowed_roles=['admin', 'patient', 'researcher'])
def data_center(request):
    current_email = request.user.email
    print(current_email)
    user_studies_queryset = Display_File.objects.all()

    all_studies = []

    for user_study in user_studies_queryset:

        study_json = {}
        study_xml_filename = '/uploadedstudydetails/' + user_study.display_file.name

        study_json["file_name"] = user_study.file_name
        study_json["display_file"] = user_study.display_file
        study_json["email"] = user_study.email
        study_json["display_file_path"] = study_xml_filename

        study_json["is_link"] = (user_study.email == current_email)

        all_studies.append(study_json)

    return render(request, "data_center.html", {'all_studies': all_studies})


@login_required
def uploaded_study_detail(request, study_id):
    # print(study_id)
    file_path = os.path.join(BASE_DIR, 'blockchain\\media\\' + study_id)
    study_details = open(file_path).read()
    return render(request, "uploadedstudydetails.html", {'uploaded_study_details': study_details})


def study_detail(request, study_id):
    print(study_id)

    if study_id.endswith('.xml'):
        # process the xml file
        whatever = 123

    file_path = os.path.join(BASE_DIR, 'blockchain\\studies\\' + study_id)
    study_details = open(file_path).read()
    return render(request, "studydetails.html", {'study_details': study_details})


@login_required
def requests(request):
    user_requests_queryset = Request_File.objects.all()

    all_requests = []

    for user_requests in user_requests_queryset:
        requests_json = {}

        requests_json["file_name"] = user_requests.file_name
        requests_json["status"] = user_requests.status
        requests_json["email"] = user_requests.email

        all_requests.append(requests_json)
    return render(request, "requests.html")

