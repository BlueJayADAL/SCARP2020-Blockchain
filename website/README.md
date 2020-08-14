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
Open project in Pycharm
Files included
  project_title/
    manage.py
    project_title/
      init.py
      settings.py
      urls.py
      asgi.py
      wsgi.py
  
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
