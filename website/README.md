## README FILE FOR GRACE

### Inital Necessary Installations
Python Version 3.7
IDE used: PyCharm
Install pip through command
  <p><code>python3 -m pip --version</code>
Install Django using pip
  <p><code>pip install Django==3.0.8</code>

### Creating a project
Through the command line cd to directory where Django is stored
<p><code>django-admin startproject project_title</code>
<p>Open project in Pycharm
<p>Files included:
<p>project_title/
<p>manage.py
        <p>project_title/
            <p>init.py
            <p>settings.py
            <p>urls.py
            <p>asgi.py
            <p>wsgi.py
  
To run project, cd to outer project_title directory
<p><code>python mange.py runserver</code>

To view: go to http://127.0.0.1:8000/

### Implementing template
Download preferred template from bootstrap.com

Create templates folder in project_title

Open up downloads folder

Move index.html into templates folder

Move css, js, and vendor folders into django projects static folder

### Implementing login feature
Create a file called login.css in static/jquery/ and add the following code
<p>body {
  display: -ms-flexbox;
  display: -webkit-box;
  display: flex;
  -ms-flex-align: center;
  -ms-flex-pack: center;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style></p>

<p>Create a folder called registration in templates folder
  
Create a file called login.html and add the following code
<p><code><!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">
    <title>Signin/title>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </head>
  <body class="text-center">
    <form class="form-signin">
      <img class="mb-4" src="https://getbootstrap.com/assets/brand/bootstrap-solid.svg" alt="" width="72" height="72">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input id="inputEmail" class="form-control" placeholder="Email address" required="" autofocus="" type="email">
      <label for="inputPassword" class="sr-only">Password</label>
      <input id="inputPassword" class="form-control" placeholder="Password" required="" type="password">
      <div class="checkbox mb-3">
        <label>
          <input value="remember-me" type="checkbox"> Remember me
        </label>
      </div>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      <p class="mt-5 mb-3 text-muted">© 2017-2018</p>
    </form>
  </body>
</html></code>
  
### Login Authentication

In view.py add
<p><code>from django.contrib.auth.decorators import login_required</code>

<p>Before any function that renders a page that requires a login add the decorator</p>
<p><code>@login_required</code>

<p>Create a python file called decorators
 <p><code>from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

</code>
<p>This function allows you to restrict certain groups of users from accessing pages</p>
### Displaying Data on Homepage after Login

<p>After users login a table of studies is displayed, in the following homepage.html
<p><code>{% extends 'base.html' %}
{% load static %}


{% block extra_head  %}
    <title>Homepage</title>

{% endblock extra_head %}

{% block extra_js %}
    <script></script>
{% endblock extra_js %}

<!-- Page Content -->
{% block content %}
<!-- Build the html table here
      using the {{ contextValue }} sent in-->
<table class="table table-bordered table-striped">
  <thead class="thead-dark">
    <tr>
      <th>Title</th>
      <th>Status</th>
      <th>Study Results</th>
      <th>Condition</th>
      <th>Intervention</th>
      <th>Location</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    {% for study in all_studies %}
    <tr>
      <td><a href="study/{{ study.id }}">{{ study.title }}</a></td>
      <td>{{ study.status }}</td>
      <td>{{ study.study_results }}</td>
      <td>{{ study.condition }}</td>
      <td>{{ study.intervention }}</td>
      <td>{{ study.location }}</td>
      <td>{{ study.url }}</td>
    </tr>
{% endfor %}
  </tbody>
  </tfoot>
</table>
{% endblock content %}
</code>

<p>This html code creates a table using the .xml file that was passed in by using a for loop to go through every study
<p><code>def homepage(request):
    tree = ET.parse("blockchain/static/dataset/SearchResults.xml")

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
    return render(request=request, template_name="homepage.html", context={'all_studies': all_studies})</code>
<p>This function parses the .xml file using Element Tree
  
<p>Then add the following path into urls.py
<p><code>path('homepage/', view.homepage, name="homepage"),</code>
  

### Showing a selected clinical trial on homepage
<p>In view.py in your homepage function, add the following to allow users to select a clinical trial and view more details
<p><code>study_json["id"] = study_xml.find("url").text.replace("https://ClinicalTrials.gov/show/", "")</code>
  
<p>This function parses the .xml file again, searching for a brief summary to display when the user clicks a study
<p><code>def study(request, id):
    tree = ET.parse("blockchain/static/dataset/search_result/" + id + ".xml")
    content = tree.find("brief_summary").find("textblock").text

    return render(request=request, template_name="study.html", context={'content': content})</code>
<p>In urls.py add the following path to view more details of a study
<p><code>path('study/<str:id>', view.study, name="study"),</code>
  
### Creating a data center and uploading files

<p>The following three sets of html code creates an upload page where users can upload files
<p>create.html  
<p><code>{% extends 'base.html' %}
{% load static %}

{% block extra_head %}
    <title>Upload</title>
{% endblock extra_head %}

{% block extra_js %}
    <script></script>
{% endblock extra_js %}

{% block content %}

    <center>
        <div>
            {% block replace %}
            <form method="POST" enctype="multipart/form-data" class="form">
                {% csrf_token %}
                <table class="table">
                    {{ form.as_table }}
                </table>
                <input type="submit" class="btn btn-primary btn-lg" name="register">
            </form>
            {% endblock replace %}
        </div>
    </center>

{% endblock content %}</code>
  
<p>details.html
  
<p><code>{% extends 'base.html' %}
{% load static %}

{% block extra_head %}

{% endblock extra_head %}

{% block content %}
<CENTER>
  <p>You have successfully uploaded your file!</p>
</CENTER>
{% endblock content %}</code>

<p>error.html

<p><code>{% extends 'base.html' %}
{% block replace %}
<CENTER>
    <h1 style = 'border: 5px red solid;'> hello, you have uploaded the wrong file type.</h1>
</CENTER>
{% endblock %}</code>

<p>In view.py this function allows users to upload
<p><code>def upload(request):
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
    return render(request, 'profile_maker/create.html', context)</code>
  
<p>In urls.py add the following path to upload
<p><code>path('upload/', view.upload, name='upload'),</code>

<p>Create an html file called datacenter to display these files
  
<p><code>{% extends 'base.html' %}
{% load static %}


{% block extra_head  %}
    <title>Data Center</title>

{% endblock extra_head %}

{% block extra_js %}
    <script></script>
{% endblock extra_js %}

<!-- Page Content -->
{% block content %}
<table class="table table-bordered table-striped">
    <thead class="thead-dark">
    <tr>
        <th>Filename</th>
        <th>Email</th>
        <th>File</th>
    </tr>
    </thead>
    <tbody>
    {% for study in all_studies %}
    <tr>
        <td>{{ study.file_name }}</td>
        <td>{{ study.email }}</td>
        <td>
        {% if study.is_link %}
            <a href={{ study.display_file_path }} >{{ study.display_file }}</a>
        {% else %}
            {{ study.display_file }}
        {% endif %}
        </td>
    </tr>
    {% endfor %}
    </tbody>
</table>
{% endblock content %}
</code>  

<p>In urls.py add the following path to the data center
<p><code>path('data_center/', view.data_center, name="data_center"),</code>
