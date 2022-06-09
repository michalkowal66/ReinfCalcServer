# ReinfCalcServer

## About the ReinfCalcServer application

ReinfCalcServer is a [Django] web application created for the purpose of handling calculations requested by the [reinfCalc] desktop application.
The application comes with an account management system (users registration and login), a calculation [engine module], a task results handling system, and an admin panel.

## App's Tech Stack

- [Python3] - Main coding language of the application
- [Django] - Web development framework used for project's web application 
- [Bootstrap] - Front-end framework used for website components styling
- [MathJax] - Front-end framework used for displaying mathematical equations

*The application is a part of Reinforcement Calculator Project, see its other parts: [reinfCalc] desktop application, [engine module]*

## Using the application

### Installation and setup

After running the Django application locally on the host device or deploying it using hosting services, users gain access to the full functionality of the desktop application.

#### Running the application locally

In order to work with the application, its source code must be downloaded and dependencies installed.

First, download the source code or copy repository to the desired location.

Next, install all the required modules using following terminal command: 

`<path to the python script directory>\python -m pip install -r requirements.txt`

Use of virtual environment for running the script is advised in order to avoid conflicts between modules.
Instructions on creating a virtual environment in Python can be found in [Python docs on venv installation].

Then, inside the `<path to the application directory>\reinfCalc\reinfCalc` directory, create `.env` file 
containing the Django secret key (make sure to make it sufficiently complex and do not share it, as it will be used for cryptography purposes) as in an example below:


*.env file content*\
`SECRET_KEY=<your secret key>`


After setting up, the first migration must be made using following terminal commands:

`<path to the python script directory>\python manage.py makemigrations accounts`

`<path to the python script directory>\python manage.py migrate`

Finally, to run the application, run script `manage.py` using following terminal command:

`<path to the python script directory>\python manage.py runserver`

Once the application is running, the website can be accessed using default 'localhost:8000' or '127.0.0.1:8000' addresses.

*Note, that the application uses debug mode that should be disabled when deploying the application.*

#### Deployment

In order to deploy the application certain changes to the code must be introduced.
The process will not be explained here.
It is recommended to follow this [guide on Django applications deployment] to learn more about the topic.

### Site navigation

To navigate on the site users can use links in the navbar and the footer.

### Creating an account

In order to create an account user should visit the signup page using an appropriate link in the navbar.

After successfully creating an account, the user is taken to the login page.

### Accessing the results

To access the results user first needs to log in.

Once the user has logged in, the navbar displays additional link - Results. After the user does any calculations they'll show up there.

To access detailed results of calculations, the user has to select task and open the report page using the `Show Report` button.

   [Python3]: <https://www.python.org/> 
   [Django]: <https://www.djangoproject.com/>
   [guide on Django applications deployment]: <https://docs.djangoproject.com/en/4.0/howto/deployment/>
   [MathJax]: <https://www.mathjax.org/>
   [Bootstrap]: <https://getbootstrap.com/docs/5.1/getting-started/introduction/>
   [reinfCalc]: <https://github.com/michalkowal66/reinfCalc>
   [engine module]: <https://github.com/michalkowal66/reinfCalcEngine>
