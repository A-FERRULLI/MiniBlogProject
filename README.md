# Mini Blog Website Project

A Mini Blog Website made for a school project.

<br>

You can view, create, edit, delete blog posts.

On a post, you can view, create, edit, delete comments.

# Requirements

Python >=3.11

If you want to create a Virtual Environment:
```bash
> python -m venv .
```

Then to activate it:
Windows CMD:
```bash
> .\Scripts\activate.bat
```

Linux & MacOS:
```bash
> source ./bin/activate
```

Librairies:
```bash
> pip install --no-cache-dir -r requirements.txt
```

*`--no-cache-dir` is used to force pip to get files online (grabbing newer files)*

# Usage

Before starting run these commands to create the database:
```bash
> python manage.py makemigrations BlogApp
> python manage.py migrate
```

To start the server, run this command:
```bash
> python manage.py runserver
```
