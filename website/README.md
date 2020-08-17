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
<p><code>body {
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
</style></code>

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

<p>Create a python file called decorators
  
### Displaying Data on Homepage after Login

### Showing a selected clinical trial on homepage

### Creating a data center and uploading files


