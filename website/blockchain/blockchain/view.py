from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
import xml.etree.ElementTree as ET



def index(request):
    # return HttpResponse("Hello World")
    return render(request, "index.html", {})


def homepage(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        tree = ET.parse("C:\\Users\\grace\\Blockchain Repository\\SCARP2020-Blockchain\\website\\blockchain\\blockchain\\static\\dataset\\SearchResults.xml")

        all_studies = []

        for search_results_xml in tree.iter("search_results"):
            for study_xml in search_results_xml.iter("study"):
                study_json = {}

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


