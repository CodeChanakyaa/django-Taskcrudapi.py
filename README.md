# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/CodeSode10/django-Taskcrudapi.py

Now change directory to:

    $ cd django-Taskcrudapi.py
    $ cd CrudApi
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip3 install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py makemigrations    
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
